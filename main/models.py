from django.db import models
from ckeditor.fields import RichTextField
from account.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.

# blog category
class Category(models.Model):
    name    = models.CharField(max_length=200)
    slug       = models.SlugField(max_length=200)
    category_img = models.CharField(max_length=300, default='https://images.unsplash.com/photo-1589827577276-65d717348780?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWVra2FofGVufDB8fDB8fHww&auto=format&fit=crop&w=600&q=60')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def get_absolute_url(self):
        return reverse("menu_link", args={self.slug})
    

# Post
class Post(models.Model):
    b_name      = models.CharField(max_length=200)
    author        = models.ManyToManyField(User)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at  = models.DateField(auto_now_add=True)
    modified_at= models.DateField(auto_now_add=True, blank=True)
    post            = RichTextField()
    post_img    = models.CharField( max_length=300, help_text='image url')
    tags            = TaggableManager()
    likeCount    = models.PositiveIntegerField(default=1)
    
    def get_absolute_url(self):
        return reverse("single_page", args=(self.pk, self.category.slug))

    def get_absolute_url_like_count(self):
        return reverse("like_count", kwargs={"pk": self.pk, "number":self.likeCount})
    
    
    
    def __str__(self):
        return self.b_name

# Comment
class Comment(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    email   = models.CharField(max_length=225)
    name   = models.CharField(max_length=100)
    comment = models.TextField()
    created_at  = models.DateField(auto_now_add=True)
