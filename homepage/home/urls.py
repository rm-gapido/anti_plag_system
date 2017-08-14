from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^login/$', views.login, name='login'),
    url(r'^user/$', views.home, name='user_home'),
    url(r'^procedure/$', views.procedure, name='user_procedure'),
    url(r'^document_title/$', views.document_title, name='document_title'),
    url(r'^$', views.index, name='index'),
]