from django.contrib import admin
from blog.models import Tag, Post, Comment

# To configure how the admin site behave with a certain model,
# a subclass of admin.ModelAdmin must be created_at

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)


