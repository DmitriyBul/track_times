from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter

from track_times.views import UserTimeViewSet, UserDetailView

app_name = 'track_times'
router = SimpleRouter()

router.register(r'times', UserTimeViewSet)
router.register(
    r'users/(?P<id>\d+)',
    UserDetailView, basename='api endpoint')

urlpatterns = [
    # path('times/', UserTimeViewSet),
    # path('times/<int:pk>/', UserDetail.as_view()),
]

urlpatterns += router.urls
#urlpatterns = format_suffix_patterns(urlpatterns)