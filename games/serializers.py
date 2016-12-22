from rest_framework import serializers

from .models import (
	Game, 
	GameCategory,
	Player,
	PlayerScore
)

import games.views


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
	# note that this is a link and is connected
	# to the GameDetail view class with 
	# name of `game-detail`
	games = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='game-detail')

	class Meta:
		model = GameCategory
		fields = (
			'url',
			'pk',
			'name',
			'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url', 
            'game_category', 
            'name', 
            'release_date',
            'played')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	game = GameSerializer()

	class Meta:
		model = PlayerScore
		fields = (
			'url',
			'pk',
			'score',
			'score_date',
			'game',
			)


class PlayerSerializer(serializers.ModelSerializer):
	scores = ScoreSerializer(many=True, read_only=True)
	gender = serializers.ChoiceField(
		choices=Player.GENDER_CHOICES)
	# the source string is built with get_ followed
	# by the `field name` (gender), and _display
	gender_description = serializers.CharField(
		source='get_gender_display',
		read_only=True)

	class Meta:
		model = Player
		fields = (
			'url',
			'name',
			'gender',
			'gender_description',
			'scores',
			)

class PlayerScoreSerializer(serializers.ModelSerializer):
	player = serializers.SlugRelatedField(queryset=Player.objects.all(),
					slug_field='name')
	game = serializers.SlugRelatedField(queryset=Game.objects.all(),
					slug_field='name')

	class Meta:
		model = PlayerScore
		fields = (
			'url',
			'pk',
			'score',
			'score_date',
			'player',
			'game'
			)

	