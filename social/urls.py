from django.urls import path
from .views import PostListView, ProfileView, ProfileEditView

urlpatterns = [  
    path('', PostListView.as_view(), name='post-list'), 
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
]