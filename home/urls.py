from django.urls import path

from home import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('sites/', views.ListSites.as_view(), name='sites'),
    path('site/<int:site_id>/', views.feed_site, name='feed-site'),
    path('add', views.AddNewSite.as_view(), name='add-site'),
]
