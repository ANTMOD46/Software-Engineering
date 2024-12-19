from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.shortcuts import render, redirect
from .forms import MemberForm, DrinkCategoryForm, DrinkRecipeForm
from .models import DrinkRecipe

from django.shortcuts import render
from .models import DrinkRecipe
from django.shortcuts import render, redirect
from .models import DrinkRecipe
from django.shortcuts import render
from .models import DrinkRecipe
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import DrinkRecipe
from django.shortcuts import render, get_object_or_404, redirect
from .models import DrinkRecipe

def home(request):
    # ดึงข้อมูลสูตรเครื่องดื่มล่าสุด
    recipes = DrinkRecipe.objects.all().order_by('-created_at')[:6]  # แสดง 6 สูตรล่าสุด
    return render(request, 'recipes/home.html', {'recipes': recipes})


def home_user(request):
    return render(request, 'recipes/home_user.html')




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_user')
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/signup.html', {'form': form})





# ฟังก์ชันเพิ่มสูตรเครื่องดื่ม
def create_recipe(request):
    if request.method == 'POST':
        form = DrinkRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.creator = request.user  # ผูกกับผู้สร้าง
            recipe.save()
            return redirect('home')  # ไปยังหน้า Home
    else:
        form = DrinkRecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})



def view_recipes(request):
    # ดึงข้อมูลสูตรทั้งหมดจากฐานข้อมูล
    recipes = DrinkRecipe.objects.all()
    return render(request, 'recipes/view_recipes.html', {'recipes': recipes})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        ingredients = request.POST['ingredients']
        steps = request.POST['steps']
        image = request.FILES.get('image')  # รับไฟล์ภาพจากฟอร์ม

        # บันทึกข้อมูลลงฐานข้อมูล
        DrinkRecipe.objects.create(
            name=name,
            category=category,
            ingredients=ingredients,
            steps=steps,
            image=image,
            creator=request.user
        )
        return redirect('view_recipes')
    return render(request, 'recipes/add_recipe.html')





def search_recipes(request):
    category_query = request.GET.get('category', '')

    if category_query:
        recipes = DrinkRecipe.objects.filter(category__icontains=category_query)
    else:
        recipes = DrinkRecipe.objects.all()

    return render(request, 'recipes/search_recipes.html', {'recipes': recipes, 'selected_category': category_query})




@login_required
def my_stats(request):
    # ดึงสูตรทั้งหมดที่ผู้ใช้สร้าง
    recipes = DrinkRecipe.objects.filter(creator=request.user)
    
    # นับจำนวนสูตรทั้งหมด
    total_recipes = recipes.count()

    # นับจำนวนสูตรแยกตามประเภท
    stats = (
        recipes.values('category')  # ใช้ 'category' เพื่อแยกตาม CharField
        .annotate(count=Count('category'))  # นับจำนวนในแต่ละประเภท
        .order_by('-count')
    )

    # แยกข้อมูลเป็น List สำหรับ Chart.js
    categories = [stat['category'] for stat in stats]
    counts = [stat['count'] for stat in stats]

    return render(request, 'recipes/my_stats.html', {
        'total_recipes': total_recipes,
        'categories': categories,  # รายชื่อประเภท
        'counts': counts,          # จำนวนในแต่ละประเภท
    })





def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(DrinkRecipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(DrinkRecipe, id=recipe_id)
    if request.method == 'POST':
        recipe.name = request.POST['name']
        recipe.category = request.POST['category']
        recipe.ingredients = request.POST['ingredients']
        recipe.steps = request.POST['steps']
        if 'image' in request.FILES:
            recipe.image = request.FILES['image']
        recipe.save()
        return redirect('view_recipes')
    return render(request, 'recipes/recipe_edit.html', {'recipe': recipe})

def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(DrinkRecipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('view_recipes')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})
