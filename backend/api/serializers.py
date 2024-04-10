from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {'author': {'read_only': True}}