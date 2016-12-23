from games.models import (
    GameCategory,
    Game,
    Player,
    PlayerScore
)

from games.serializers import GameCategorySerializer
from games.serializers import GameSerializer
from games.serializers import PlayerSerializer
from games.serializers import PlayerScoreSerializer
from games.serializers import UserSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter
from django_filters.rest_framework import DjangoFilterBackend

from games.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'scores': reverse(PlayerScoreList.name, request=request),
            'users': reverse(UserList.name, request=request)
            })


# GameCategory - GET and POST
# game-categories/
class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('name', )
    search_fields = ('^name', )
    ordering_fields = ('name', )


# GameCategory - GET, PUT, PATCH and DELETE
# game-category/{id}/
class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)


# Game - GET and POST
# games/
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )

    filter_fields = (
        'name',
        'game_category',
        'release_date',
        'played',
        'owner')
    search_fields = (
        '^name')
    ordering_fields = (
        'name',
        'release_date')

    def perform_create(self, serializer):
        # Pass an additional owner field to the create method
        # To set hte owner to the user received in the request
        serializer.save(owner=self.request.user)



# Game - GET, PUT, PATCH and DELETE
# game/{id}/
class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )

# Player - GET and POST
# players/
class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'
    filter_fields = (
        'name',
        'gender')
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        )

# Player - GET and POST
# player/{id}/
class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class PlayerScoreFilter(filters.FilterSet):
    # it is a django_filters.NumberFilter instsance that allows
    # thte client to filter the player scores whose score numeric value 
    # is greater than or equal to the specified number. The value for name
    # indicate the field to which the numeric filter is aplied, 'score',
    # and the lookup_expr value indicates the lookup expression, 'gte', 
    # which means >=
    min_score = NumberFilter(
        name='score', lookup_expr='gte')
    max_score = NumberFilter(
        name='score', lookup_expr='lte')
    from_score_date = DateTimeFilter(
        name='score_date', lookup_expr='gte')
    to_score_date = DateTimeFilter(
        name='score_date', lookup_expr='gte')
    player_name = AllValuesFilter(
        name='player__name')
    game_name = AllValuesFilter(
        name='game__name')

    class Meta:
        model = PlayerScore
        fields = (
            'score',
            'from_score_date',
            'to_score_date',
            'min_score',
            'max_score',
            'player_name',
            'game_name',
            )


# PlayerScore- GET and POST
# player-scores/
class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'
    filter_backends = (DjangoFilterBackend,)
    filter_class = PlayerScoreFilter
    ordering_fields = (
        'score',
        'score_date')


# PlayerScore- GET, PUT, PATCH and DELETE
# player-score/{id}/
class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'



