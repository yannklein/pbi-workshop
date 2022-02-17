# Programming Basics - Livecode

We will code a **Rock Scissors Paper** game.

Hints:

```python
name = input("What's your name?")

import random
random.choice([ "a", "b", "c" ])
```

<details><summary markdown='span'>View solution
</summary>

```python
import random

HANDS = ["ROCK", "SCISSORS", "PAPER"]
MAX_SCORE = 3

player_score = 0
computer_score = 0

while player_score < MAX_SCORE and computer_score < MAX_SCORE:
    print(f"Possible hands: {', '.join(HANDS)}")
    player_hand = input("What do you choose?\n> ")
    if player_hand not in HANDS:
        print("Wrong input. Please try again")
        continue

    computer_hand = random.choice(HANDS)
    print(f"Computer played {computer_hand}")

    if player_hand == computer_hand:
        print("Draw!")
    elif (player_hand == "ROCK" and computer_hand == "SCISSORS") or \
        (player_hand == "PAPER" and computer_hand == "ROCK") or \
        (player_hand == "SCISSORS" and computer_hand == "PAPER"):
        player_score += 1
        print("You win this one")
    else:
        computer_score += 1
        print("You lose this one")

    print(f"Player score: {player_score} - Computer score: {computer_score}")

if player_score > computer_score:
    print("You won! :-)")
else:
    print("Sorry, computer won :-(")
```

</details>

Check out the [screencast](https://vimeo.com/393470211/23b5e8e25b) of this livecode recorded on Feb 24th, 2020 in Malmö by @ssaunier
