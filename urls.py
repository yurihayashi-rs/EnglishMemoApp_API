
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, UserViewSet, ManageUserView, HealthBodyViewSet,SocialRelationshipViewSet, TravelViewSet,\
    SchoolWorkViewSet, NatureViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)
router.register('healthbody', HealthBodyViewSet)
router.register('socialrelationship', SocialRelationshipViewSet)
router.register('travel',TravelViewSet)
router.register('schoolwork',SchoolWorkViewSet)
router.register('nature',NatureViewSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
]