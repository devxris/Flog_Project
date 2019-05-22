from django.contrib import admin


# Register your models here.
# to show model in admin page
from .models import Post

admin.site.register(Post)
