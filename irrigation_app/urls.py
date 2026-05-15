from django.urls import path
from .views import (
    test_api,
    add_sensor_data,
    dashboard,
    get_history,
    last_status,
    save_boundary,     # ✅ NEW
    get_zones,         # ✅ NEW
    zone_irrigation    # ✅ NEW
)

urlpatterns = [
    # 🌐 Dashboard
    path('', dashboard),

    # 🧪 Test
    path('test/', test_api),

    # 🌱 Sensor system
    path('sensor/', add_sensor_data),

    # 📊 Data APIs
    path('history/', get_history),
    path('status/', last_status),

    # 🗺 NEW FEATURES (IMPORTANT)
    path('save-boundary/', save_boundary),
    path('zones/<int:farm_id>/', get_zones),
    path('irrigation/', zone_irrigation),
]