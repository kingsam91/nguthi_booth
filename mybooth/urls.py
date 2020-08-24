from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.welcome, name='welcome')
    # url('^today_photos$',views.today_photos, name='todayPhotos')
    # url('^past_photos/(\d{4}-\d{2}-\d{2})/$',views.past_p hotos,name = 'pastPhotos') 
]