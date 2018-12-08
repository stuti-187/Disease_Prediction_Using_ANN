from django.conf.urls import patterns, include, url
from . import views

app_name= 'symptomchecker'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #/symptomchecker/
    url(r'^$', views.index, name='index'),
    #/symptomchecker/123/
    #url(r'^(?P<disease_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.finddisease, name='finddisease'),
url(r'^searchdoctor/$', views.recommenddoctor, name='finddoctor'),
)
