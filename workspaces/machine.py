import configparser
import os
import socket
sh = os.system
config = configparser.ConfigParser()
config.read('config.conf')
host = str(config['DEFAULT']['host'])
port = str(config['DEFAULT']['port'])
dbfile = str(config['DEFAULT']['DBFILE'])


def logo():
    print("""
          ______          \ /
      .-'` .    `'-.    -= * =-
    .'  '    .---.  '.    / \ 
   /  '    .'     `'. \ 
  ;  '    /          \|
 :  '  _ ;            `
;  :  /(\ \ 
|  .       '.
|  ' /     --'
|  .   '.__\              MoonLight Lab
;  :       /
 ;  .     |            , By Mrx04programmer
  ;  .    \           /|
   \  .    '.       .'/
    '.  '  . `'---'`.'
      `'-..._____.-`
""")
# Main
def main():
    # Sentences
    ## Server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", int(port)))
        logo()
        print("Corriendo maquina en el puerto "+str(port))
        #sh("rm "+dbfile)
        s.listen()
        c, a = s.accept() # Accept All Requests
        with c:
            print("Conexión entrante")
            print(f"Desde : {a}")
            data = c.recv(1024)
            if not data:
                pass
            c.sendall(data)

if __name__ == "__main__":
    try:
        main()
        print("Corriendo maquina")
    except Exception as e:
        print(":( Error of "+e)