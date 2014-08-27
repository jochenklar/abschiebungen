from rest_framework import serializers
from data.models import *

class AbschiebungBundeslaenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungBundeslaender