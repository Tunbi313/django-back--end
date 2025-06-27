from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser, Role
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

#api register
class RegisterView(APIView):
    def post(self,request):
        role_name = request.data.get('role','user')#user
        try:
            role = Role.objects.get(name = role_name)
        except ObjectDoesNotExist:
            return Response({"error":"not found Role"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_data = request.data 
        user_data['role'] = role.id
        serializer = UserSerializer(data= user_data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response({"error": "Invalid username"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.check_password(password):
            #tạo token khi mật khẩu chính xác
             refresh = RefreshToken.for_user(user)
             return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token), 
                'role': user.role.name, #trả về role người dùng
             })
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)


