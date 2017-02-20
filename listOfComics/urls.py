from django.conf.urls import url
from django.views.generic.base import TemplateView
from listOfComics import views

urlpatterns = [
    url(r'^comics/$', views.ComicsView.as_view(), name='comics_signup'),
    url(r'^success/$', TemplateView.as_view(template_name='success.html'), name='success_page'),
    url(r'^my_list/$', views.my_list, name='my_list'),
    url(r'^comic_issue/(?P<pk>\d+)/$', views.IssueView.as_view(), name='issue_profile'),
    url(r'^my_comics/(?P<pk>[0-9]+)/$',views.ComicUpdateView.as_view(), name='comic_update'),
    url(r'^my_comics/(?P<pk>[0-9]+)/delete/$',views.ComicDeleteView.as_view(), name='comic_delete')
    
    ]