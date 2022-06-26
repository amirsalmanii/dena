from django.urls import path
from . import views

urlpatterns = [
    path('marks/', views.UserMarksView.as_view(), name='user_marks'),
    path('marks/<int:pk>/', views.DeleteMarkView.as_view(), name='mark_delete'),
    path('marks/ra/<int:pk>/', views.RemoveOrAddToMarksView.as_view(), name='mark_add_remove'),
]