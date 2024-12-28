from django.urls import path
from .views import CampaignListApiView,CampaignDetailApiView,SubscribeToCampaignApiView



urlpatterns = [
    path("campaigns",CampaignListApiView.as_view(),name="campaigns"),
    path("campaigns/<str:slug>",CampaignDetailApiView.as_view(),name="campaign"),
    path("subscribers",SubscribeToCampaignApiView.as_view(),name="subscribe")
]
