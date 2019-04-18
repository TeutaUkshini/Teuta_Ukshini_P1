from socket import *
import sys
from _thread import *
import datetime
import random
import os
host='localhost'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

try :
    serverSocket.bind(('',serverPort))
except IOError:
    print("Klienti nuk mund te lidhet!")
    sys.exit()


print ('Serveri u startua ne localhostin:'+str(serverPort))
serverSocket.listen(10)
print('Serveri eshte i gatshem te pranoj kerkese')

def faktoriel(n):
    a=1
    while int(n)>=1:
        a=a*int(n)
        n=int(n)-1
    return a

def FIBONACCI(number):
     x=1
     y=1
     for z in range(2,number):
            fibonacci = x + y;
            x = y;
            y = fibonacci;
     return fibonacci


def IPADRESA():
    return gethostbyname(gethostname())

def BASHTINGELLORE(x):
    bashtingellore = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z']
    y=0
    for shkronja in x:
        if(shkronja in bashtingellore ):
            y=y+1
    return y

def EMRIIKOMPJUTERIT(): 
    return gethostname()

def KOHA():
    kh=datetime.datetime.now()
    kh = kh.strftime('%H:%M:%S')
    return kh

def LOJA():
    n = random.sample(range(0,49),7)
    
    numrin = str(n)
    return numrin

def KONVERTIMI(emri, numri):
     if emri=="KilowattToHorsepower":
        rez = numri*1.341 

     elif emri=="HorsepowerToKilowatt":
        rez = numri/1.341 

     elif emri=="DegreesToRadians":
        rez = numri*pi/180

     elif emri=="RadiansToDegrees":
        rez = numri*180/pi 

     elif emri=="GallonsToLiters":
        rez = numri*3.785 
     
     elif emri=="LitersToGallons":
        rez = numri/3.785 
     else:

        rez = "Gabim"
     return rez


def clientthread(connectionSocket):
    while True:
        try:
            zgjedhja = connectionSocket.recv(128).decode('utf-8')
            if not zgjedhja:
                break;
        except IOError:
            print('Ka problem!')
            break

        komanda = str(zgjedhja)

        if komanda == 'NUMRIPORTIT':
            connectionSocket.send(str(serverPort).encode('utf-8'))
        elif komanda == 'PRINTIMI':
            kerkesa = connectionSocket.recv(128)
            connectionSocket.send(kerkesa)
        elif komanda== 'FAKTORIEL':
            print('Numri i dhene eshte:'+str(numri))
            numri = connectionSocket.recv(128).decode('utf-8')
            connectionSocket.send(str(faktoriel(numri)).encode('utf-8'))
        elif komanda =='EMRIIKOMPJUTERIT':
            connectionSocket.send(str(EMRIIKOMPJUTERIT()).encode('utf-8'))
        elif komanda =='IPADRESA':
            connectionSocket.send(str(IPADRESA()).encode('utf-8'))
        elif komanda == 'BASHTINGELLORE':
            fjalia = connectionSocket.recv(128).decode('utf-8')
            print('Fjalia e dhene eshte: "'+fjalia+'"')
            connectionSocket.send(str(BASHTINGELLORE(fjalia)).encode('utf-8'))
        elif komanda =='KOHA':
            connectionSocket.send((KOHA().encode('utf-8'))) 
        elif komanda =='LOJA':
            connectionSocket.send((LOJA().encode('utf-8')))
        elif komanda =='FIBONACCI':
            numri=connectionSocket.recv(128).decode('utf-8')
            print('Numri i dhene eshte: '+numri)
            nr=int(numri)
            connectionSocket.send(str(FIBONACCI(nr)).encode('utf-8'))
        elif komanda =='KONVERTIMI':
            emri = connectionSocket.recv(128).decode('utf-8')
            numri = connectionSocket.recv(128).decode('utf-8')
            nr=int (numri)
            print('Klienti ka zgjedhur te konvertoj' + str(emri))
            connectionSocket.send(str(KONVERTIMI(emri, nr)).encode('utf-8'))
    connectionSocket.close()

while 1:
    connection, address=serverSocket.accept()
    print("Serveri eshte i lidhur ne:"+str(address))
    start_new_thread(clientthread,(connection,))

serverSocket.close()

