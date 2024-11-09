from django.urls import path
from task_tracker import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task-create', views.TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('comment-delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)