import socket

# 1. Setting prokontol komunikasi

# socket() params
# AF_INET buat ipv4
# AF_INET6 buat ipv6
# SOCK_STREAM buat TCP
# SOCK_DGRAM buat UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# 2. Alur server 
# bind() -> listen() -> accept()

# bind() params
# bind((HOST, PORT))
# dimana disesuaikan dengan
# host dan port yang dituju
s.bind((socket.gethostname(), 1698))

# listen() params
# listen()
s.listen()