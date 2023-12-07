from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),  # Your home page URL
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL for post_detail view
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('contact/', views.contact_us, name='contact_us'),
    #path('search/', views.search_view, name='search'),  # Add the search URL pattern
    path('live-search/', views.live_search, name='live_search'),
    path('category/business/', views.business, name='business'),  # URL for Business category
    path('category/insurance/', views.insurance, name='insurance'),  # URL for Insurance category
    path('category/technology/', views.technology, name='technology'),  # URL for Technology category
    path('category/real_estate/', views.real_estate, name='real_estate'),  # URL for Real Estate category
    path('category/fashion_lifestyle/', views.fashion_lifestyle, name='fashion_lifestyle'),  # URL for Fashion & Lifestyle category
    path('category/automobile/', views.automobile, name='automobile'),  # URL for Automobile category
    path('category/health_fitness/', views.health_fitness, name='health_fitness'),  # URL for Health & Fitness category
    path('category/finance/', views.finance, name='finance'),  # URL for Finance category
    path('category/food_nutrition/', views.food_nutrition, name='food_nutrition'),  # URL for Food & Nutrition category
]

"""

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),  # Your home page URL
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL for post_detail view
    path('category/business/', views.business, name='business'),  # URL for Business category
    path('category/insurance/', views.insurance, name='insurance'),  # URL for Insurance category
    path('category/technology/', views.technology, name='technology'),  # URL for Technology category
    path('category/real_estate/', views.real_estate, name='real_estate'),  # URL for Real Estate category
    path('category/fashion_lifestyle/', views.fashion_lifestyle, name='fashion_lifestyle'),  # URL for Fashion & Lifestyle category
    path('category/automobile/', views.automobile, name='automobile'),  # URL for Automobile category
    path('category/health_fitness/', views.health_fitness, name='health_fitness'),  # URL for Health & Fitness category
    path('category/finance/', views.finance, name='finance'),  # URL for Finance category
    path('category/food_nutrition/', views.food_nutrition, name='food_nutrition'),  # URL for Food & Nutrition category
]

"""