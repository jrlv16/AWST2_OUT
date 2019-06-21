from django.contrib import admin, auth
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views
from . views import *

urlpatterns =[
    # path('personnels/', views.EntraineurListView.as_view(), name ='personnel_list'),
    path('clients/', views.ClientListView.as_view(), name = 'client_list'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name = 'client_detail'),
    path('client/create', views.ClientCreate.as_view(), name = 'client_creation'),
    path('client/update/<int:pk>', views.ClientUpdate.as_view(), name = 'client_maj'),
    path('client/c_update/<int:pk>', views.ClientClientUpdate.as_view(), name = 'clientclient_maj'),
    path('client/delete/<int:pk>', views.ClientDelete.as_view(), name = 'client_del'),
    path('personnel/create', views.EntraineurCreate.as_view(), name = 'entraineur_creation'),
    path('client/suivobs_byclient_list', views.SuiviByClientListView.as_view(), name = 'monsuivi'),
    path('client/suivobs__ent_byclient_list/<int:pk>', views.SuiviByClientEntrListView.as_view(), name = 'listsuivient'),
    path('client/suivobs_detail/<int:pk>', views.SuivobsDetailView.as_view(), name='suivi_detail'),
    path('client/suivi_create/<int:pk>', views.SuivobsCreate.as_view(), name='suivobs_creation'),
    path('suivi_tous', views.SuivobsList.as_view(), name ='tous_les_suivis'),
    path('client/password/', MyPasswordReset.as_view(), name='password'),
    ]
