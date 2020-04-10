import socket
import argparse
#klienti

parser = argparse.ArgumentParser(description ='this is the client from threading sockets')
parser.add_argument('--host',metavar = 'host', type = str ,nargs="?",default=socket.gethostname())
parser.add_argument('--port',metavar = 'port', type = int ,nargs="?",default=13000)
args = parser.parse_args()
print('**********************************************************************************************************')
print('FIEK-TCP ')
print('KLIENTI')
print('Ju jeni lidhur me sukses me Serverin dhe mund te komunikoni.')
print('**********************************************************************************************************')

print(f'Konektimi u be ne serverin me HOST-in: {args.host} dhe PORT-in: {args.port}')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sck:    
    try:
        sck.connect((args.host,args.port))
    except Exception as e:
        raise SystemExit(f'we have faild to connect to host: {args.host} with the port :{args.port} because {e}')
    

    while True:
        msg=input('Operacioni (IPADDRESS, NDRYSHO-IP, PORT, NDRYSHO-PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, NUMRAT, FREKUENCA)?:')
        try:
            
            sck.sendall(msg.encode('utf-8'))
            
            data = sck.recv(128)
            print(f'Pergjigjja: {data.decode()}')          
           
        #ValueError
        except IndexError as error:
            print('\nSection: Function to Create Instances of WebDriver\nCulprit: random.choice(ua_strings)\nIndexError: {}\n'.format(error))
            continue
          


