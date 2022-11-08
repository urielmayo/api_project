from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from .models import Dealer, Lead, Post, Vehicle, Accesory
from .serializers import (
    AccesorySerializer,
    DealerSerializer,
    LeadSerializer,
    PostSerializer,
    VehicleSerializer
)

# Create your views here.
class DealersView(ListCreateAPIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()

class DealerDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()


class VehiclesView(ListCreateAPIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = VehicleSerializer

    def get_queryset(self):
        dealer_pk = self.kwargs['dealer_pk']
        return Vehicle.objects.filter(dealer=dealer_pk)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['dealer'] = kwargs['dealer_pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = VehicleSerializer

    def get_queryset(self):
        dealer_pk = self.kwargs['dealer_pk']
        return Vehicle.objects.filter(dealer=dealer_pk)


class AceesoriesView(ListCreateAPIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = AccesorySerializer

    def get_queryset(self):
        dealer_pk = self.kwargs['dealer_pk']
        return Accesory.objects.filter(dealer=dealer_pk)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['dealer'] = kwargs['dealer_pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AccesoryDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = AccesorySerializer

    def get_queryset(self):
        dealer_pk = self.kwargs['dealer_pk']
        return Accesory.objects.filter(dealer=dealer_pk)


class PostsView(ListCreateAPIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = PostSerializer

    def get_queryset(self):
        dealer_pk = self.kwargs['dealer_pk']
        return Post.objects.filter(dealer=dealer_pk)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['dealer'] = kwargs['dealer_pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PostDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = PostSerializer

    def get_queryset(self):
        dealer_pk = self.kwargs['dealer_pk']
        return Post.objects.filter(dealer=dealer_pk)

class LeadView(ListCreateAPIView):
    http_method_names = ['get', 'post']
    serializer_class = LeadSerializer

    def get_queryset(self):
        dealer_pk = self.kwargs['dealer_pk']
        return Lead.objects.filter(dealer=dealer_pk)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['dealer'] = kwargs['dealer_pk']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)