- The problem I encountered while working on the Class-Based Serializers and Views along with the new Models (GameCategory, Player, PlayerScore) is all about typos regarding the field names and its type.

- to force makemigrations, do the following `python manage.py makemigrations <app name>`


```
# insert a new user
from	django.contrib.auth.models	import	User	
user	=	User.objects.create_user('kevin',	'kevin@example.com',	'kevinpassword')		
user.save()
```

## Gotchas:


#### Pagination
You can set the pagination for the response (or number of rows in your response).

in settings.py
```
REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS'	: 'rest_framework.pagination.Limit..',
	'PAGE_SIZE': 5
}
```
http://localhost/api/games/?limit=5&offset=5


#### Throttling

```
# in your settings.py
REST_FRAMEWORK = {
...
	'DEFAULT_THROTTLE_CLASSES': (
	    'rest_framework.throttling.AnonRateThrottle',
	    'rest_framework.throttling.UserRateThrottle'),
	'DEFAULT_THROTTLE_RATES': {
	    'anon': '5/hour',
	    'user': '20/hour',
	    'game-categories': '30/hour'
	},
}

# the previous code is a global thing,
# to override this and set a specific for class based view

class GameCategoryList(generics.ListCreateAPIView):
	...
	throttle_scope = 'game-categories'
	throttle_classes = (ScopeRateThrottle,)
```

You can test the throttling by running this command in your terminal:

```
for	i	in	{1..6};	do	http	:8000/player-scores/;	done;

for	i	in	{1..30};	do	http	:8000/game-categories/;	done;
```

####  Filtering, Searching and Ordering for views

`pip install django-filter`

`pip install django-crispy-forms`


```
   'DEFAULT_FILTER_BACKENDS': (
   		__'rest_framework.filters.DjangoFilterBackend',__
        # this class provides field filtA
        ering capabilities
        # it uses the previously installed django-filter package.
        # We can specify the set of fields we want to be able to filter against or create
        # a rest_framework.filters.FilterSet class with more customized settings and
        # associated it with the view.
        'rest_framework.filters.DjangoFilterBackend',

        # this class provides a single query parameter based searching capabilities
        # and it is based on Django admin's search function
        'rest_framework.filters.SearchFilter',

        # This class allows the client to control how the results
        # are orderd with a single-query parameter.
        'rest_framework.filters.OrderingFilter',
    )
```

```

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
        name='player__name', )
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
```

__NOTE: You need to add this `filter_backends = (DjangoFilterBackend,)` before the filter_class property of PlayerScoreList__



#### Testing

python manage.py text -v 2 // verbosity level 2