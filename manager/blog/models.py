from django.db import models
from users.models import Users

# Create blog model.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    author_id = models.ForeignKey(Users, related_name='blogs', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog'