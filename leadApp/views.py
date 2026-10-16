from django.shortcuts import render
from leadApp.serializers import LeadSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from leadApp.models import Lead
from rest_framework import authentication,permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.

class LeadCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=['status','source']
    search_fields=['name','email','status','source']
    ordering_fields=['name','added_date']

class LeadRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
   
# class StatusLevelLeadsview(ListAPIView):
#     serializer_class=LeadSerializer
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     def get(self,request,*args,**kwargs):
#         new_leads=Lead.objects.filter(status="New")
#         contacted_leads=Lead.objects.filter(status="Contacted")
#         converted_leads=Lead.objects.filter(status="Converted")
#         lost_leads=Lead.objects.filter(status="Lost")
#         return Response({"New_leads":new_leads,"Contacted_leads":contacted_leads,"Converted_leads":converted_leads,"Lost_leads":lost_leads})

