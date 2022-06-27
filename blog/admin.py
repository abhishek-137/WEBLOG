from django.contrib import admin
from .models import Post,Author,Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=("title","author","post_date")
    list_filter=("author","tags")


admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

