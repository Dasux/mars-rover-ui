import socket
import threading
import json
from queue import Queue
import signal
import sys

class Server:
    def __init__(self, host="0.0.0.0", port=9090):
        self.host = host
        self.port = port
        self.clients = []
        self.telemetry_queue = Queue()
        self.server = None

    def handle_client(self, conn, addr):
        """Handle incoming client connections."""
        print(f"[NEW CONNECTION] {addr} connected.")
        self.clients.append(conn)
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                try:
                    telemetry = data.decode().strip()
                    self.telemetry_queue.put(telemetry)
                    print(f"[Telemetry] {telemetry}")
                except Exception as e:
                    print(f"[Decode Error] {e}")
        except Exception as e:
            print(f"[Connection Error] {e}")
        finally:
            conn.close()
            self.clients.remove(conn)
            print(f"[DISCONNECTED] {addr} disconnected.")

    def send_command(self, command_dict):
        """Send a command to all connected clients."""
        message = json.dumps(command_dict) + "\n"
        for client in self.clients:
            try:
                client.sendall(message.encode())
            except:
                continue

    def get_latest_telemetry(self):
        """Retrieve the latest telemetry data."""
        if not self.telemetry_queue.empty():
            return self.telemetry_queue.get()
        return None

    def stop_server(self, signum=None, frame=None):
        """Gracefully stop the server and close all connections."""
        if self.server:
            print("\n[SHUTTING DOWN] Server is shutting down.")
            for client in self.clients:
                client.close()
            self.server.close()
            sys.exit(0)

    def start_server(self):
        """Start the server and listen for incoming connections."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"[LISTENING] Server listening on {self.host}:{self.port}")

        # Register signal handler for graceful termination
        signal.signal(signal.SIGINT, self.stop_server)

        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    server = Server()
    server.start_server()

