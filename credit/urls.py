from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientView.as_view(), name='clients_list'),
    path('<int:id>/detail/', views.ClintDetailView.as_view(template_name='detail.html'), name='detail')
]
