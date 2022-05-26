from django.urls import path
from .views import(
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostCreateFeatureView,
    PostDetailFeatureView,
    PostDeleteFeatureView,
    PostUpdateFeatureView,
    UserPostListView
) 
from . import views

urlpatterns = [
    path('', views.home, name='whatsonzambia-home'),
    path('user/<str:email>', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='whatsonzambia-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feature/<int:pk>/', PostDetailFeatureView.as_view(), name='feature-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/new-feature/', PostCreateFeatureView.as_view(), name='post-create-feature'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/update-feature/', PostUpdateFeatureView.as_view(), name='feature-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/delete-feature/', PostDeleteFeatureView.as_view(), name='feature-delete'),
]