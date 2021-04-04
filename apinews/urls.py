from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="api-category-list"),
    path("categories/<int:pk>", CategoryDetailView.as_view(),
         name="api-category-detail")

]
