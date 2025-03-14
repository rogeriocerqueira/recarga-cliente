import socket
import json

HOST = "127.0.0.1"
PORT = 6000

def ponto_recarga():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print("Ponto de recarga ativo...")

        while True:
            conn, _ = server.accept()
            dados = conn.recv(1024).decode()
            requisicao = json.loads(dados)

            if requisicao["acao"] == "reservar":
                resposta = {"status": "Reservado"}
            else:
                resposta = {"status": "Disponível"}

            conn.sendall(json.dumps(resposta).encode())
            conn.close()

if __name__ == "__main__":
    ponto_recarga()