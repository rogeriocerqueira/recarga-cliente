# mqttclient.py
import paho.mqtt.client as mqtt
import time
import json

# Configurações do broker
broker_address = "broker_ba"
broker_port = 1883
client_id = "recarga_cliente"

# Tópicos
topico_reservas = "reserva/#"
topico_solicitacao_recarga = "solicitacao/recarga"

# Dados de teste (substitua pelo conteúdo do seu arquivo dados_teste.txt se preferir)
dados_testes = [
    {"cliente": "João Silva", "posto": "BA", "origem": "MA", "destino": "SE", "timestamp": 1620000000.1},
    {"cliente": "Maria Oliveira", "posto": "MA", "origem": "SE", "destino": "BA", "timestamp": 1620000000.2},
    {"cliente": "Carlos Souza", "posto": "SE", "origem": "BA", "destino": "MA", "timestamp": 1620000000.3},
    {"cliente": "Ana Costa", "posto": "MA", "origem": "BA", "destino": "SE", "timestamp": 1620000000.4},
    {"cliente": "Pedro Santos", "posto": "BA", "origem": "SE", "destino": "MA", "timestamp": 1620000000.5},
    {"cliente": "Lucia Lima", "posto": "MA", "origem": "SE", "destino": "BA", "timestamp": 1620000000.6},
    {"cliente": "Fernando Alves", "posto": "SE", "origem": "MA", "destino": "BA", "timestamp": 1620000000.7},
    {"cliente": "Juliana Pereira", "posto": "MA", "origem": "BA", "destino": "SE", "timestamp": 1620000000.8},
    {"cliente": "Roberto Gomes", "posto": "BA", "origem": "MA", "destino": "SE", "timestamp": 1620000000.9},
    {"cliente": "Patricia Rocha", "posto": "MA", "origem": "SE", "destino": "BA", "timestamp": 1620000001.0}
]

def on_connect(client, userdata, flags, reason_code, properties):
    """Callback chamado quando o cliente se conecta ao broker."""
    if reason_code == 0:
        print(f"Conectado ao broker {broker_address}:{broker_port}")
        client.subscribe(topico_reservas)
        print(f"Assinando tópico: {topico_reservas}")
    else:
        print(f"Falha na conexão. Código: {reason_code}")

def on_message(client, userdata, message):
    """Callback chamado quando uma mensagem é recebida."""
    payload = message.payload.decode("utf-8")
    print(f"\nNova mensagem recebida:")
    print(f"Tópico: {message.topic}")
    print(f"Payload: {payload}\n")

def solicitar_recarga(client, cliente_nome, posto, origem, destino):
    """Publica uma mensagem solicitando recarga para uma viagem entre estados."""
    payload = {
        "cliente": cliente_nome,
        "posto": posto,
        "origem": origem,
        "destino": destino,
        "timestamp": time.time()
    }
    mensagem = json.dumps(payload)
    client.publish(topico_solicitacao_recarga, mensagem)
    print(f"Solicitação de recarga publicada: {mensagem}")

def main():
    # Inicializa o cliente MQTT
    client = mqtt.Client(client_id=client_id, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    
    # Configura os callbacks
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Conecta ao broker
    client.connect(broker_address, broker_port, 60)
    
    # Inicia o loop para processar mensagens
    client.loop_start()
    
    try:
        print("Cliente MQTT iniciado. Enviando solicitações de teste...")
        
        # Envia todos os dados de teste automaticamente
        for dado in dados_testes:
            solicitar_recarga(client, dado["cliente"], dado["posto"], dado["origem"], dado["destino"])
            time.sleep(1)  # Intervalo entre publicações
            
        print("Todas as solicitações foram enviadas. Pressione CTRL+C para sair.")
        while True:
            time.sleep(1)  # Mantém o cliente ativo para receber mensagens
            
    except KeyboardInterrupt:
        print("\nDesconectando do broker...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()