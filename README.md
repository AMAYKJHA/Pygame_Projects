# Newton's Apple Game

**Newton's Apple** is an exciting 2D game built with Python and the Pygame library. The goal is to catch falling apples while avoiding dangerous thorns. As you progress, the game becomes faster and more challenging, and you have to manage your lives carefully. Can you keep up with the falling apples and avoid the thorns?

## Features
- **Catch Falling Apples:** Increase your score by catching apples that fall from the top of the screen.
- **Avoid Thorns:** Dodge the falling thorns. If you hit one, you lose a life.
- **Score System:** Keep track of your score as you catch apples and gain bonuses.
- **Multiple Lives:** Start with 3 lives, and lose one each time you hit a thorn.
- **Game Over:** When you run out of lives, the game ends.
- **Background Music & Sound Effects:** Enjoy dynamic sound effects for catching apples, losing lives, and game over.
- **Visuals:** Enjoy a colorful background, player, and various falling items like apples and thorns.


## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/AMAYKJHA/Pygame_Projects.git

Navigate to the project folder:

cd Newtons-Apple
Install Pygame using pip:

pip install pygame
Ensure you have the following media files in the project directory:

gameloop.mp3 (Background music)
bonus.wav (Bonus sound effect)
loose.wav (Damage sound effect)
game_over.wav (Game over sound effect)
background1.png (Upper background image)
background2.png (Lower background image)
player.png (Player character image)
apple.png (Apple image)
thorny.png (Thorn image)
stars.png (Star image)
heart.png (Heart image)

Run the game:
python main.py

# Controls
Left Arrow: Move the player left.
Right Arrow: Move the player right.
Space Bar: Start the game and trigger the falling of apples and thorns.

# Game Logic
Apple Falling: Apples fall from the top at a constant rate. The player needs to catch them to score points.
Thorns Falling: Thorns also fall from the top. If the player collides with a thorn, they lose a life.
Score System: The score increases each time an apple is caught. Every 9 apples increase the fall speed of both apples and thorns.
Life System: The player starts with 3 lives. Losing all lives ends the game.
Game Over: When the player runs out of lives, the game will display a "Game Over" message.
# How to Play
Start the game by pressing the Space Bar. Apples and thorns will begin falling from the top.
Use the Left Arrow and Right Arrow keys to move the player and try to catch the falling apples.
If you catch an apple, your score increases. Be careful not to hit the thorns!
Every time you hit a thorn, you lose one life. If you lose all your lives, the game will end.
Press Space Bar again to restart the game after it’s over.
# Contributing
Feel free to fork the repository and submit pull requests. If you find bugs or have ideas for improvements, please open an issue, and we'll discuss it!

To Contribute:
Fork this repository
Create a new branch for your feature or bug fix.
Commit your changes.
Push to the branch.
Submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.



