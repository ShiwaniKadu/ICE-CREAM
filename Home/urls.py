from django.contrib import admin
from django.urls import path
from Home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', index,name="home"),
    path("about/", about,name="about"),
    path("services/", services,name="services"),
    path("contact/",contact,name="contact"),
    path("icecream/", icecream,name="Icecream"),
    path("delete-icecream/<id>/", delete_icecream,name="delete_icecream"),
    path('update-icecream/<id>/', update_icecream, name='update_icecream'),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()

