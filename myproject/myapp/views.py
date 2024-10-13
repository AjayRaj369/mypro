# from django.shortcuts import render, HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Employee
# from .serializers import EmployeeSerializer

# from rest_framework import viewsets
# from .models import Employee
# from .serializers import EmployeeSerializer




# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def employee(request):
#     if request.method == 'GET':
#         objEmployee = Employee.objects.all()
#         serializer = EmployeeSerializer(objEmployee, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = request.data
#         serializer = EmployeeSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    

#     elif request.method == 'PUT':
#         data = request.data
#         try:
#             obj = Employee.objects.get(id=data['id'])
#         except Employee.DoesNotExist:
#             return Response({"error":"person not found"}, status=404)
        
#         serializer = EmployeeSerializer(obj, data=data, partial=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)


#     elif request.method == 'PATCH':
#         data = request.data
#         try:
#             obj = Employee.objects.get(id=data['id'])
#         except Employee.DoesNotExist:
#             return Response({"error":"person not found"}, status=404)
        
#         serializer = EmployeeSerializer(obj, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    


#     elif request.method == 'DELETE':
#         data = request.data
#         try:
#             obj = Employee.objects.get(id=data['id'])
#         except Employee.DoesNotExist:
#             return Response({"error":"person not found"}, status=404)

#         obj.delete()
#         return Response({"message":"Employee deleted successfully"}, status=204)






# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer   






from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password


class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)


        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)  
        )

        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

from rest_framework.permissions import IsAdminUser

class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "You are an admin!"})




from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def get(self, request):
        return Response({"message": "Welcome, you are authenticated!", "user": request.user.username})


