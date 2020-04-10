import socket
import re
import argparse
import threading
import datetime
import random
from collections import Counter

parser = argparse.ArgumentParser(description ='this is the server from multi threading sockets')
parser.add_argument('--host',metavar = 'host', type = str ,nargs="?",default=socket.gethostname())
parser.add_argument('--port',metavar = 'port', type = int ,nargs="?",default=13000)
args = parser.parse_args()

print(f'Running the server to host:{args.host} on port {args.port}')

sck= socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
 
try:
	sck.bind((args.host,args.port))
	sck.listen(5)
except Exception as e:
        raise SystemExit(f'Nuk mund te lidheni me serverin ne host-in:{args.host} and portin {args.port} sepse {e}')

def on_new_client(client,connection):

    ip=connection[0]
    port=connection[1]
    print(f'Konektimi u be nga IP-ja :{ip} dhe PORT-i:{port}') 
    
    while True:
        try:
            msg=client.recv(128)
            msg = msg.decode('utf-8').upper() 
            lista =msg.split(" ")

            if (lista[0]== 'IPADDRESS'):
                ipaddress = str(ip)
                client.sendall(('IPADDRESS-a e juaj eshte:'+str(ipaddress)).encode('utf-8'))
                #print('IP Adresa e klientit është: ' + str(ip))

            elif (lista[0]== 'NDRYSHO-IP'):
                ipaddress = lista[1]
                client.sendall(('IPADDRESS-a e juaj eshte:'+str(ipaddress)).encode('utf-8'))
                print(f'Konektimi u be nga IP-ja :{ipaddress} dhe PORT-i:{port}')

            elif (lista[0] == 'PORT'):
                port = str(port)
                client.sendall(('Ju jeni duke përdorur portin'+str(port)).encode('utf-8'))
                #print('Klienti është duke përdorur portin '+str(port))

            elif (lista[0] == 'NDRYSHO-PORT'):
                 port = lista[1]
                 client.sendall(('Ju jeni duke perdorur PORT-in:'+str(port)).encode('utf-8'))
                 print(f'Konektimi u be nga IP-ja :{ip} dhe PORT-i:{port}')

            elif (lista[0] == 'COUNT'):
                try:
                    teksti =""
                    for i in range(len(lista)):
                          if ( i != 0):
                             teksti += lista[i] + " " 
                    

                    zanoretCount=0
                    bashktinglloretCount=0
                    teksti = teksti.replace(" ","")

                    if teksti != "":
                        for i in teksti:                        
                            if(i.isalpha()):
                                    if(i=='a' or i=='e' or i=='ë' or i=='i' or i=='o' or i=='u' or i=='y' or i=='A'
                                    or i=='E' or i=='Ë' or i=='I' or i=='O' or i=='U' or i=='Y'):
                                        zanoretCount +=1  
                                    else:
                                        bashktinglloretCount +=1
                    else:
                         raise ValueError("Ju nuk keni jepur tekst.")

                    #print("Teksti i pranuar përmban "+ str(zanoretCount) +" zanore dhe "+str(bashktinglloretCount) + 'bashketingellore')
                    string = 'Teksti i pranuar përmban ' + str(zanoretCount) + ' zanore dhe ' +str(bashktinglloretCount) + ' bashketingellore'
                    client.sendall(string.encode('utf-8'))
               
                except ValueError as err:
                    msg = err.args[0]
                    client.sendall(str(msg).encode('utf-8'))
                    
            elif (lista[0] == 'REVERSE'):
                
                bashkimiFjaleve=""
                for i in range(len(lista)):
                    if ( i != 0):
                            bashkimiFjaleve += lista[i] + " " 

                if bashkimiFjaleve.replace(" ","") == "":
                    raise Exception("ju nuk e keni shkruar tekstin.")

                def my_function(x):
                    return x[::-1].strip()

                #print("Reverse :" + str(my_function(bashkimiFjaleve)))
                reverse= str(my_function(bashkimiFjaleve.strip()))
                client.sendall(reverse.encode('utf-8'))
                
            elif (lista[0] == 'PALINDROME'):

                def reverse(s): 
                    return s[::-1] 
                def isPalindrome(s): 
                    rev = reverse(s) 
                    if (s == rev): 
                        return True
                    return False

                if lista[1].replace(" ","") == "":
                    raise Exception("ju nuk e keni shkruar tekstin.")

                pergjigjja = isPalindrome(lista[1])
                if pergjigjja == 1: 
                    string = "Fjalia e dhene eshte palindrome." 
                else: 
                    string = "Fjalia e dhene nuk eshte palindrome."
                client.sendall(string.encode('utf-8'))

            elif (lista[0] == 'TIME'):
                # 10.04.2020 11:00:00 PM
                x=datetime.datetime.now()			
                #print(str(x.strftime("%d.%m.%Y"))+ " " +str(x.strftime('%X'))+" "+ str(x.strftime('%p')))
                time = str(x.strftime("%d.%m.%Y"))+ " " +str(x.strftime('%X'))+" "+ str(x.strftime('%p'))
                client.sendall(time.encode('utf-8'))

            elif (lista[0] == 'GAME'):
            
                def selection_sort(arr):        
                    for i in range(len(arr)):
                        minimum = i        
                        for j in range(i + 1, len(arr)):
                            if arr[j] < arr[minimum]:
                                minimum = j
                        arr[minimum], arr[i] = arr[i], arr[minimum]  
                    return arr
                
                i=0
                lista_random = []
                while (i<5):
                    n = random.randint(0,35)
                    if not n in lista_random:
                        lista_random.append(n)
                        i = i + 1         
                 
                #print(selection_sort(randomlist))
                game = selection_sort(lista_random)
                client.sendall((str(game)).encode('utf-8'))
            

            elif (lista[0] == 'GCF'):
                try:
                    k=int(lista[1])
                    l=int(lista[2])
                    def GCF(a,b): 
                        if(b==0): 
                           return a 
                        else: 
                           return int(GCF(b,a%b)) 

                   # print ("GCF: " + str(GCF(k,l))) 
                    gcf = str(GCF(k,l))
                    client.sendall(gcf.encode('utf-8'))
                except:
                    raise Exception("Ju nuk keni jepur numer.")

            elif (lista[0] == 'CONVERT'):
                    
                zgjedhja = lista[1]			

                #if lista[2] != int(lista[2]) :
                #    raise Exception("ju nuk keni jepur numer.")
                konvertimi = lista[2]
                try:
                    #konvertimi = int(konvertimii)
                    if (zgjedhja == 'CMTOFEET'):
                        #1 cm = (1/30.48) ft = 0.0328084 ft
                        #cmToFeet
                        feet=0.0328*int(konvertimi)
                        #print("Rezultati: " + str(round(feet,2)) + ' ft.')
                        rezultati = str(round(feet,2))
                        client.sendall(rezultati.encode('utf-8'))
                    elif  (zgjedhja == 'FEETTOCM'):
                        #1 ft = 30.48 cm
                        #FeetToCm
                        cmm=30.48*int(konvertimi)
                        #print("Rezultati: " + str(round(feet,2)) + ' cm.')
                        rezultati = str(round(feet,2))
                        client.sendall(rezultati.encode('utf-8'))
                    elif  (zgjedhja == 'KMTOMILES'):
                        #1 km = (1/1.609344) mi = 0.62137119 mi
                        #kmToMiles				
                        mile=0.62137119*int(konvertimi)
                        #print("Rezultati: " + str(round(mile,2)) + ' miles')
                        rezultati = str(round(mile,2))
                        client.sendall(rezultati.encode('utf-8'))
                    elif (zgjedhja == 'MILETOKMS'):				
                        #1 mi = 1.609344 km
                        #MileToKm			
                        kmm=1.609344*int(konvertimi)
                        #print("Rezultati: " + str(round(kmm,2)) + " km")
                        rezultati = str(round(kmm,2))
                        client.sendall(rezultati.encode('utf-8'))

                    else:
                        raise ValueError("Mundesit e zgjedhjes jane: cmToFeet, FeetToCm, kmToMiles, MileToKm")
                except ValueError as err:
                    msg = err.args[0] 
                    client.sendall(str(msg).encode('utf-8'))
        
            elif (lista[0] == 'NUMRAT'):
                      
                numrat=""
                for i in range(len(lista)):
                      if ( i != 0):
                          if(i == (len(lista)-1)):
                              numrat += lista[i]
                          else:
                              numrat += lista[i] + "," 
                if numrat.replace(" ","") == "":
                    raise Exception("duhet ti shenoni numrat per ti gjetur cift-et dhe tek-et.")
                 
                cift = 0
                tek=0
                rezultati = re.split(',', numrat)
                for i in range(len(rezultati)):
                    if (int(rezultati[i]) % 2) == 0:
                        cift = cift +1
                    else:
                       tek = tek + 1
            
                #print('Ju keni shkruar: ' +str(cift) + " numra qift dhe " +str(tek)+ ' numra tek')
                perfundimi = 'Ju keni shkruar: ' +str(cift) + " numra qift dhe " +str(tek)+ ' numra tek'
                client.sendall(perfundimi.encode('utf-8'))

            elif (lista[0] == 'FREKUENCA'):	

                teksti= ""
                for i in range(len(lista)): 
                    if ( i != 0):                     
                        teksti += lista[i] + " "
                teksti  = teksti.replace(" ","")

                if teksti == "":
                    raise Exception("ju nuk keni shkruar tekstin per ta gjetur frekuencen.")
                
                #print ("Frekuenca : ")              
                #for i,j in all_freq.items():
                     #print( str(i) + ":" + str(j))
                
                rezultati = Counter(teksti)
                client.sendall(str(rezultati).encode('utf-8'))

            elif ( lista[0] == 'EXIT'):
                msg = "Ju e mbyllet komunikimin!"
                client.sendall(str(msg).encode('utf-8'))
                break

            else:
                raise  Exception("Ju nuk keni jepur asnje nga metodat e dhena.")
        except OSError:
             print('Klienti u diskonektua befasishem!!')
             break
        except Exception as e:
             dergoje= f"Ju nuk mundet te komunikoni me serverin, sepse {e}"
             client.sendall(str(dergoje).encode('utf-8'))
        
    print(f'Klienti me IP:{ip} dhe PORT:{port}, u diskonektua suksesshem.')
    client.close()

while True:
    try:
        client,ip = sck.accept()
        threading._start_new_thread(on_new_client,(client,ip))
    except KeyboardInterrupt:
        print(f'serveri u ndal me sukses!')
    except Exception as e:
        raise SystemExit(f'well I did not anticipate this: {e}')
sck.close()

