import socket
from _thread import *
import os
import sys
from Player import Player
import pickle
WIDTH, HEIGHT = 1400, 700
# WIN = pygame.display.set_mode((WIDTH,HEIGHT))


#COLORS:
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
#----------------------

#EVENTS:
#PLAYER DEFAULT STATE:
BULLET_WIDTH = 10
BULLET_HEIGTH = 20
BULLET_VEL = 10
BULLET_COLOR_P1 = WHITE
BULLET_COLOR_P2 = RED
BULLET_MODE_P1 = "-y"
BULLET_MODE_P2 = "+y"
P1_INIIAL_X = 500
P1_INITIAL_Y = 500
P2_INIIAL_X = 500
P2_INITIAL_Y = 100


#BORDER CONSTANTS:
BORDER_WIDTH = WIDTH
BORDER_HEIGHT = 30
BORDER_X = 0
BORDER_Y = HEIGHT//2 + BORDER_HEIGHT//2

#SPACESHIP = pygame.transform.scale(pygame.image.load("Assets/spaceship.png"),(50,50))

#SETTINGS:
IS_LOCAL = False
DEBUG = False

FPS = 60









server = "192.168.0.136"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server,port))
except socket.error as e:
    str(e)



s.listen(2)
print("Server Started.")


players = [Player(P1_INIIAL_X,P1_INITIAL_Y,50,50,BULLET_WIDTH,BULLET_HEIGTH,BULLET_VEL,BULLET_COLOR_P1,BULLET_MODE_P1,os.path.join("Assets","spaceship2.2.png"),True,IS_LOCAL),Player(P2_INIIAL_X,P2_INITIAL_Y,50,50,BULLET_WIDTH,BULLET_HEIGTH,BULLET_VEL,BULLET_COLOR_P2,BULLET_MODE_P2,os.path.join("Assets","spaceship.png"),False,IS_LOCAL)]



def threaded_client(conn,player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:

                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", data)
                print("Sending: ", reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Connection lost.")
    conn.close()
        


currentPlayer = 0
while True:
    conn, addr = s.accept()    

    print("Connected to:", addr)

    start_new_thread(threaded_client,(conn,currentPlayer))
    currentPlayer += 1