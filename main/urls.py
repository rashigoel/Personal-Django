from django.urls import path
from main import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path(r'', views.index, name='index'),

    path(r'^$', views.index, name='index'),
]

handler404 = views.index
handler500 = views.index
