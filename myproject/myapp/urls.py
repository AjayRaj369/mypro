# from django.urls import path
# from myapp.views import employee

# from rest_framework.routers import DefaultRouter
# from .views import EmployeeViewSet


# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)



# urlpatterns = [

#     path('home/',employee),
    

# ]+router.urls




from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView,AdminOnlyView




urlpatterns = [
    # Registration URL
    path('api/register/', RegisterView.as_view(), name='register'),

    # JWT Token obtain (Login)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # JWT Token refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/admin-only/', AdminOnlyView.as_view(), name='admin_only'),

]



