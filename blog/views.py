from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.db.models import Q
from .forms import SearchForm
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Subscriber
from django.contrib import messages

def article_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/article_detail.html', {'post': post})
"""
def search_view(request):
    query = request.GET.get('q')
    articles = []
    
    if query:
        # Filter articles based on the query
        articles = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        # Create a list of dictionaries containing article titles and URLs
        results = [{'title': article.title, 'url': article.get_absolute_url()} for article in articles]
    
    # Return JSON response
    return JsonResponse(results, safe=False)
"""
def live_search(request):
    query = request.GET.get('q')
    articles = []

    if query:
        articles = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    results = [{'title': article.title, 'url': article.get_absolute_url()} for article in articles]

    return JsonResponse({'results': results})

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        topic_ids = request.POST.getlist("topics")  # Get a list of topic IDs
        topics = Category.objects.filter(id__in=topic_ids)  # Get the Category objects from IDs
        subscriber = Subscriber(full_name=name, email=email)
        subscriber.save()
        subscriber.topics.set(topics)  # Set the topics using Category objects
        messages.success(request, "Thank you for subscribing!")
        return redirect('blog:home')
    return render(request, 'blog/contact_us.html')

def category_posts(request, category_name):
    category = Category.objects.get(name=category_name)
    category_posts = Post.objects.filter(category=category)
    return render(request, f'blog/{category_name}.html', {'category_posts': category_posts, 'category': category})

def home(request):
    recent_posts = Post.objects.order_by('-publication_date')[:6]
    return render(request, 'blog/home.html', {'recent_posts': recent_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def business(request):
    business_posts = Post.objects.filter(category__name="Business")
    return render(request, 'blog/business.html', {'business_posts': business_posts})

def insurance(request):
    insurance_posts = Post.objects.filter(category__name="Insurance")
    return render(request, 'blog/insurance.html', {'insurance_posts': insurance_posts})

def technology(request):
    technology_posts = Post.objects.filter(category__name="Technology")
    return render(request, 'blog/technology.html', {'technology_posts': technology_posts})

def real_estate(request):
    real_estate_posts = Post.objects.filter(category__name="Real Estate")
    return render(request, 'blog/real_estate.html', {'real_estate_posts': real_estate_posts})

def fashion_lifestyle(request):
    fashion_lifestyle_posts = Post.objects.filter(category__name="Fashion & Lifestyle")
    return render(request, 'blog/fashion_lifestyle.html', {'fashion_lifestyle_posts': fashion_lifestyle_posts})

def automobile(request):
    automobile_posts = Post.objects.filter(category__name="Automobile")
    return render(request, 'blog/automobile.html', {'automobile_posts': automobile_posts})

def health_fitness(request):
    health_fitness_posts = Post.objects.filter(category__name="Health & Fitness")
    return render(request, 'blog/health_fitness.html', {'health_fitness_posts': health_fitness_posts})

def finance(request):
    finance_posts = Post.objects.filter(category__name="Finance")
    return render(request, 'blog/finance.html', {'finance_posts': finance_posts})

def food_nutrition(request):
    food_nutrition_posts = Post.objects.filter(category__name="Food & Nutrition")
    return render(request, 'blog/food_nutrition.html', {'food_nutrition_posts': food_nutrition_posts})

