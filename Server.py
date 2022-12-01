import socket
import random

class player:
    def __init__(self):
        self.port = ""
        self.address = ""
        self.turn = 0 #keeps track of which turn a player has
        self.health = 100 #health points for the player
        self.attack = 10 #base attack points
        self.defend = 10 #defend points
        self.potions = 3 #number of potions a player has
        self.isdef = 0 #sets if the player is able to block success fully


# decision making for Player 1
def recvData1():
    msg1 = player1.port.recv(2048)
    decision = msg1.decode('ascii')
	
	#Attack
    if decision == '1':
        if player2.isdef == 0:
            player2.health = player2.health - (player1.attack + random.randrange(0,9,1))#Adds critical damage from 0-8 to player 1's attack
        else:
            player2.isdef = 0
    
    #Defend
    elif decision == '2':
        player1.isdef = random.randrange(0,2,1)#random number 0-1 -> 1 is defend success and 0 is unsuccessful
    
    #Use Potion
    elif decision == '3':
        if player1.health <= 80:
            player1.health = player1.health + 20
        else:
            player1.health = 100
        player1.potions = player1.potions - 1
    
    #Quit Game
    elif decision == '4':
        msg3 = "q"
        player2.port.send(msg3.encode('ascii'))
        return


    msg3 = ""
    msg3 = str(player1.health) + " " + str(player2.health) + " " + str(player1.potions) + " " + str(player2.potions)
    player2.port.send(msg3.encode('ascii'))
    player1.port.send(msg3.encode('ascii'))

#Decision making for Player 2
def recvData2():
    msg1 = player2.port.recv(2048)
    decision = msg1.decode('ascii')
    
    #Attack
    if decision == '1':
        if player1.isdef == 0:
            player1.health = player1.health - (player2.attack + random.randrange(0,9,1))#Adds critical damage from 0-8 to player 2's attack
        else:
            player1.isdef = 0
    
    #Defend
    elif decision == '2':
        player2.isdef = random.randrange(0,2,1)#random number 0-1 -> 1 is defend success and 0 is unsuccessful
    
    #Use Potion
    elif decision == '3':
        if player2.health <= 80:
            player2.health = player2.health + 20
        else:
            player2.health = 100
        player2.potions = player2.potions - 1
    
    #Quit Game
    elif decision == '4':
        msg3 = "q"
        player2.port.send(msg3.encode('ascii'))
        return

    msg3 = ""
    msg3 = str(player1.health) + " " + str(player2.health) + " " + str(player1.potions) + " " + str(player2.potions)
    player1.port.send(msg3.encode('ascii'))
    player2.port.send(msg3.encode('ascii'))

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

#Port number for server to start listening on
port = 9999

# bind the hostname and port to the socket
serversocket.bind((host, port))

# queue up to 2 requests
serversocket.listen(2)

print("Server is listening...")

# establish a connection

player1 = player()
player2 = player()

print("Waiting for player 1 to connect...")

player1.port, player1.address = serversocket.accept()

print("Got a connection from %s" % str(player1.address))
print("Player 1: %s" % str(player1.address))

msg = 'You have connected successfully. You are player 1.' + "\r\n"
player1.port.send(msg.encode('ascii'))

player2.port, player2.address = serversocket.accept()

msg = "p2connected"
player1.port.send(msg.encode('ascii'))


print("Got a connection from %s" % str(player2.address))
print("Player 2: %s" % str(player2.address))

msg = 'You have connected successfully. You are player 2.' + "\r\n"
player2.port.send(msg.encode('ascii'))

if player1.port != "" and player2.port != "":
    print("Player 1 and player 2 are both connected! Lets start")
else:
    print("Something Went wrong... Please restart the server.")
    exit()


player1.turn = 1
player2.turn = 0

#Game runs only while both players health
while player1.health > 0 and player2.health > 0:
    if player1.turn == 1:
        recvData1()
        player1.turn = 0
        player2.turn = 1
    else:
        recvData2()
        player1.turn = 1
        player2.turn = 0


exit()

