from django.conf.urls import url
from questions import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^questions/$', views.question_list),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.question_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
