from django.urls import path

from posts import views
app_name = 'posts'

urlpatterns = [
    path('',views.PostListView.as_view(),name = 'all_post_group'),
    path('create/',views.CreatePost.as_view(),name = 'create_post'),
    path('<int:pk>/post_details/',views.PostDetailView.as_view(),name = 'post_details'),
    path('delete/<int:pk>/',views.DeletePostView.as_view(),name = 'delete_post'),
    path('<username>/all/',views.UserPosts.as_view(),name = 'all_posts_user')
]
