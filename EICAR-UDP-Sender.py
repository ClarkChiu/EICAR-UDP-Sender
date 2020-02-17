import socket
from argparse import ArgumentParser

cmd_parser = ArgumentParser(
    prog='EICAR-UDP-Sender', description='EICAR UDP Sender'
)

cmd_parser.add_argument(
    '-ip', help='IP address', required=True
)

cmd_parser.add_argument(
    '-port', help='Port number', required=True
)

cmd_args = cmd_parser.parse_args()
ip = cmd_args.ip
port = int(cmd_args.port)
eicar_str = \
    'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(eicar_str.encode(), (ip, port))
sock.close()
