from project.models import persons
from rest_framework import viewsets
from rest_framework import permissions
from project.serializers.persons_serializer import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = persons.objects.all().order_by('id')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
