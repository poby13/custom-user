from django.conf.urls import url, include

from .views import ManagerHomeTV, MemberHomeTV


urlpatterns = [
    url(r'^member/$', MemberHomeTV.as_view(), name='member_welcome'),
    url(r'^manager/$', ManagerHomeTV.as_view(), name='manager_welcome'),
]