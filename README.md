# Python Tic-Tac-Toe
## Basic (game.py)
A slightly modified python version of:
[Rogue.rb Tic-Tac-Toe](https://github.com/roguerb/tic-tac-toe)

## Evolved (egame.py)
My own, "evolved" Python version of Tic-Tac-Toe.
Intended to be a more evolved version of the OffensiveAI.

Board dimensions can be changed, so "3 in-a-row" can now be "10 in-a-row".
    - Default size is 3, which makes a 3x3 board.
    - Board sizes will always be proportionate.

```python
#egame.py

board = Board(players, dimension=3)
```

Players can be swapped to any of the following:

1. Player() is a Human Player
2. RandomAI() aka "dumb AI", makes random decisions.
3. OffensiveAI() will go for blocks and wins, but still makes random decisions
4. EvolvedAI() inherits OffensiveAI abilities, but doesnt make random decisions

```python
#egame.py

players = [Player('x'), EvolvedAI('o')]
```
	
## Prerequisites
- Python 3

## To Play
1. Open a command-line or terminal window.
2. `cd` into the project directory
3. Type the following in the root project directory:
    - `python game.py` for Basic Board and AI.
    or
    - `python egame.py` for Evolved Board and AI

## Game Instructions

You will be prompted with a console "game board". That looks similar to this:

```
---------- 

  |  |  
  |  |  
  |  |  

---------- 
 
Available Moves: [1,2,3,4,5,6,7,8,9]
x > 
```

You place your move by typing a number and pressing enter.
If you enter a spot that has already been taken you will be re-prompted.

The numbers match up to the board  in this order.

```
---------- 

 1 | 2 | 3 
 4 | 5 | 6 
 7 | 8 | 9 

---------- 

```
