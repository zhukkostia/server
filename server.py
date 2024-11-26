import socket
import threading
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI працює разом із TCP-сервером"}


def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8000))  
    server_socket.listen(5)
    print("TCP-сервер запущено")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Підключено: {client_address}")
       


threading.Thread(target=start_tcp_server, daemon=True).start()
