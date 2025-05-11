# mqttclient.py
import paho.mqtt.client as mqtt
import time
import json

# Configurações do broker (as mesmas do servidor)
broker_address = "broker_ba"
broker_port = 1884
client_id = "recarga_cliente"

# Tópico padrão para assinar (pode ser modificado conforme necessidade)
topico_reservas = "reserva/#"

def on_connect(client, userdata, flags, reason_code, properties):
    """Callback chamado quando o cliente se conecta ao broker."""
    if reason_code == 0:
        print(f"Conectado ao broker {broker_address}:{broker_port}")
        # Assina o tópico ao conectar
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

def main():
    # Inicializa o cliente MQTT
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id, protocol=mqtt.MQTTv311)
    
    # Configura os callbacks
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Conecta ao broker
    client.connect(broker_address, broker_port, 60)
    
    # Inicia o loop para processar mensagens
    client.loop_start()
    
    try:
        print("Cliente MQTT iniciado. Pressione CTRL+C para sair.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDesconectando do broker...")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()