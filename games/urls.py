from django.conf.urls import url

from games import views


urlpatterns = [
    url(r'^users/$', 
        view=views.UserList.as_view(), 
        name=views.UserList.name),
    url(r'^user/(?P<pk>[0-9]+)/$', 
        view=views.UserDetail.as_view(), 
        name=views.UserDetail.name),

    url(r'^game-categories/$', 
    	view=views.GameCategoryList.as_view(), 
    	name=views.GameCategoryList.name),
    url(r'^game-categories/(?P<pk>[0-9]+)/$', 
    	view=views.GameCategoryDetail.as_view(), 
    	name=views.GameCategoryDetail.name),

    url(r'^games/$', 
    	view=views.GameList.as_view(), 
    	name=views.GameList.name),
    url(r'^game/(?P<pk>[0-9]+)/$', 
    	view=views.GameDetail.as_view(), 
    	name=views.GameDetail.name),

    url(r'^players/$', 
    	view=views.PlayerList.as_view(), 
    	name=views.PlayerList.name),
    url(r'^player/(?P<pk>[0-9]+)/$', 
    	view=views.PlayerDetail.as_view(), 
    	name=views.PlayerDetail.name),

    url(r'^player-scores/$', 
    	view=views.PlayerScoreList.as_view(), 
    	name=views.PlayerScoreList.name),
    url(r'^player-score/(?P<pk>[0-9]+)/$', 
    	view=views.PlayerScoreDetail.as_view(), 
    	name=views.PlayerScoreDetail.name),

    url(r'^$', 
    	view=views.ApiRoot.as_view(),
    	name=views.ApiRoot.name),
]
