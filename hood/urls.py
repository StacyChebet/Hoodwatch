from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^accounts/profile/$', views.profile, name="profile"),
    url(r'^business/$', views.business, name="business"),
    url(r'^stations/$,', views.police_stations, name="stations"),
    url(r'^health/$', views.health, name="health"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
