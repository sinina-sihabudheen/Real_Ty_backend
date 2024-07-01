from rest_framework import viewsets, status, generics, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from .models import Seller, LandProperty, ResidentialProperty, EmailDevice, Region, Buyer
from .serializers import SellerSerializer, RegionSerializer, LandPropertySerializer, ResidentialPropertySerializer, RegisterSerializer, OTPSerializer, OTPVerificationSerializer, ResendOTPSerializer
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.db import transaction
from rest_framework.permissions import AllowAny


User = get_user_model()


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class CustomLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        role = 'Buyer'  # Default to Buyer
        if hasattr(user, 'seller'):
            role = 'Seller'

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': role,
        }, status=status.HTTP_200_OK)
    
class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer  



####

   

    

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        is_seller = serializer.validated_data.get('is_seller', False)

        try:
            user = User.objects.get(email=email)
            return Response({'detail': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

       
        username = email 
        user = User.objects.create_user(username=username, email=email, password=password)

     
        device = EmailDevice.objects.create(user=user, email=email)
        device.generate_challenge()

        send_mail(
            'Your OTP Code',
            f'Your OTP code is {device.token}',
            'sinna.sihabudheen@gmail.com',
            [email],
            fail_silently=False,
        )

      
        return Response({
            'detail': 'OTP sent successfully',
            'email': email,
            'token': device.token  
        }, status=status.HTTP_200_OK)

class OTPVerificationView(generics.GenericAPIView):
    serializer_class = OTPVerificationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        token = serializer.validated_data['token']

        try:
            device = EmailDevice.objects.get(email=email, token=token, is_active=True)
        except EmailDevice.DoesNotExist:
            return Response({'detail': 'Invalid OTP or email'}, status=status.HTTP_400_BAD_REQUEST)

        # Activate user account
        try:
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Deactivate the device token after successful verification
        device.deactivate()

        return Response({'detail': 'OTP verified successfully'}, status=status.HTTP_200_OK)

class ResendOTPView(generics.GenericAPIView):
    serializer_class = ResendOTPSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        EmailDevice.objects.filter(user=user, is_active=True).update(is_active=False)
        self.send_otp(user)

        return Response({"detail": "OTP resent successfully"}, status=status.HTTP_200_OK)

    def send_otp(self, user):
        device = EmailDevice.objects.create(user=user, email=user.email)
        device.generate_challenge()
        send_mail(
            'Your OTP Code',
            f'Your OTP code is {device.token}',
            'sinna.sihabudheen@gmail.com',
            [user.email],
            fail_silently=False,
        )       

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class LandPropertyViewSet(viewsets.ModelViewSet):
    queryset = LandProperty.objects.all()
    serializer_class = LandPropertySerializer

class ResidentialPropertyViewSet(viewsets.ModelViewSet):
    queryset = ResidentialProperty.objects.all()
    serializer_class = ResidentialPropertySerializer



