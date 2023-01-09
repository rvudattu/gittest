from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
import cx_Oracle
'''
# Create your views here.
from rest_framework import viewsets, generics, permissions, serializers
from allocation.models import *
from .serializers import *

from django.contrib import admin

admin.autodiscover()
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class QuoteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer
'''

from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['POST'])
def count_cur_sim(request):
    try:
        '''
        conn = cx_Oracle.connect('Apps/apps@omsddb.cswg.com:1521/omsd_app', encoding="UTF-8")
        query = f"select count(*) from apps.OMS_ALC_CURR_SIM_RESULTS"
        df = pd.read_sql(query, conn)
        res = df.to_dict('records')
        conn.close()
        return JsonResponse({"status": "success", "data": res})
        '''
        # Added a comment to Main by Pgarikap user.
        # Added a comment to Main by rvudattu user.
        return JsonResponse({"status": "success", "data": "Response from Git Poc Main branch version-4.0"})

    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})

@api_view(['GET'])
def getresponse(request):
    try:
        return JsonResponse({"status":"success", "msg": "success."})
    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})

@api_view(['post'])
def testApi(request):
    try:
        # Added change from sub user on 22-12-2022.
        return JsonResponse({"status":"success", "msg": "code merge ."})
    except Exception as e:
        return JsonResponse({"status": "failed", "msg": str(e)})
