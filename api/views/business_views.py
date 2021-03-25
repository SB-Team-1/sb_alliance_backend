from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout

from ..serializers import BusinessSerializer

from ..models.business import Business

class AllBusiness(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated)
    def get(self, request):
        """Index request"""
        business = Business.objects
        data = BusinessSerializer(business, many=True).data
        return Response({ 'business': data })
        
class Business(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated)
    serializer_class = BusinessSerializer
    def get(self, request):
        """Index request"""
        business = Business.objects.filter(user=request.user.id)
        data = BusinessSerializer(business, many=True).data
        return Response({ 'business': data })
    def post(self, request):
        """Create request"""
        request.data['business']['user'] = request.user.id
        business = BusinessSerializer(data=request.data['business'])
        if business.is_valid():
            business.save()
            return Response({ 'business': business.data }, status=status.HTTP_201_CREATED)
        return Response(business.errors, status=status.HTTP_400_BAD_REQUEST)
class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated)
    def get(self, request, pk):
        """Show request"""
        business = get_object_or_404(Business, pk=pk)
        data = BusinessSerializer(business).data
        return Response({ 'business': data })
    def delete(self, request, pk):
        """Delete request"""
        business = get_object_or_404(Business, pk=pk)
        if not request.user.id == business.id:
            raise PermissionDenied('Unauthorized, you do not own this business')
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['business'].get('user', False):
            del request.data['business']['user']
        business = get_object_or_404(Business, pk=pk)
        if not request.user.id == business.id:
            raise PermissionDenied('Unauthorized, you do not own this business')
        request.data['business']['user'] = request.user.id
        data = BusinessSerializer(business, data=request.data['business'])
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)