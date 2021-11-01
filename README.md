# Simple Maze Game

A reconstruction of my previous “Simple-Maze-Game” but created using Python and the Pygame module. Like the previous version, the game consists of three stages where the player controls the red square using the w-a-s-d keys and must get to the light green square without touching any of the dark green obstacles. If the player touches a dark green obstacle, they are sent back to the beginning to the stage. All three stages must be completed to win the game. The game also includes a main menu screen, instructions on how to play, and a pause screen.

![Alt Text](https://media.giphy.com/media/ex1M6QkNR3QQXapoKI/giphy.gif)

## How it works

The game uses the Pygame module (which could be downloaded here https://www.pygame.org/download.shtml) for the window creation and the multimedia components. The game is controlled by a “States” class which contains member functions that act as different states of the game. There is a game state, a main menu state, a pause state, and an instructions state. These states run their own game loop and which state is running depends on a member string variable which can be changed depending on which state we want to run. This member variable is then interpreted by the “state manager” member function and the member function that corresponds with that string value is called. On the main python file, once the “States” object is created, the “state manager” function member is called and placed inside a loop. 

![Alt Text](https://media.giphy.com/media/cE5UCasOyaaHa64s8Z/giphy.gif)

## Download

The .exe file is included in the repository, it is titled "Simple_Maze_Game.exe". You can either clone the repository and run the .exe or go to releases and download the setup.exe which downloads the repository files.
