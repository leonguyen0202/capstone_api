from rest_framework import routers
from .api import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register('', UserViewSet, 'users')

urlpatterns = router.urls
