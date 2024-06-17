from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("new/", views.new, name='new'),
    path("edit/", views.edit, name='edit'),
    path("update/<int:id>", views.update, name='update'),
    path("delete/<int:id>", views.delete, name='delete'),
    path("<str:area>/", views.area, name = 'area'),
    path("search/", views.search, name='search'),
    path("statistics/", views.statistics, name='statistics'),
]