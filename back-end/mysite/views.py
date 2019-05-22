from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

def index(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        userS = serializer.validated_data['user']
        print(userS)
        user = User.objects.get(username=userS)
        user = UserSerializer(user, many=False)
        token, created = Token.objects.get_or_create(user=userS)
        return Response({
            'token': token.key,
            'user': user.data
        })

