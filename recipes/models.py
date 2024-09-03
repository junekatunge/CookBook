from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class Recipe(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     instructions = models.TextField()
#     ingredients = models.TextField()
#     image = models.ImageField(upload_to='recipes/images/', blank=True)
#     cooking_time = models.IntegerField(default=0)
#     prep_time = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipes/images/', blank=True)
    cooking_time = models.IntegerField(default=0)
    prep_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Add a field for storing the recipe's category
    category = models.CharField(max_length=100, choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('snack', 'Snack'),
        ('other', 'Other'),
    ], default='other')

    # Add a field for storing the recipe's difficulty level
    difficulty = models.CharField(max_length=50, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ], default='medium')

    def __str__(self):
        return self.title