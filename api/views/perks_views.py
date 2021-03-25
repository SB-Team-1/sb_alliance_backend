from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout

from ..serializers import PerksSerializer
from ..models.business import Perks

class AllPerks(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated)
    def get(self, request):
        """Index request"""
        perks = Perks.objects
        data = PerksSerializer(perks, many=True).data
        return Response({ 'perks': data })
        
class Perks(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated)
    serializer_class = PerksSerializer
    def get(self, request):
        """Index request"""
        perks = Perks.objects.filter(user=request.user.id)
        data = PerksSerializer(perks, many=True).data
        return Response({ 'perks': data })
    def post(self, request):
        """Create request"""
        request.data['perk']['user'] = request.user.id
        perk = PerksSerializer(data=request.data['perk'])
        if perk.is_valid():
            perk.save()
            return Response({ 'perk': perk.data }, status=status.HTTP_201_CREATED)
        return Response(perk.errors, status=status.HTTP_400_BAD_REQUEST)
class PerksDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated)
    def get(self, request, pk):
        """Show request"""
        perk = get_object_or_404(Perks, pk=pk)
        data = PerksSerializer(perk).data
        return Response({ 'perk': data })
    def delete(self, request, pk):
        """Delete request"""
        perk = get_object_or_404(Perks, pk=pk)
        if not request.user.id == perk.user.id:
            raise PermissionDenied('Unauthorized, you do not own this perk')
        perk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['perk'].get('user', False):
            del request.data['perk']['user']
        perk = get_object_or_404(Perks, pk=pk)
        if not request.user.id == perk.user.id:
            raise PermissionDenied('Unauthorized, you do not own this perk')
        request.data['perk']['user'] = request.user.id
        data = PerksSerializer(perk, data=request.data['perk'])
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)