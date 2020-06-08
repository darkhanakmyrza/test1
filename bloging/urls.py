from django.urls import path
from .views import home, postView, PostDelete, PostUpdate, PostCreate

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>', postView, name='post'),
    path('create/<int:pk>/update', PostUpdate.as_view(), name='update_post'),
    path('create/', PostCreate.as_view(), name='create_post'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
    # ex: /blog/post/5/comment/

]