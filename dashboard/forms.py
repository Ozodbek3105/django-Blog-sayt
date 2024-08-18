from  blogs.models import Blog, Category
from django import forms
from django.contrib.auth.models import User, Permission
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
        fields = ('username','email','first_name','last_name','is_staff','is_active','groups','user_permissions')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    user_permissions = forms.ModelMultipleChoiceField(
    queryset=Permission.objects.filter(codename__in=['add_blog', 'view_blog', 'change_blog', 'delete_blog', 'add_category', 'view_category', 'change_category', 'delete_category']),
    widget=forms.SelectMultiple,
    required=False 
    )

class EditUserForm(forms.ModelForm ):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_staff','is_active','is_superuser','groups','user_permissions')
    
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.filter(codename__in=['add_blog', 'change_blog', "view_blog"]),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
