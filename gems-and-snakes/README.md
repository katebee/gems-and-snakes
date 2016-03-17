## Gems and Snakes

It's the Monty Hall problem!

:snake: :snake: :gem:

Python version is currently the most complete. For the purpose of the game, we will assume that you want to receive gems, and that you hate snakes.

To run:
`$ python snakes_and_gems.py`
For now, you will also need stats.json to exist in the same directory.

To have the stats output at the end of the game, add a second argument:
`$ python snakes_and_gems.py stats`

Basic rules:

* There are three closed boxes, the exterior appearance is identical, however, the contents differ
* Two of the boxes contain snakes (boo!), only one contains gems (yay!)
* The player must pick a box
* The host will remove one of the boxes that was not picked by the player
* The host must always remove a box that contains snakes
* The host will offer the chance to switch between the originally chosen box and the remaining box.
