from django.urls import path
from . import views
from .views import BorderDeleteView, BorderUpdateView, BorderDetailView, BorderCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('border/', views.borderListView.as_view(), name='border'),
    path('border/search/', views.border_search, name='search'),
    path('writing/', BorderCreateView.as_view(), name='writing'),
    path('border/delete/<int:pk>', BorderDeleteView.as_view(), name='delete'),
    path('border/modify/<int:pk>', BorderUpdateView.as_view(), name='modify'),
    path('border/detail/<int:pk>', BorderDetailView.as_view(), name='detail'),

    path('test/', views.test, name='test'),
]


