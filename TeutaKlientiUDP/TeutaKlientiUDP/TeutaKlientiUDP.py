from socket import *
import sys

host='localhost'
port=12000
klientSocket=socket(AF_INET, SOCK_DGRAM)
print('UNIVERSITETI I PRISHTINES')
print('HASAN PRISHTINA')
print('Fakulteti i Inxhinierise Elektrike dhe Kompjuterike')
print('Departamenti i Inxhinierise Kompjuterike')
print('Lenda:Rrjetat Kompjuterike')
print('FIEK-TCP klienti')
print('--------------------------------------------------------------------------------------------------------------------')
print('Opsionet:')
print('IPADRESA; NUMRIPORTIT; BASHTINGELLORE; PRINTIMI; EMRIIKOMPJUTERIT; KOHA; LOJA; FIBONACCI; KONVERTIMI; FAKTORIEL;{hapsire} Numri \nKONVERTIMI {hapsire} Opsioni {hapsire} vlera \nOpsionet:KilowattToHorsepower<-->HorsePowerToKilowatt\n\t DegreesToRadians<-->RadiansToDegrees\n\t GallonsToLiters<-->LitersToGallons  ')
print('--------------------------------------------------------------------------------------------------------------------')
kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    
address = (host,port)

while(kerkesa!='' and kerkesa!='1'):
    data=''
    if 'FAKTORIEL' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Faktorieli i numrit te dhene eshte: '+ str(data))
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'BASHTINGELLORE' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Numri i bashtingellore ne fjaline e dhene eshte :'+str(data))
        mesazhi=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'EMRIIKOMPJUTERIT' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), (host,port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Emri i kompjuterit te juaj eshte: '+ str(data))
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'FIBONACCI' in kerkesa:
        klientSocket.sendto(kerkesa.encode() , (host , port))
        data=klientSocket.recv(128).decode('utf-8')
        print('Fibonacci i numrit te dhene eshte: '+str(data))
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'IPADRESA' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print('IP ADRESA e juaj eshte: '+data)
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'NUMRIPORTIT' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print('Porti juaj eshte: '+str(data))
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'PRINTIMI' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print('Fjalia e dhene eshte:' +data)
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'KOHA' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print(data)
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'LOJA' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), address)
        data=klientSocket.recv(128).decode('utf-8')
        print('Numrat e gjeneruar jane: '+data)
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    elif 'KONVERTIMI' in kerkesa: 
        klientSocket.sendto(kerkesa.encode(), address)
        data=klientSocket.recv(128)
        print(data)
        kerkesa=input('Shkruani kerkesen tuaj ose shtypni 1 per shkeputje te lidhjes me serverin: ')
    else:
        print('Shtypni nje kerkese te rregullt! :')

klientSocket.close()
