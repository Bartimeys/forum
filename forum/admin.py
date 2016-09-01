from django.contrib import admin
from .models import Post, Category, Topic, UserEvent

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(UserEvent)
