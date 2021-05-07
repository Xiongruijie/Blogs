from django.contrib import admin
from doc_blog.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'modified_time', 'category', 'author']
    fields = ['name', 'body', 'excerpt', 'category', 'tags', 'create_time', 'modified_time']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)