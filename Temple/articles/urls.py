from django.urls import path

from . import views
urlpatterns = [
    path('welcome/', views.WelcomeListView.as_view(), name='welcome'),
    path('pooja/', views.PoojaListView.as_view(), name='pooja'),
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'), # new
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    
]