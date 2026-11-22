# Projectile Game

A text-based Python game where you try to hit a target by choosing a launch angle and speed.

## What it does

5 rounds are played in the terminal. In each round, the computer picks a random target distance. You, the user, enter a launch angle (1-89 degrees) and a launch speed (1-60 m/s), and the program calculates where the ball lands using the standard projectile range formula:

'range = v^2 * sin(2 * theta) / g'

## How to run it

1. Make sure Python 3 is installed
2. Download 'Projectile Game.py'
3. In a terminal, go to the folder containing the file and run:
  ```
   python 'Projectile Game.py'
  ```
The only libraries needed are 'math' and 'random'.
## Example output
```
Round 1 of 5
Target distance: 99 m
Launch angle in degrees (1-89): 30
Launch speed in m/s (1-60): 20

Your ball landed 35.3 m away.
You fell short by 63.688057 m.
Points this round: 0
```

At the end of the game, you get a summary:
```
GAME SUMMARY:
Round    Target   Landed   Off by  Points
1            99     35.3     63.7       0
2            52     22.6     29.4      10
3            21     22.6      1.6     100
4            60     40.2     19.8      30
5            83    160.6     77.6       0

Total score: 140 / 500
Closest shot: round 3
(off by 1.6 m)
Rating: Keep practising!
```

## How the code is organised

Each part of the game is its own function:

- 'calculate_range()' works out where the ball lands
- 'get_number()' asks for a number and keeps asking until it's valid
- 'get_points()' and 'get_rating()' turn the results into a score and a message
- 'play_round()' runs a single round
- 'show_summary()' prints the results table
- 'main()' runs the whole game and tracks the high score

## What I learned

Writing this project helped me practise functions, loops, dictionaries and lists. What was new content, was the math library and the formation of a table that could be displayed. Although they were annoying to type out, they were quite self-explanatory and fun to use. More importantly, this project helped me test a user input carefully, as well as providing a suitable error message.

## Possible improvements

- Adding difficulty levels (altering the hit tolerance is one way?)
- Add extra variables (like wind) to change the landing distance
- Saving the high score to a file so that it transfers between sessions
