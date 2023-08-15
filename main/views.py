from django.shortcuts import render , redirect
from . models import Post , Category, Comment
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.

def home(request):
    posts   = Post.objects.all().order_by('-id')
    category = Category.objects.all().order_by('-id')
    
    fatwaa   = Post.objects.filter(category__name='fatwaa').order_by('-id')
    islam_think   = Post.objects.filter(category__name='islam think').order_by('-id')

    popularPost = Post.objects.filter(likeCount__gt = 4)
    
    context = {
        'post' : posts,
        'category' : category,
        'fatwaa':fatwaa,
        'islam_think':islam_think,
        'popularPost':popularPost,
    }
    return render(request, 'index.html', context)

def single_page(request,post_id,category_slug):
    post  = Post.objects.get(pk=post_id, category__slug = category_slug)
    
    comments    = Comment.objects.all()
    count = comments.count
    context = {
        'post' : post,
        'comments' : comments,
        'count':count
    }
    return render(request, 'single.html', context)

# Comment submit 
def comment(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        
        post = Post.objects.get(pk=id)
        Comment(post = post, name = name, email = email, comment = comment).save()
    # return HttpResponseRedirect(request.path_info)
    return HttpResponseRedirect('request.path_info')

        
# search function 
def search(request):
    query = request.GET.get('query')
    
    if query:
        post  = Post.objects.get(b_name__icontains=query)
    elif query:
        post  = Post.objects.get(author__icontains=query)
    else:
        post  = Post.objects.get(category__icontains=query)
        
        print(post)
    
    return HttpResponse(query)
    

# Like Count 
def like_count(request, pk, number):
    post    = Post.objects.get(pk=pk)
    post.likeCount += number
    post.save()
    print(pk)
    print(post)
    return redirect('/')





