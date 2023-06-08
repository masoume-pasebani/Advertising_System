from django.urls import path
from . import views

urlpatterns = [
    path('show-ads/', views.ShowAds.as_view(), name='show-ads'),
    path('create-ad/', views.AdFormView.as_view(), name='create-ad'),
    path('click/<int:pk>/', views.CountClickAndRedirect.as_view(), name='count-click'),
    path('ad-detail/<int:pk>/', views.AdDetail.as_view(), name='ad-detail')
]
