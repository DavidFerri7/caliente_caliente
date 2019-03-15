import socket

puerto = 8080
ip = "10.0.2.15"
def chat(cliente):
    condicion = True
    while condicion:
        mensaje_cliente = input("Comienzo del chat")
        send_bytes = str.encode(mensaje_cliente)
        cliente.send(send_bytes)
        mensaje_servidor = cliente.recv(2048).decode("utf-8")
        print(mensaje_servidor)
try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ip, puerto))
    chat(cliente)
except OSError:
    print("Socket está usándose.")
cliente.close
