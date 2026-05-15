import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import SensorData, Farm
from .serializers import SensorDataSerializer
from ml_model.predict import predict_irrigation

from .utils import (
    get_rain_forecast_by_coords,
    generate_zones,
    irrigation_decision
)

# ================= DASHBOARD =================
def dashboard(request):
    return render(request, 'dashboard.html')


# ================= TEST API =================
def test_api(request):
    return JsonResponse({"message": "Smart Irrigation Backend Working 🚀"})


# ================= SENSOR API =================
@csrf_exempt
@api_view(['POST'])
def add_sensor_data(request):

    logger.info("📥 Received sensor data request")

    serializer = SensorDataSerializer(data=request.data)

    if serializer.is_valid():
        sensor_data = serializer.save()

        lat = request.data.get("lat")
        lon = request.data.get("lon")

        if not lat or not lon:
            lat, lon = 13.0827, 80.2707  # Chennai fallback

        # 🌧 Weather API
        rain_forecast = get_rain_forecast_by_coords(lat, lon)

        # 🤖 ML INPUT
        data = [
            sensor_data.moisture,
            sensor_data.temperature,
            sensor_data.humidity,
            sensor_data.rainfall,
            rain_forecast
        ]

        prediction = predict_irrigation(data)

        return Response({
            "message": "Data saved successfully",
            "data": serializer.data,
            "rain_forecast": rain_forecast,
            "irrigation_needed": bool(prediction)
        })

    return Response(serializer.errors, status=400)


# ================= HISTORY =================
@api_view(['GET'])
def get_history(request):
    data = SensorData.objects.all().order_by('-timestamp')[:10]
    serializer = SensorDataSerializer(data, many=True)
    return Response(serializer.data)


# ================= LAST STATUS =================
@api_view(['GET'])
def last_status(request):
    last = SensorData.objects.last()

    if not last:
        return Response({"message": "No data"})

    lat, lon = 13.0827, 80.2707

    rain_forecast = get_rain_forecast_by_coords(lat, lon)

    data = [
        last.moisture,
        last.temperature,
        last.humidity,
        last.rainfall,
        rain_forecast
    ]

    prediction = predict_irrigation(data)

    return Response({
        "last_data": {
            "moisture": last.moisture,
            "temperature": last.temperature,
            "humidity": last.humidity,
            "rainfall": last.rainfall
        },
        "irrigation_needed": bool(prediction)
    })


# ================= SAVE FARM BOUNDARY =================
@api_view(['POST'])
@csrf_exempt
def save_boundary(request):

    farmer_id = request.data.get("farmer_id")
    boundary = request.data.get("boundary")

    if not boundary:
        return Response({"error": "No boundary provided"}, status=400)

    farm = Farm.objects.create(
        farmer_id=farmer_id,
        boundary=boundary
    )

    return Response({
        "message": "Boundary saved",
        "farm_id": farm.id
    })


# ================= GENERATE ZONES =================
@api_view(['GET'])
def get_zones(request, farm_id):

    try:
        farm = Farm.objects.get(id=farm_id)
    except Farm.DoesNotExist:
        return Response({"error": "Farm not found"}, status=404)

    zones = generate_zones(farm.boundary)

    return Response({
        "farm_id": farm_id,
        "zones": zones
    })


# ================= ZONE IRRIGATION =================
@api_view(['POST'])
def zone_irrigation(request):

    zones = request.data.get("zones")

    if not zones:
        return Response({"error": "No zone data provided"}, status=400)

    results = []

    for z in zones:
        moisture = z.get("moisture", 0)

        decision = irrigation_decision(moisture)

        results.append({
            "zone": z.get("zone"),
            "decision": decision
        })

    return Response({
        "results": results
    })