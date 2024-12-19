from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_recipes, name='view_recipes'),  # ดูสูตรทั้งหมด
    path('add/', views.add_recipe, name='add_recipe'),  # เพิ่มสูตรใหม่
    path('search/', views.search_recipes, name='search_recipes'),  # ค้นหาสูตร
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # ดูรายละเอียดสูตร
    path('<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),  # แก้ไขสูตร
    path('<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),  # ลบสูตร
]
