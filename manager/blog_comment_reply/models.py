from django.db import models
from blog.models import Blog
from blog_comment.models import BlogComment
from users.models import Users

# Create blog comment reply model.
class BlogCommentReply(models.Model):
    content = models.TextField()
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(BlogComment, related_name="replies", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog_comment_reply'