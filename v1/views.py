from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):
    def get(self, *args, **kwargs):
        return Response("Hi")