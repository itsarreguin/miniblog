from django_unicorn.components import UnicornView
from django_unicorn.components import QuerySetType

from posts.models import Post
from posts.models import Comment


class CommentView(UnicornView):
    
    content: str = ''
    comments: QuerySetType[Comment] = Comment.objects.none()
    
    def mount(self):
        self.comments = Comment.objects.all()
    
    def add_comment(self, post_id: int = None) -> None:
        post = Post.objects.filter(id=post_id).first()
        Comment.objects.create(author=self.request.user, post=post, content=self.content)
        
        self.comments = Comment.objects.all()
        self.content = ''