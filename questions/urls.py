from django.conf.urls import url
from questions import views


urlpatterns = [
    url(r'^questions/$', views.question_list),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.question_detail),
]