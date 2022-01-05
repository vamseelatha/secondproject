from rest_framework.serializers import  ModelSerializer
from.models import test
class testSerializer(ModelSerializer):
    class Meta:
        model=test
        fields="__all__"