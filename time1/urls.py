from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.timetable,name="timetable"),
    url(r'^/(?P<album_id>[0-9]+)/$',views.day,name='day'),

]
