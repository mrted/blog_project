from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from.models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer, UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting blog category instances.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting blog instances.
    """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author=user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
