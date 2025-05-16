import socket
import threading
import json
from queue import Queue
import signal
import sys

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 9090

clients = []
telemetry_queue = Queue()
server = None  # To store the server socket

# Callback to handle ESP32 connection
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            try:
                telemetry = data.decode().strip()
                telemetry_queue.put(telemetry)
                print(f"[Telemetry] {telemetry}")
            except Exception as e:
                print(f"[Decode Error] {e}")
    except Exception as e:
        print(f"[Connection Error] {e}")
    finally:
        conn.close()
        clients.remove(conn)
        print(f"[DISCONNECTED] {addr} disconnected.")

# Function to send commands to all connected ESP32s
def send_command(command_dict):
    message = json.dumps(command_dict) + "\n"
    for client in clients:
        try:
            client.sendall(message.encode())
        except:
            continue

# Gracefully stop the server and close connections
def stop_server(signum, frame):
    global server
    if server:
        print("\n[SHUTTING DOWN] Server is shutting down.")
        for client in clients:
            client.close()
        server.close()
        sys.exit(0)

# Start the server
def start_server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()

# For GUI to use telemetry data
def get_latest_telemetry():
    if not telemetry_queue.empty():
        return telemetry_queue.get()
    return None

# Register signal handler for graceful termination
signal.signal(signal.SIGINT, stop_server)  # Handle Ctrl+C (SIGINT)

if __name__ == "__main__":
    start_server()

