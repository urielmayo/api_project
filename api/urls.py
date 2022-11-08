from .views import (
    DealersView, DealerDetailView,
    VehiclesView, VehicleDetailView,
    AceesoriesView, AccesoryDetailView,
    PostsView, PostDetailView,
    LeadView,
)
from django.urls import path

urlpatterns = [
    path('dealer/', DealersView.as_view(), name='lc_deales'),
    path('dealer/<int:pk>/', DealerDetailView.as_view(), name='urd-dealers'),

    path('dealer/<int:dealer_pk>/vehicles/', VehiclesView.as_view(), name='lc-vehicles'),
    path('dealer/<int:dealer_pk>/vehicles/<int:pk>/', VehicleDetailView.as_view(), name='urd-vehicles'),

    path('dealer/<int:dealer_pk>/accesories/', AceesoriesView.as_view(), name='lc-accesories'),
    path('dealer/<int:dealer_pk>/accesories/<int:pk>/', AccesoryDetailView.as_view(), name='urd-accesories'),

    path('dealer/<int:dealer_pk>/posts/', PostsView.as_view(), name='lc-posts'),
    path('dealer/<int:dealer_pk>/posts/<int:pk>/', PostDetailView.as_view(), name='urd-posts'),

    path('dealer/<int:dealer_pk>/leads/', LeadView.as_view(), name='lc-leads'),

]