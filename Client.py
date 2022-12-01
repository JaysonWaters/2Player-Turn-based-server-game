import socket

#initilizes array for stats with default values. Thjis will be used to hold array of values sent by server.
stats = ('100','100','3','3')

#function to recieve data (64 bytes) from the server
def recvData1():
    msg1 = s.recv(2048)
    decoded = msg1.decode('ascii')

    #if the message from the server is q (Other player selected quit), close the connection and exit the game.)
    if decoded == "q":
        print("The other player has quit... Exiting the game.")
        s.close()
        exit()
    #if the other place didn't quit, seperate the message from the server by the spaces. return the array.
    stat = decoded.split()
    return stat


#function to send the decision of the player to the server.
def sendAction():
    while 1:
        action = input("Please Select an action:\n1: attack \n2: defend \n3: use potion\n4:Quit the game\n: ")
        if action == '1':
            s.send(action.encode('ascii'))
            break

        if action == '2':
            s.send(action.encode('ascii'))
            break

        if action == '3':
            #if we are either player 1 or player 2 and we have potions in our inventory, use it or repeat the loop and tell the player they are out of potions.
            if(player == 1 and int(stats[2]) > 0 or player == 2 and int(stats[3]) > 0):
                s.send(action.encode('ascii'))
                break

        if action == '4':
            s.send(action.encode('ascii'))
            s.close()
            print("Quitting the game...")
            exit()
            break
        else:
            print("\n\n\nYou are out of potions.\n\n")


def checkWinner(stats, player):
    pInfo = stats
    p = player
    if int(pInfo[0]) > 0 and int(pInfo[1]) > 0:
        return
    if p == 1:
        if int(pInfo[0]) <= 0:
            again = input("\n\n\nYour health has reached zero. you have lost. Enter 'q' to quit\n")
        else:
            again = input("You are victor. Enter 'q' to quit\n")
    if p == 2:
        if int(pInfo[1]) <= 0:
            again = input("\n\n\nYour health has reached zero. you have lost. Enter 'q' to quit\n")
        else:
            again = input("You are victor. Enter 'q' to quit\n")

    while 1:
        a = input()
        if a == 'q' or a == 'Q':
            print("Thank you for playing\n")
            exit()

#How the players' data is displayed to the players in their terminal
def showData():
    print("\n***************************\n" +
          "You are Player " + str(player) +
          "\n***************************\n"
          "player 1 Health: " + stats[0] +
          "\nPlayer 1 Potions: " + stats[2] +
          "\nPlayer 2 Health: " + stats[1] +
          "\nPlayer 2 Potions: " + stats[3] +
          "\n***************************\n"
          )


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))
msg = s.recv(2048)
print(msg.decode('ascii'))

#When the player 1 connects
if b'player 1' in msg:
    player = 1
    turn = 1
    print("You are player 1. Waiting for player 2 to connect....")
    msg = s.recv(2048)
    if msg.decode('ascii') == "p2connected":
        print("Player 2 is connected.")

#when player 2 connects
else:
    turn = 0
    player = 2
    print("You are player 2.")

showData() #Displays Health and potion data to the players that is stored on the server

#How the game is played using turns of the players
while 1:
    if turn == 1:
        sendAction()
        stats = recvData1()
        checkWinner(stats, player)
        showData()
        turn = 0

    else:
        print("Other player is deciding...\n")
        stats = recvData1()
        checkWinner(stats, player)
        showData()
        turn = 1
