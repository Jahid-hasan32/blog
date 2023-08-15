from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    # path('single_page/<slug:category>/', views.single_page, name="menu_link"),
    path('single_page/<int:post_id>/<slug:category_slug>/', views.single_page, name="single_page"),
    path('comment/<int:id>/', views.comment, name="comment"),
    path('like_count/<int:pk>/<int:number>/', views.like_count, name="like_count"),
    path('search/', views.search, name="search"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
