
Save new game category
`http POST :8000/api/game-categories/ name='2d mobile arcade'`


Save new game
```
http POST :8000/api/games/	name='The Last of us'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http -a markronquillo:'testing123' POST :8000/api/games/	name='The Last of us'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='PvZ Garden Warfare	4'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Superman vs Aquaman'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Tetris Reloaded'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Puzzle Craft'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Blek'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Scribblenauts Unlimited'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Tiny Dice Dungeon'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='A Dark Room'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Bastion'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='Welcome to the Dungeon'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

http POST :8000/api/games/	name='An Elysian Tail'	game_category='2d mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'

```

Save new players
```
http POST :8000/api/players/ name='Barnacle' gender='M'
http POST :8000/api/players/ name='Kevin' gender='M'

```


Save Player Scores
```
http POST :8000/api/player-scores/ score=35000	score_date='2016-06-21T03:02:00.776594Z' player='Barnacle' game='PvZ Garden Warfare 4'

http POST :8000/api/player-scores/ score=85125	score_date='2016-06-22T01:02:00.776594Z'	player='Barnacle' game='PvZ Garden Warfare 4'

http POST :8000/api/player-scores/ score=123200	score_date='2016-06-22T03:02:00.776594Z'	player='Kevin' game='Superman vs Aquaman'

http POST :8000/api/player-scores/ score=11200	score_date='2016-06-22T05:02:00.776594Z'	player='Kevin' game='PvZ Garden Warfare 4'

```
