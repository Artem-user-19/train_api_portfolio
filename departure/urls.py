from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    TrainTypeViewSet,
    TrainViewSet,
    StationViewSet,
    RouteViewSet,
    CrewViewSet,
    JourneyViewSet,
    OrderViewSet,
    TicketViewSet,
    CountryViewSet,
    CityViewSet, UserRegistrationView
)

router = DefaultRouter()
router.register(r'train-types', TrainTypeViewSet)
router.register(r'trains', TrainViewSet)
router.register(r'stations', StationViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'crews', CrewViewSet)
router.register(r'journeys', JourneyViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]
