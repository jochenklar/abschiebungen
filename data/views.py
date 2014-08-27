from rest_framework import viewsets
from data.models import *
from data.serializers import *

class AbschiebungBundeslaender(viewsets.ModelViewSet):
    queryset = AbschiebungBundeslaender.objects.all()
    serializer_class = AbschiebungBundeslaenderSerializer
