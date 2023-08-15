from .models import Category
from taggit.models import Tag

def menu_links(request):
    link = Category.objects.all()
    tags = Tag.objects.all()
    
    return dict(links = link, tag = tags)