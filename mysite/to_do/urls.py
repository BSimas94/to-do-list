from django.conf.urls import url
from to_do import views

app_name = 'to_do'

urlpatterns = [
    url(r'^$',views.TaskListView.as_view(),name='list'),
    url(r'^create/$',views.TaskCreateView.as_view(),name='create'),
    url(r'^delete/(?P<pk>\d+)/$',views.TaskDeleteView.as_view(),name='delete')
]
