from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import CustomTokenObtainPairSerializer


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class MeApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField(required=True)
        email = serializers.CharField(required=True)

    def get(self, request):
        # Get the currently authenticated user
        requested_user = request.user

        data = self.OutputSerializer(requested_user).data

        return Response(data)
