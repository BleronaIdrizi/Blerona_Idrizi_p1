import socket
import re
import argparse
import threading
import datetime
import random
from collections import Counter

parser = argparse.ArgumentParser(description ='Ky eshte serveri me multi threading sockets')
parser.add_argument('--host',metavar = 'host', type = str ,nargs="?",default=socket.gethostname())
parser.add_argument('--port',metavar = 'port', type = int ,nargs="?",default=13000)
args = parser.parse_args()

print(f'Serveri degjon ne HOST-in:{args.host} dhe PORT-in: {args.port}')

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
try:
    sck.bind((args.host,args.port))
except Exception as e:
        raise SystemExit(f'Nuk mund te lidheni me serverin ne host-in:{args.host} and portin {args.port} sepse {e}')

def on_new_client(client):
    while True:
        try:
            msg = client.decode().upper()
            lista = msg.split(" ")

            #prit veq te baj nihere veq nje metode 1 min

            if (lista[0] == 'TIME'):
                # 10.04.2020 11:00:00 PM
                x = datetime.datetime.now()			
                #print(str(x.strftime("%d.%m.%Y"))+ " "
                #+str(x.strftime('%X'))+" "+ str(x.strftime('%p')))
                time = str(x.strftime("%d.%m.%Y")) + " " + str(x.strftime('%X')) + " " + str(x.strftime('%p'))
                client.sendall(time.encode('utf-8'))

            elif (lista[0] == 'EXIT'):
                msg = "Ju e mbyllet komunikimin!"
                client.sendall(str(msg).encode('utf-8'))
                break

            else:
                raise  Exception("Ju nuk keni jepur asnje nga metodat e dhena.")
        except OSError:
             print('Klienti u diskonektua befasishem!!')
             break
        except Exception as e:
             dergoje = f"Ju nuk mundet te komunikoni me serverin, sepse {e}"
             client.sendall(str(dergoje).encode('utf-8'))
    print(f'Klienti me IP:{ip} dhe PORT:{port}, u diskonektua suksesshem.')
    client.close()

while True:
    try:
        on_new_client(sck.recvfrom(128))
    except KeyboardInterrupt:
        print(f'serveri u ndal me sukses!')
    except Exception as e:
        raise SystemExit(f'well I did not anticipate this: {e}')
sck.close()

