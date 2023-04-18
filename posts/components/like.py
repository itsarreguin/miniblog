from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from django_unicorn.components import UnicornView

from posts.models import Post
from posts.models import Like


class LikeView(LoginRequiredMixin, UnicornView):
    
    likes: int = Like.objects.none()
    
    def mount(self) -> None:
        self.likes = Like.objects.count()
    
    def add_like(self, post_id: int = None) -> None:
        if not self.request.user.is_authenticated:
            return redirect('core:login')
        
        post = Post.objects.filter(id=post_id).first()
        like = Like.objects.filter(user=self.request.user, post=post).first()
        if like and like.user == self.request.user:
            like.delete()
        else:
            Like.objects.create(user=self.request.user, post=post)
        
        self.likes = Like.objects.count()