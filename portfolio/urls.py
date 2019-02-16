from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^pdf_download/$', views.pdf_download, name='pdf_download'),
    url(r'^post2/$', views.post2, name='post2'),
    url(r'^blogs/$', views.blogView.as_view(), name='blogs'),
    url(r'^about/$', views.aboutView.as_view(), name='about'),
]