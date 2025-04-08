from rest_framework import serializers
from .models import WaitingUser, PDFDownloadUser

class WaitingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingUser
        fields = ['email', 'language']

class PDFDownloadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDownloadUser
        fields = ['email', 'language']