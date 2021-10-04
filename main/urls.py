from django.http import request
from django.urls import path
from .views import delete_post, home, detail, posts, create_post, latest_posts , search_result ,update_post , delete_post , error404 , profile_error
from django.views.static import serve 


urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("search", search_result, name="search_result"),
    path("update_post/<int:id>/",update_post, name="update_post"),
    path("delete_post/<int:id>/",delete_post, name="delete_post"),
    path("error404", error404, name="error404"),
    path("profile_error", profile_error, name="profile_error"),

    ]

#handler404 = 'main.views.error404'
