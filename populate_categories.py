import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog_project.settings")

# Initialize Django
django.setup()

# Now you can import your models
from blog.models import Category

# Define your function to populate categories
def populate():
    categories = [
        "Business",
        "Insurance",
        "Technology",
        "Real Estate",
        "Fashion & Lifestyle",
        "Automobile",
        "Health & Fitness",
        "Finance",
        "Food & Nutrition",
    ]

    for category_name in categories:
        category, created = Category.objects.get_or_create(name=category_name)
        if created:
            print(f"Created category: {category}")

if __name__ == "__main__":
    print("Populating categories...")
    populate()
    print("Categories populated.")
