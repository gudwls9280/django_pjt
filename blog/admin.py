from django.contrib import admin
# from markdownx.admin import MarkdownxModelAdmin
# from .models import Post, Category, Tag, Comment
from .models import Post


# Register your models here.

admin.site.register(Post)

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug' : ('name', )}
    
# admin.site.register(Category, CategoryAdmin)

# class TagAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug' : ('name',)}
    
# admin.site.register(Tag, TagAdmin)