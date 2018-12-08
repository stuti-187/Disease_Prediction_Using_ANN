from django.conf.urls import patterns, include, url
from . import views

app_name= 'profile_user'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #/user/register/

    url(r'^register/$', views.usercreate, name='user-add'),
    url(r'^login/$', views.userlogin, name='user-check'),
    url(r'^editinfo/$', views.useredit, name='user-edit'),
    url(r'^editmedinfo/$', views.medhistedit, name='usermedit'),
url(r'^home/$', views.loggedinhome, name='userhome'),
url(r'^changepassword/$', views.changepassword, name='passchange'),
url(r'^locatehospital/$', views.locatehospital, name='hospital'),
url(r'^logout/$', views.logout, name='logout'),

                       )
