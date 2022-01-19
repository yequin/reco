from rest_framework import serializers
from project.models import persons


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = persons
        fields = ['recorder', 'email', 'telefono']
