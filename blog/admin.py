from django.contrib import admin
# from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category
# from .models import Tag, Comment


# Register your models here.

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    
admin.site.register(Category, CategoryAdmin)

# class TagAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug' : ('name',)}
    
# admin.site.register(Tag, TagAdmin)