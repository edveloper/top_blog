"""
# Custom form for the Post model
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'category': forms.Select(choices=[(category.id, category.name) for category in Category.objects.all()])
        }

# Custom admin class for the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'publication_date', 'author', 'category')  # Include 'category' in list_display
    list_filter = ('publication_date', 'category')  # Add 'category' to list_filter
    search_fields = ('title', 'author__username', 'category__name')  # Include 'category__name' in search_fields

# Register other models as you had them
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_filter = ('post',)
    search_fields = ('author__username', 'post__title')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')
    search_fields = ('email', 'full_name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
"""

from django import forms
from django.contrib import admin
from .models import Post, Comment, Subscriber, Category

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'author')
    list_filter = ('publication_date',)
    search_fields = ('title', 'author')
    form = PostAdminForm  # Use the custom form

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_filter = ('post',)
    search_fields = ('author', 'post__title')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'get_topics_display')
    search_fields = ('email', 'full_name', 'topics__name')

    def get_topics_display(self, obj):
        return ", ".join([topic.name for topic in obj.topics.all()])

    get_topics_display.short_description = 'Interested Topics'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

