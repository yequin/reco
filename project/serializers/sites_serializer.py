from rest_framework import serializers
from project.models import sites


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sites
        fields = ['daterecord', 'schedule', 'ubicacion', 'descripcion', 'site']