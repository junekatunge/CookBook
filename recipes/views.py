from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
#  API endpoint that allows recipes to be viewed, created, updated, and deleted.
    # """
    # API endpoint that allows recipes to be viewed, created, updated, and deleted.

    # - `GET /api/recipes/`: List all recipes.
    # - `GET /api/recipes/<pk>/`: Retrieve a specific recipe.
    # - `POST /api/recipes/`: Create a new recipe (requires authentication).
    # - `PUT /api/recipes/<pk>/`: Update a specific recipe (requires authentication and ownership).
    # - `DELETE /api/recipes/<pk>/`: Delete a specific recipe (requires authentication and ownership).
    # """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 
    search_fields = ['title', 'description', 'ingredients']
    ordering_fields = ['created_at', 'cooking_time', 'prep_time']
    filterset_fields = ['category', 'difficulty']
    
    def perform_create_recipe(self,serializer):
            #    Associates the recipe with the currently authenticated user when creating.
        serializer.save(author=self.request.user)
        
    def update(self,request, *args, **kwargs):
        #  Ensures only the recipe's author can modify it.
        instance =self.get_object()
        if instance.author != self.request.user:
            return Response({"detail":"You can only update your own recipes."},status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
    def destroy(self,request, *args, **kwargs):
        #     Ensures only the recipe's author can delete it.
        instance = self.get_object()
        if instance.author != self.request.user:
            return Response({"detail": "You can only delete your own recipes."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
        
