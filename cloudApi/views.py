# from django.shortcuts import render
from http.client import ImproperConnectionState
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from cloudApi.models import RetailPrices
from cloudApi.serializers import UserSerializer, GroupSerializer, AzureApiSerializer
from rest_framework import serializers, viewsets, permissions, filters
from rest_framework.response import Response


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AzureApiViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows azure to be viewed or edited.
    """
    queryset = RetailPrices.objects.all()
    serializer_class = AzureApiSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['location', 'armskuname']
    ordering_fields = ['skuid']
    ordering = ['skuid']

    @action(detail=False, methods=['get'])
    def get_locations(self, request):
        locations = RetailPrices.objects.order_by(
            'location').values_list('location', flat=True).distinct()

        return Response(locations)

    @action(detail=False, methods=['get'])
    def get_instances(self, request):
        instances = RetailPrices.objects.order_by(
            'armskuname').values_list('armskuname', flat=True).distinct()

        return Response(instances)

    @action(detail=False, methods=['get'])
    def get_os(self, request):
        os = RetailPrices.objects.order_by('metername').values_list(
            'metername', flat=True).distinct()

        return Response(os)

    @action(detail=False, methods=['get'], url_path='get_prices_locations/(?P<location>[^/.]+)')
    def get_prices_locations(self, request, location):
        prices = RetailPrices.objects.all().order_by(
            'skuid').filter(location__contains=location)

        page = self.paginate_queryset(prices)

        if page is not None:
            serializer = self.get_serializer(prices, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='get_prices_skuname/(?P<armskuname>[^/.]+)')
    def get_prices_skuname(self, request, armskuname):
        prices = RetailPrices.objects.all().order_by(
            'skuid').filter(armskuname__contains=armskuname)

        page = self.paginate_queryset(prices)

        if page is not None:
            serializer = self.get_serializer(prices, many=True)

        return Response(serializer.data)

    # CPU BUSCAR
    @action(detail=False, methods=['get'], url_path='get_assesment/(?P<location>[^/.]+)/(?P<cpu>[^/.]+)/(?P<ram>[^/.]+)')
    def get_assesment(self, request, location, cpu, ram):
        prices = RetailPrices.objects.all().order_by(
            'skuid').filter(vmsizecpucores__lte=cpu, vmsizecpucores__gt=0, vmsizerammb__lte=ram, location__exact=location)

        page = self.paginate_queryset(prices)

        if page is not None:
            serializer = self.get_serializer(prices, many=True)

        return Response(serializer.data)
