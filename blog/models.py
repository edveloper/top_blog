from django.db import models
from django.contrib.auth.models import User  # Import User model
from django.urls import reverse
from django.conf import settings
import os

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

def default_post_image():
    return os.path.join(settings.MEDIA_URL, 'images', 'aggreg8-default-image.png')

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True, default=default_post_image)  # Add this line

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Assuming you have a 'post_detail' view with the name 'blog:post_detail'
        return reverse('blog:post_detail', args=[str(self.pk)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    topics = models.ManyToManyField(Category)  # Assuming Category represents the topics.

"""
# Creating instances for all 9 categories
business_category = Category.objects.create(name='Business')
insurance_category = Category.objects.create(name='Insurance')
technology_category = Category.objects.create(name='Technology')
real_estate_category = Category.objects.create(name='Real Estate')
fashion_lifestyle_category = Category.objects.create(name='Fashion & Lifestyle')
automobile_category = Category.objects.create(name='Automobile')
health_fitness_category = Category.objects.create(name='Health & Fitness')
finance_category = Category.objects.create(name='Finance')
food_nutrition_category = Category.objects.create(name='Food & Nutrition') """