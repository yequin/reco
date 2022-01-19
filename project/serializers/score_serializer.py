from rest_framework import serializers
from project.models import score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = score
        fields = ['recorder', 'score', 'site', 'objects']