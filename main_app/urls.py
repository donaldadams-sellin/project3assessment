from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addwidget/', views.add_widget, name='add_widget'),
    path('removewidget/<int:widget_id>/', views.remove_widget, name='remove_widget')
]