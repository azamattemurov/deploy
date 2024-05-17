from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [
    path('list/', NewsListView.as_view(), name='list'),
    path('new-detail/<int:pk>/', NewsDetailView.as_view(), name='new-detail'),
    path('new-create/', NewsCreateView.as_view(), name='new-create'),
    path('new-update/<int:pk>/', NewsUpdateView.as_view(), name='new-update'),
    path('new-delete/<int:pk>/', NewsDeleteView.as_view(),name='new-delete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', ThankYouView.as_view(), name='thank_you'),
]
