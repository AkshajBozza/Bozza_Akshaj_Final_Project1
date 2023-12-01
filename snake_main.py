#This file was created by Akshaj Bozza

'''
Title: Snake Game

Goals: 
1) have the snake body move with the arrow keys and have the head switch direction when the arrow key is pressed (and then have the body follow)
2) have an apple that randomly generates after it collides with the snake
3) have the snake expand in length each time it consumes an apple
4) terminate the game when the snake either collides with itself or with the borders of the screen

MAYBE
1) adding power-ups such as a score multiplier or one that expands the size of the screen or one that increases/decreases the speed of the snake
2) adding some obstacles (maybe not feasible if the snake achieves a longer length) -- maybe one to reduce score without reducing length
3) sound-effects
4) letting the player customize the look of the snake before playing

'''

import socket
 
HOST = ""
PORT = 0
 
def decode_client_key(key):
    sprtr = key[0]
    tokens = key[1:len(key)-1].split(sprtr)
    port = int(tokens[0] + tokens[len(tokens)-1])
    tokens = tokens[1:len(tokens)-1]
    decoder = tokens[(len(tokens)-1)//2+1:]
    host_tokens = tokens[:(len(tokens)-1)//2+1]
    host = ".".join(host_tokens[int(index)] for index in decoder)
    return host, port
 
HOST, PORT = decode_client_key(input("Enter in room ID: "))
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ing = input("Enter in password: ")
    s.sendall(ing.encode())
    data = s.recv(1024)
    if data == b"1":
        raise ConnectionRefusedError
 
print(f"Successfully Connected! Data outputted: {data.decode()}")



