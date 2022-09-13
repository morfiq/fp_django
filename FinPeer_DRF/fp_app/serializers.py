from rest_framework import serializers
from .models import fpuserdata


# class userDataSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = UserData
#         fields = '__all__'

#
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    # class Meta:
    #     model = UserData
    #     fields = "__all__"

class SaveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = fpuserdata
        fields = "__all__"