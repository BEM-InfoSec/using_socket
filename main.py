# argparse kutuphanesini bu basit script uzerinde gercekleyiniz
# ornek argparse kullanimi github uzerinde mevcuttur : https://github.com/BEM-InfoSec/Using_args
# bu programin olmasi gereken ornek kullanimi: python3 using_socket -t 192.168.1.1 -p 80 

import socket

def connect_to_target(x, y):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((x, y))
        return True
    except:
        return False


if __name__ == '__main__':
    victim = ""
    port = 0

    if connect_to_target(victim, port):
        print(f'[+] Connection success: {victim}:{port}')
    else:
        print(f'[-] Connection failed: {victim}:{port}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
