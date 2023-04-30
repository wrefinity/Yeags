from django.urls import path
from .views import world_list_view, world_featured

app_name = "worlds"
urlpatterns = [
    path('list', world_list_view, name="world_list"),
    path('featured', world_featured, name="world_featured"),
]
