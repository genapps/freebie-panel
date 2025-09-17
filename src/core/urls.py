from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from managament.views import AddressViewSet, PersonViewSet, ItemViewSet, CompanyViewSet, BusinessHoursViewSet, RedemptionPointViewSet, TransactionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Routers separados
address_router = DefaultRouter()
address_router.register(r'', AddressViewSet, basename='address')

person_router = DefaultRouter()
person_router.register(r'', PersonViewSet, basename='person')

item_router = DefaultRouter()
item_router.register(r'', ItemViewSet, basename='item')

company_router = DefaultRouter()
company_router.register(r'', CompanyViewSet, basename='company')

business_hours_router = DefaultRouter()
business_hours_router.register(r'', BusinessHoursViewSet, basename='businesshours')

redemption_point_router = DefaultRouter()
redemption_point_router.register(r'', RedemptionPointViewSet, basename='redemptionpoint')

transaction_router = DefaultRouter()
transaction_router.register(r'', TransactionViewSet, basename='transaction')











urlpatterns = [
    path('Address/', include(address_router.urls)),
    path('Person/', include(person_router.urls)),
    path('Item/', include(item_router.urls)),
    path('Company/', include(company_router.urls)),
    path('BusinessHours/', include(business_hours_router.urls)),
    path('RedemptionPoint/', include(redemption_point_router.urls)),
    path('Transaction/', include(transaction_router.urls)),
    
    path('api-auth/', include('rest_framework.urls')),
    path('i18n/', include('django.conf.urls.i18n')), 
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
