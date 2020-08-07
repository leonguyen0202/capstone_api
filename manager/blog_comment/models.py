from django.db import models
from blog.models import Blog
from users.models import Users

# Create blog comment model.
class BlogComment(models.Model):
    content = models.TextField()
    blog_id = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog_comment'