from django.conf import settings

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'full_name', 'image_url']        
        read_only_fields = ['email']
