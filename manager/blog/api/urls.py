from rest_framework import routers
from .api import BlogViewSet

app_name = 'blog'

router = routers.DefaultRouter()
router.register('', BlogViewSet, 'blog')

urlpatterns = router.urls
