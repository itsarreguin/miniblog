from django.contrib import admin

from posts.models import Post
from posts.models import Comment
from posts.models import Like


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    
    pass


@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    
    pass