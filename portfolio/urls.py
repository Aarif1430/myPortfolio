from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^pdf_download/$', views.pdf_download, name='pdf_download'),
    url(r'^deploying_django_app_with_wsgi_in_apache/$', views.deploying_django_app_with_wsgi_in_apache, name='deploying_django_app_with_wsgi_in_apache'),
    url(r'^blogs/$', views.blogView.as_view(), name='blogs'),
    url(r'^about/$', views.aboutView.as_view(), name='about'),
]