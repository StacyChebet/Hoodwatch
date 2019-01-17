from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^accounts/profile/$', views.profile, name="profile"),
    url(r'^business/$', views.business, name="business"),
    url(r'^stations/$', views.police_stations, name="stations"),
    url(r'^health/$', views.health, name="health"),
    url(r'^add/business/$', views.add_business, name="add_business"),
    url(r'^add/post/$', views.add_post, name="add_post"),
    url(r'^add/hood/$', views.add_hood, name="add_hood"),
    url(r'^search/$', views.search_results, name="search_results")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
