from django.urls import path

from . import views
urlpatterns = [
    path('welcome/', views.WelcomeListView.as_view(), name='welcome'),
    path('pooja/', views.PoojaListView.as_view(), name='pooja'),
    path('timing/', views.PoojaTimingListView.as_view(), name='poojaTiming'),
    path('detail/', views.PoojaDetailListView.as_view(), name='poojaDetail'),
    path('administration/', views.AdministrationListView.as_view(), name='administration'),
    path('addpooja/', views.AddPoojaListView.as_view(), name='addPooja'),
    path('poojaPrint/', views.PrintListView.as_view(), name='poojaPrint'),
    path('contact/', views.ContactListView.as_view(), name='contact'),
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'), # new
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
   
    
]