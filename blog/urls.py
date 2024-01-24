from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='main_home'),
    path('posts/<slug:slug>', views.PostListByCategory.as_view(), name='post_category'),
    path('post/<slug:slug>', views.index_post, name='main_post'),

    # manipulation of posts
    path('post/create/', views.CreatePost.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts_user', views.UserPostList.as_view(), name='user_posts')
]


