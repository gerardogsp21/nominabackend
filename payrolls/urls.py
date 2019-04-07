from rest_framework import routers
from .api import PayrollViewSet

router = routers.DefaultRouter()
router.register('api/payrolls', PayrollViewSet , 'payrolls')

urlpatterns = router.urls