from django.conf.urls import url
from django.views.generic.base import TemplateView
from listOfComics import views

urlpatterns = [
url(r'^comics/$', views.ComicsView.as_view(), name='comics_signup'),
    url(r'^success/$', TemplateView.as_view(template_name='success.html'), name='success_page'),
    ]