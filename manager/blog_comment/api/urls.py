from rest_framework.routers import DefaultRouter, SimpleRouter
from .api import BlogCommentViewSet

app_name = 'blog_comment'

router = DefaultRouter()
router.register('', BlogCommentViewSet, 'blog_comment')

urlpatterns = router.urls

# urlpatterns = [
#     path('', BlogCommentViewSet, name='comments'),
# ]