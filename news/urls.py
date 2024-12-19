from django.http import HttpResponse
from django.urls import path, include
from news.views import *


urlpatterns = [
    path('', HomeNewsView.as_view(), name='home-page'),
    path('hotnews/', HomeNewsView.as_view(), name='hotnews-page'),
    path('dashboard/', DashboardView.as_view(), name='news-dashboard'),
    path('dashboard/add', NewsAddView.as_view(), name='news-add'),
    path('dashboard/edit/<int:pk>', NewsEditView.as_view(), name='news-edit'),
    path('login/', UserLoginView.as_view(), name='news-login'),
    path('logout/', UserLogoutView.as_view(), name='news-logout'),
    path('register/', UserRegisterView.as_view(), name='news-register'),
    path('dashboard/addtags', TagsAddView.as_view(), name='tags-form'),
    path('dashboard/delete/<int:pk>/', NewsDeleteView.as_view(), name='news-delete'),
    path('news/<int:pk>', NewsByIDView.as_view(), name="news-by-ID"),
    path('news/comment/<int:pk>', CommentAddViews.as_view(), name='comment-add'),
]