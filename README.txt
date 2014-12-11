This project and all of its content is developed by Swathi Shanmugasundaram 
(swathishanmugasundaram@gmail.com)

----------------------------------------------------------------------------------------------------------------------------------------
ABOUT: This project is about game logic and AI for 'Pallanguzhi', a board game.
The project is developed in Python 2.7

----------------------------------------------------------------------------------------------------------------------------------------
CONTENTS: The project contains two python modules: game.py and board.py.
The game module contains the game which uses a board object. 
The project utilizes a modified Min Max strategy for the AI part.

----------------------------------------------------------------------------------------------------------------------------------------
RUNNING THE PROGRAM: To run the program run the game.py

----------------------------------------------------------------------------------------------------------------------------------------
EXPECTED OUTPUT FORMAT: You can expect to see a output which prints,
The player names as Player 0, Player 1 respectively.
The choice of strategy for players by default (Player 0 chooses modified Min Max strategy, Player 1 chooses Naive strategy)
The initial board (14 pits and 5 coins in each pit by default)
The consecutive boards after each move
The final board.
The scores of the players 
The game winner

-----------------------------------------------------------------------------------------------------------------------------------------
INTERPRETING THE OUTPUT: As seen in the default program output, you can notice that Player 0 who chooses Min Max strategy wins.
Now my switching the player staregies, you can see that Player 1 wins over Player 0 instead.
Now the game can be repeated for different board sizes beginning from 2, 4, 6, 8, 10, 12, 14.
Notice that the board size has to be an even number. Otherwise the given number - 1 would be taken as the board size number.

-----------------------------------------------------------------------------------------------------------------------------------------
MODIFING THE PROGRAM: The game module can be modified before run inorder to switch player strategies or to change the board size.
To switch player strategies:
1. Scroll to the end of the game module program until you find Play() function.
2. Change the if current player is 0 condition to current player is 1 or vice versa.
3. Run the program.
To change the board size:
1. Scroll to the end of the game module.
2. You can see that we create a game object with two parameters.
3. Provide the board size as the first parameter. 
4. Run the program.

-----------------------------------------------------------------------------------------------------------------------------------------