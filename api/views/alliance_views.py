from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout

from ..serializers import AllianceSerializer

from ..models.business import Alliance

class AllAlliance(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated)
    def get(self, request):
        """Index request"""
        alliance = Alliance.objects
        data = AllianceSerializer(alliance, many=True).data
        return Response({ 'alliance': data })
        
class Alliance(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated)
    serializer_class = AllianceSerializer
    def get(self, request):
        """Index request"""
        alliance = Alliance.objects.filter(user=request.user.id)
        data = AllianceSerializer(alliance, many=True).data
        return Response({ 'alliance': data })
    def post(self, request):
        """Create request"""
        request.data['alliance']['user'] = request.user.id
        alliance = AllianceSerializer(data=request.data['alliance'])
        if alliance.is_valid():
            alliance.save()
            return Response({ 'alliance': alliance.data }, status=status.HTTP_201_CREATED)
        return Response(alliance.errors, status=status.HTTP_400_BAD_REQUEST)
class AllianceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated)
    def get(self, request, pk):
        """Show request"""
        alliance = get_object_or_404(Alliance, pk=pk)
        data = AllianceSerializer(alliance).data
        return Response({ 'alliance': data })
    def delete(self, request, pk):
        """Delete request"""
        alliance = get_object_or_404(Alliance, pk=pk)
        if not request.user.id == alliance.user.id:
            raise PermissionDenied('Unauthorized, you do not own this alliance')
        alliance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['alliance'].get('user', False):
            del request.data['alliance']['user']
        alliance = get_object_or_404(Alliance, pk=pk)
        if not request.user.id == alliance.user.id:
            raise PermissionDenied('Unauthorized, you do not own this alliance')
        request.data['alliance']['user'] = request.user.id
        data = AllianceSerializer(alliance, data=request.data['alliance'])
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)