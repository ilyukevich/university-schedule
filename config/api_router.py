from django.conf import settings
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.accounts.api.views import (RegistrationAPIView, LoginAPIView, LogoutAPIView,
                                     ResetPasswordAPIView, UserViewSet, UserProfileViewSet)
from apps.university.api.views import (FacultiesViewSet, DepartamentsViewSet, StudyGroupsViewSet,
                                       AuditoriesViewSet, DisciplinesViewSet)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api"


router.register("users", UserViewSet, basename='user')
router.register('userprofiles', UserProfileViewSet, basename='userprofile')
router.register('faculties', FacultiesViewSet, basename='faculty')
router.register('departaments', DepartamentsViewSet, basename='faculty')
router.register('study-groups', StudyGroupsViewSet, basename='study-group')
router.register('auditories', AuditoriesViewSet, basename='auditory')
router.register('disciplines', DisciplinesViewSet, basename='discipline')


additional_urls = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registrations/', RegistrationAPIView.as_view(), name='registrations'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),

]

urlpatterns = router.urls + additional_urls
