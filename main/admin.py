from django.contrib import admin
from . models import Category , Post, Comment
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','b_name','category','created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
