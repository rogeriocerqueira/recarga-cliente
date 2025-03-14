import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

def solicitar_ponto_de_recarga(nivel_bateria, localizacao):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        dados = {"bateria": nivel_bateria, "localizacao": localizacao}
        s.sendall(json.dumps(dados).encode())

        resposta = s.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")

if __name__ == "__main__":
    solicitar_ponto_de_recarga(15, "Rua A, 123")
