from django.conf.urls import url
from nba import views

urlpatterns = [
	url(r'^team/$', views.team_list, name='team_list'), #list teams
 	url(r'^team/(?P<team_slug>[\w\s]+)/$', views.player_by_team, name='player_by_team'), #list players in a specified team
 	url(r'^team/(?P<team_slug>[\w\s]+)/(?P<cat_slug>[\w\s]+)/$', views.player_by_team_cats, name='player_by_team_cats'), #same as above, but by categories
 	url(r'^(?P<pk>\d+)/$', views.player_detail, name='player_detail'), #gives details of individual players
 	url(r'^$', views.player_list, name='player_list'), #lists all players
 	url(r'^categories/(?P<cat_slug>[\w\s]+)/$', views.player_list_cats, name='player_list_cats'), #same as above, but by categories 
 	url(r'^contactus/$', views.contact_us, name='contact_us'), #contact us
]