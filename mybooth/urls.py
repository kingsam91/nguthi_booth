from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.all_photos, name='allPhotos'),
     url(r'^photo/(\d+)',views.all_photos,name ='photo'),
    # url('^today_photos$',views.today_photos, name='todayPhotos')
    # url('^past_photos/(\d{4}-\d{2}-\d{2})/$',views.past_p hotos,name = 'pastPhotos') 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)