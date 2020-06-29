from rest_framework import serializers
from .models import Project, Blog, Job, Category

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('pk','title', 'subtitle', 'description', 'image', 'github','url','featured')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        
class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    
    class Meta:
        model = Blog
        fields = ('pk','title', 'description', 'category', 'image', 'content','slug','created_at')

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('pk','company', 'position', 'date')