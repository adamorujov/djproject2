from django.contrib import admin
from blogs.models import BlogModel, CategoryModel, CommentModel
# Register your models here.

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    fields = ('title', 'categories', 'image', 'context', 'views_time', 'comment_number')
    search_fields = ('title',)

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    fields = ('name',)
    search_fields = ('name',)

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    fields = ('comment', 'blog', 'parent')
    search_fields = ('comment', 'blog', 'parent')