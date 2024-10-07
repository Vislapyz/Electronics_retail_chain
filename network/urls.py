from rest_framework.routers import SimpleRouter

from network.apps import NetworkConfig
from network.views import NetworkObjectViewSet, ProductViewSet

app_name = NetworkConfig.name


router = SimpleRouter()
router.register("products", ProductViewSet)
router.register("networkobjects", NetworkObjectViewSet)

urlpatterns = [

              ] + router.urls