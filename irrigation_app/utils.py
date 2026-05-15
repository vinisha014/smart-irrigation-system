import requests
import logging

logger = logging.getLogger(__name__)

API_KEY = "ea5883054221c39ce906bedbcada7103"   # 🔥 move to env later


# ================= WEATHER FORECAST =================
def get_rain_forecast_by_coords(lat, lon):
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/forecast"
            f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            logger.error(f"❌ Weather API error: {response.status_code}")
            return 0

        data = response.json()

        # Check next few forecasts
        for item in data.get("list", [])[:5]:
            weather = item["weather"][0]["main"].lower()

            if "rain" in weather:
                logger.info("🌧 Rain expected")
                return 1

        logger.info("☀️ No rain expected")
        return 0

    except Exception as e:
        logger.error(f"❌ Weather fetch failed: {str(e)}")
        return 0


# ================= ZONE GENERATION =================
def generate_zones(boundary, num_zones=3):
    """
    Generate zone center points inside boundary
    """

    lats = [p[0] for p in boundary]
    lons = [p[1] for p in boundary]

    lat_min, lat_max = min(lats), max(lats)
    lon_min, lon_max = min(lons), max(lons)

    zones = []

    for i in range(num_zones):
        lat = (lat_min + lat_max) / 2 + (i * 0.001)
        lon = (lon_min + lon_max) / 2 + (i * 0.001)

        zones.append({
            "zone": i + 1,
            "lat": lat,
            "lon": lon
        })

    return zones


# ================= IRRIGATION LOGIC =================
def irrigation_decision(moisture):
    """
    Smart irrigation logic
    """

    if moisture < 30:
        return "FULL"       # 💧 full irrigation

    elif moisture < 60:
        return "PARTIAL"    # 🌱 moderate

    else:
        return "SKIP"       # 🚫 no irrigation