from django import forms
from .models import Member, DrinkRecipe, DrinkCategory

# ฟอร์มสำหรับ Member
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

# ฟอร์มสำหรับ DrinkCategory
class DrinkCategoryForm(forms.ModelForm):
    class Meta:
        model = DrinkCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

# ฟอร์มสำหรับ DrinkRecipe
class DrinkRecipeForm(forms.ModelForm):
    class Meta:
        model = DrinkRecipe
        fields = ['name', 'category', 'ingredients', 'steps', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List of Ingredients'}),
            'steps': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Steps to Prepare'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
