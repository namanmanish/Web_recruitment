from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/', views.detailes, name='detailes'),
    path('statistics/', views.statistics, name="statistics" ),
    path('new/', views.new, name="new"),
    path('ajax/', views.ajax, name="ajax"),
]
