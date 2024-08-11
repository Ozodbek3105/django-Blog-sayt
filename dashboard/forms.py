from  blogs.models import Blog, Category
from django import forms
from django.contrib.auth.models import User
 # Category modelingizni import qiling
from django.contrib.auth.forms import UserCreationForm
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category  # Bu yerda modelingizni belgilash
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog  # Bu yerda modelingizni belgilash
        fields = ('title','category','featured_image','short_description','body','status','is_featured')


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_staff','is_active','is_superuser','groups','user_permissions')

class EditUserForm(forms.ModelForm ):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_staff','is_active','is_superuser','groups','user_permissions')