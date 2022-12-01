# 2Player-Turn-based-server-game

Kevin Stanley and Jayson Waters
Game Project Documentation 
csc 4350 Networking
11/23/20

How to Play:

The game is a two-player turn-based game.

To start the game each player will enter the commanded "python3 Client.py"

into their terminal,making sure that each player is in the correct directory.

Once each player is connected to the server they will be prompted with a screen
that looks similar to each player.

Player 1's terminal screen:

***************************
You are Player 1
***************************
player 1 Health: 100
Player 1 Potions: 3
Player 2 Health: 100
Player 2 Potions: 3
***************************

Please Select an action:
1: attack
2: defend
3: use potion
4:Quit the game


Player 2's terminal screen:

***************************
You are Player 2
***************************
player 1 Health: 100
Player 1 Potions: 3
Player 2 Health: 100
Player 2 Potions: 3
***************************

Other player is deciding...

While one player decides the other player is presented with the statement
"Other Player is deciding..." at the bottom of the terminal.

When it is the players turn they will be prompted with 4 action they could take:

1: attack -----------> base damage is 10 with with a critical hit chance that adds 0-8 damage to the attack

2: defend -----------> this action has a chance to negate all damage if successful but there is a chance that the defense will be unsuccessful

3: use potion -------> this will add 20 health points to the player (each player starts with 3)

4:Quit the game -----> this will end the game for both user if picked

Each player's screen will update after an action is chosen. Each players' health
and potion numbers will update each time a action is picked.

Once a player's health reaches 0 the game will end and to play another game
the player would have to enter "python3 Client.py" like they did at the beginging to 
start the game.
