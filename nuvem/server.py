import socket
import json
import threading

HOST = "0.0.0.0"
PORT = 5000

def handle_client(conn):
    dados = conn.recv(1024).decode()
    requisicao = json.loads(dados)

    resposta = {
        "mensagem": "Ponto de recarga encontrado",
        "endereco": "Avenida X, 456"
    }

    conn.sendall(json.dumps(resposta).encode())
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print("Servidor rodando...")

        while True:
            conn, _ = server.accept()
            threading.Thread(target=handle_client, args=(conn,)).start()

if __name__ == "__main__":
    start_server()
