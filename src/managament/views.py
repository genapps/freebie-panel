from django.shortcuts import render
from rest_framework import viewsets
from .models import Address,Person,Item,Company,BusinessHours,RedemptionPoint,Transaction
from .serializers import AddressSerializer, PersonSerializer, ItemSerializer, CompanySerializer, BusinessHoursSerializer, RedemptionPointSerializer, TransactionSerializer
# Create your views here



class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class BusinessHoursViewSet(viewsets.ModelViewSet):
    queryset = BusinessHours.objects.all()
    serializer_class = BusinessHoursSerializer

class RedemptionPointViewSet(viewsets.ModelViewSet):
    queryset = RedemptionPoint.objects.all()
    serializer_class = RedemptionPointSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer