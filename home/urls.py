from django.urls import path

from home import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('sites/', views.ListSites.as_view(), name='sites'),
]
