from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, authentication, status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from .models import Card
from .serializers import UserSerializer, CardSerializer, FriendSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def destroy(self, request, pk):
        """
        Custom destroy method to limit card deletion to card creators
        """
        instance = self.get_object()
        if instance.creator == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("This Card does not belong to you", status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, permission_classes = [permissions.IsAuthenticated])
    def me(self, request):
        cards = request.user.cards.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    @action(detail=False, permission_classes = [permissions.IsAuthenticated])
    def all(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        #cards = Card.objects.all()
        #serializer = CardSerializer(cards, many=True)
        #return Response(serializer.data)

    @action(detail=False, permission_classes = [permissions.IsAuthenticated])
    def friends(self, request):
        cards = Card.objects.filter(creator__followers = request.user)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

class FollowedUserView(GenericAPIView):
    """
    Show friends that are being followed by the request.user
    """
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]  
    serializer_class = FriendSerializer
    def get(self, request, format=None):
        my_followed_users = User.objects.filter(followers=request.user)
        serializer = self.get_serializer(my_followed_users, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        """Add a User to your list of followed users"""
        name_of_user = request.data["user"]
        user_to_follow = User.objects.get(username=name_of_user)
        current_user = request.user
        current_user.followed_users.add(user_to_follow)
        return Response("User Added!", status=status.HTTP_200_OK)

        
class DeleteFollowedUser(APIView):
    """Remove a user from your list of followed users"""
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, user_id, format=None):  
        user_to_remove = get_object_or_404(User, id=user_id)
        current_user = request.user
        current_user.followed_users.remove(user_to_remove)
        return Response(status=status.HTTP_204_NO_CONTENT)

class FavoriteCardsView(GenericAPIView):
    pass