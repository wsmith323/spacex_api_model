from rest_framework.routers import SimpleRouter

from .views import LaunchpadViewSet

router = SimpleRouter()

router.register('launchpads', LaunchpadViewSet, basename='launchpad')

urlpatterns = router.urls
