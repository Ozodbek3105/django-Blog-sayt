from django.contrib import admin

from blogs.models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id','title', 'status', 'is_featured', 'created_at')
    list_editable = ('is_featured','status', 'title')
    search_fields = ()
    

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)