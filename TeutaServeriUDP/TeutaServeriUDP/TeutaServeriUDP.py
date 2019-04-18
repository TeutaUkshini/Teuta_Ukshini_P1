from socket import * 
import sys 
from _thread import * 
import datetime
import random 
import os 

host = 'localhost'
port = 12000
serverSocket= socket(AF_INET , SOCK_DGRAM)

try: 
    serverSocket.bind((host,port))
except: 
    print('Nuk mund te lidheni!!!')
    sys.exit()

print('Serveri eshte startuar ne localhost '+str(port))
print('Serveri eshte i gatshem te pranoje kerkesa ')

def FAKTORIEL(n):
    a=1
    while int(n)>=1:
        a=a*int(n)
        n=int(n)-1
    return a

def BASHTINGELLORE(x):
    bashtingellore = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z']
    y=0
    for shkronja in x:
        if(shkronja in bashtingellore ):
            y=y+1
    return y
def FIBONACCI(number):
     x=1
     y=1
     for z in range(2,number):
            fibonacci = x + y
            x = y
            y = fibonacci
     return fibonacci

def IPADRESA():
    return gethostbyname(gethostname())
def EMRIIKOMPJUTERIT(): 
    return gethostname()

def KOHA():
    kh=datetime.datetime.now()
    kh = kh.strftime('%H:%M:%S')
    return kh

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

def LOJA():
    n = random.sample(range(0,49),7)
    
    numrin = str(n)
    return numrin

def clientthread (input , address):
    try:
        data = input.decode('utf-8')
    except IOError:
        print('Ka ndodhur nje gabim')
    komanda=str(data).rsplit(' ')
    fjalia=''
    i=len(komanda)
    for zgjedhja in range(1,i):
        fjalia=fjalia+komanda[zgjedhja]
        if(zgjedhja!=i):
            fjalia+=' '
    fund=str(fjalia)
    if komanda[0]=='FAKTORIEL':
        serverSocket.sendto(str(FAKTORIEL(komanda[1])).encode('utf-8') , address)
    elif komanda[0]=='BASHTINGELLORE':
        serverSocket.sendto(str(BASHTINGELLORE(fund)).encode('utf-8') , address)
    elif komanda[0]=='EMRIIKOMPJUTERIT':
        serverSocket.sendto(str(EMRIIKOMPJUTERIT()).encode('utf-8'), address)
    elif komanda[0]=='FIBONACCI':
        nr=int(komanda[1])
        serverSocket.sendto(str(FIBONACCI(nr)).encode('utf-8'),address)
    elif komanda[0]== 'IPADRESA':
        serverSocket.sendto(str(IPADRESA()).encode('utf-8') , address)
    elif komanda[0]=='NUMRIPORTIT':
        serverSocket.sendto(str(port).encode('utf-8') , address)
    elif komanda[0] == 'PRINTIMI':
        serverSocket.sendto(str(fund).encode('utf-8') , address)
    elif komanda[0]== 'KOHA':
        serverSocket.sendto(str(KOHA()).encode('utf-8') , address)
    elif komanda[0] == 'LOJA':
        serverSocket.sendto(str(LOJA()).encode('utf-8') , address)
    elif komanda[0] == 'KONVERTIMI':
        print('Klienti ka zgjedhur te konvertoj' + komanda[1])
        nr=int(komanda[2])
        serverSocket.sendto(str(KONVERTIMI(komanda[1], nr)).encode('utf-8'),address)
    else:
        serverSocket.sendto(str('ERROR!!!').encode('utf-8'))
while True:
    data , address=serverSocket.recvfrom(128)
    print('Serveri tani eshte lidh me ' + str(address))
    start_new_thread(clientthread , (data,address,))
serverSocket.close()

