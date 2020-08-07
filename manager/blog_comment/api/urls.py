from rest_framework.routers import DefaultRouter, SimpleRouter
from blog_comment.api.api import BlogCommentViewSet
from django.urls import path, include

app_name = 'blog_comment'
blog_comment_viewset_list = BlogCommentViewSet.as_view({'get': 'list'})
# blog_comment_viewset_create = BlogCommentViewSet.as_view({'post': 'create'})

router = DefaultRouter()
router.register('', BlogCommentViewSet, 'blog_comment')

urlpatterns = router.urls

# urlpatterns = [
#     # path('', blog_comment_viewset_list)
#     url(r'api/blog/<slug>/comments/(?P<comment_id>\d+)/', blog_comment_viewset_list)
# ]