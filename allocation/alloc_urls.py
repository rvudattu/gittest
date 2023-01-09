import django.conf.urls
from django.urls import path, include
from django.urls import path
from django.contrib.auth.models import User, Group

from allocation.views import count_cur_sim, getresponse, testApi, GroupList
from rest_framework import routers
from rest_framework import viewsets
# from restapi.models import *
from .serializers import *

# urlpatterns =[
# django.conf.urls.url(r'^count_cur_sim', count_cur_sim, name="To get count of rows.") ,
# ]

router = routers.DefaultRouter()
# router.register(r'quotes', QuoteViewSet, basename='QuoteViewSet')
# router.register(r'count_cur_sim', count_cur_sim, basename='count_cur_sim')
router.register(r'count_cur_sim', count_cur_sim.as_view(), basename='count_cur_sim')
router.register(r'groups', GroupList.as_view(), basename='count_cur_sim')

urlpatterns =[
    path('', include(router.urls)),
    path('groups', GroupList.as_view()),
    path(r'count_cur_sim', count_cur_sim.as_view(), name="To get count of rows."),
    # path('getresponse', getresponse, name="To get response."),
    # path('testApi', testApi, name="test api.")
]
