from django.urls import include, path
from rest_framework import routers

from project.viewsets.persons_viewsets import PersonViewSet

router = routers.DefaultRouter()
router.register(r'Persons', PersonViewSet, basename='persons')

urlpatterns = [
    path('', include(router.urls)),
]
