from django.conf.urls import url
from nba import views

urlpatterns = [
 	url(r'^team/(?P<team_slug>[\w\s]+)/$', views.player_by_team, name='player_by_team'),
 	url(r'^(?P<pk>\d+)/$', views.player_detail, name='player_detail'),
 	url(r'^$', views.player_list, name='player_list'),
]