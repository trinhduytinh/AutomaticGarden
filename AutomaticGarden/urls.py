from django.urls import include, path
from . import views
urlpatterns = [
    # path('', views.control_lights_and_watering, name='control_lights_and_watering'),
    path('', views.index, name='index'),
]