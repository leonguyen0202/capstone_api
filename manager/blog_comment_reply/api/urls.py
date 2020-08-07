from rest_framework.routers import DefaultRouter, SimpleRouter
from .api import BlogCommentReplyViewSet

app_name = 'blog_comment_reply'

router = DefaultRouter()
router.register('', BlogCommentReplyViewSet, 'blog_comment_reply')

urlpatterns = router.urls