import socket
import sys

serverName = 'localhost'
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName , 12000))
klientPort = 1111
print('Fiek Klienti:')
while True:
    print('UNIVERSITETI I PRISHTINES')
    print('HASAN PRISHTINA')
    print('Fakulteti i Inxhinierise Elektrike dhe Kompjuterike')
    print('Departamenti i Inxhinierise Kompjuterike')
    print('Lenda:Rrjetat Kompjuterike')
    print('FIEK-TCP klienti')
    print('--------------------------------------------------------------------------------------------------------------------')
    print('Opsionet:')
    print('IPADRESA; NUMRIPORTIT; BASHTINGELLORE; PRINTIMI; EMRIIKOMPJUTERIT; KOHA; LOJA; FIBONACCI; KONVERTIMI; FAKTORIELI;  ')
    print('--------------------------------------------------------------------------------------------------------------------')
    var=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    kerkesa= var.upper()

    if kerkesa=='NUMRIPORTIT':
        s.sendall(str.encode(kerkesa))
        emriportit= str(klientPort)
        s.sendall(str.encode(emriportit))
        data=s.recv(128).decode('utf-8')
        print('Porti juaj eshte: '+str(klientPort))
    elif kerkesa == 'PRINTIMI':
        s.sendall(str.encode(kerkesa))
        zgjedhja = input('Shkruani nje fjali:')
        s.sendall(str.encode(zgjedhja))
        data=s.recv(128).decode('utf-8')
        print('Fjalia e dhene eshte:' +data)
    elif kerkesa=='EMRIIKOMPJUTERIT':
        s.sendall(str.encode(kerkesa))
        data=s.recv(128).decode('utf-8')
        print('Emri juaj eshte: '+data)
    elif kerkesa== 'IPADRESA':
        s.sendall(str.encode(kerkesa))
        data=s.recv(128).decode('utf-8')
        print('IP ADRESA e juaj eshte: ' + data)
       
    elif kerkesa=='FAKTORIEL':
        s.sendall(str.encode(kerkesa))
        numri=input('Jepni numrin: ')
        s.sendall(str.encode(numri))
        data=s.recv(128).decode('utf-8')
        print('Faktorieli i '+ str(numri)+' eshte '+str(data))
    elif kerkesa=='BASHTINGELLORE':
        s.sendall(str.encode(kerkesa))
        Zgjedhja=input('Shtypni fjalin tuaj: ')
        s.sendall(str.encode(Zgjedhja))
        data=s.recv(128).decode('utf-8')
        print('Numri i bashtingelloreve ne fjaline e shtypur eshte: '+data)
    elif kerkesa == 'KOHA':
        s.sendall(str.encode(kerkesa))
        data=s.recv(128).decode('utf-8')
        print(data)   
    elif kerkesa =='LOJA':
        s.sendall(str.encode(kerkesa))
        data=s.recv(128).decode('utf-8')
        print('Numrat random te gjeneruar jane:'+data)
    elif kerkesa == 'FIBONACCI':
        s.sendall(str.encode(kerkesa)) 
        numri= input('Jepni nje numer')
        s.sendall(str.encode(numri))
        data=s.recv(128).decode('utf-8')
        print('Fibonacci i numrit te dhene eshte ' +data)
    elif kerkesa == 'KONVERTIMI': 
        s.sendall(str.encode(kerkesa))
        print('Ju mund te beni keto konvertime: \nKilowattToHorsepower \nHorsepowerToKilowatt \nDegreesToRadians \nRadiansToDegrees \nGallonsToLiters \nLitersToGallons')
        emri= input('Zgjedhni nje opsion: ')
        s.sendall(str.encode(emri))
        sasia = input('Jepni numrin qe doni te konvertoni')
        s.sendall(str.encode(sasia))
        data=s.recv(128).decode('utf-8')
        print('Madhesia e konvertuar: '+data)
    elif kerkesa=='1':
        break
    else:
        print('Komanda qe keni shtypur nuk eshte e rregullt!!')
    print()
s.close()



