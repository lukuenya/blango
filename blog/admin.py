from django.contrib import admin
from blog.models import Tag, Post 

# Register your models here.
admin.site.register(Tag)

# To configure how the admin site behave with a certain model,
# a subclass of admin.ModelAdmin must be created_at

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('title', 'published_at')

admin.site.register(Post, PostAdmin)
