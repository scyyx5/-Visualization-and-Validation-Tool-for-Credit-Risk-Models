"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from polls.views import *
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from django.conf.urls import url
from django.urls import re_path as url



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v3',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      #terms_of_service="http://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #path('', views.index, name='index'),
    #path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    path('api/v4/login/', log_in2,name = 'user log in'),
    path('api/v4/Register/',Register.as_view(), name='auth_register'),
    path('api/v4/adjust/',adjust_apc, name = "adjust_apc"),
    path('api/v4/download_graph/', download_graph4,name = 'download_graph4'),
]

'''
    path('api/v1/addCondition/',addCondition, name = "addCondition"),
    path('api/v1/adjust/',adjust, name = "adjust"),
    path('api/v3/download_graph/', downloadGraph3,name = 'downloadGraph3'),
    path('api/v2/download_graph/', downloadGraph2,name = 'downloadGraph2'),
    #path('api/v2/download_graph_blind/', downloadGraphisBlind2,name = 'downloadGraphisBlind2'),
    path('api/v1/download_graph/', downloadGraph,name = 'downloadGraph'),
    path('api/v1/download_graph_blind/', downloadGraphisBlind,name = 'downloadGraphisBlind'),
    path('api/v1/download_dr_age_blind/', download_dr_age_blind,name = 'download_dr_age_blind'),
    path('api/v1/download_dr_cal_blind/', download_dr_cal_blind,name = 'download_dr_cal_blind'),
    path('api/v1/download_apc_blind/', download_apc_blind,name = 'download_apc_blind'),
    path('api/v1/download_dr_age/', download_dr_age,name = 'download_dr_age'),
    path('api/v1/download_dr_cal/', download_dr_cal,name = 'download_dr_cal'),
    path('api/v1/download_lexis/', download_lexis,name = 'download_lexis'),
    path('api/v1/download_apc/', download_apc,name = 'download_apc'),
    #url(r'^download_dr_age/',download_dr_age,name="download_dr_age"),
    #url(r'^download_dr_cal/',download_dr_cal,name="download_dr_cal"),
    '''