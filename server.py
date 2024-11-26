import socket
import threading
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI працює разом із TCP-сервером"}


def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 10000))  
    server_socket.listen(5)
    print("TCP-сервер запущено на 127.0.0.1:65432")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Підключено: {client_address}")
        data = client_socket.recv(1024).decode()
        print(f"Отримано від {client_address}: {data}")
        client_socket.sendall(f"Привіт, {client_address}. Ви сказали: {data}".encode())
        client_socket.close()


threading.Thread(target=start_tcp_server, daemon=True).start()
