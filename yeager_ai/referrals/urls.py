from django.urls import path
from . import views

app_name="referrals"

urlpatterns = [
	path('referrals/', views.ReferralProfileView.as_view(), name='view-referral-profile' ),
	]