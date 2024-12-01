import socket
import threading
import time

class Server:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.clients = {}
        self.lock = threading.Lock()

    def handle_client(self, conn, addr):
        conn.settimeout(20)
        self.clients[addr] = time.time()
        try:
            while True:
                data = conn.recv(1024).decode()
                if data.strip() == "PING":
                    self.clients[addr] = time.time()
                    conn.sendall(b"PONG\n")
                else:
                    break
        except socket.timeout:
            print(f"Client with {addr} time outed.")
        except Exception as e:
            print(f"Error with client {addr}: {e}")
        finally:
            with self.lock:
                if addr in self.clients:
                    del self.clients[addr]
            conn.close()
            print(f"Connection with {addr} closed.")

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"Server run on {self.host}:{self.port}")
            while True:
                conn, addr = server_socket.accept()
                print(f"Client connected: {addr}")
                threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

class Client:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            print("Connected to host.")
            try:
                while True:
                    client_socket.sendall(b"PING\n")
                    data = client_socket.recv(1024).decode()
                    print(f"Received from server: {data.strip()}")
                    time.sleep(5)
            except Exception as e:
                print(f"Client error: {e}")
            finally:
                print("Client disconnected.")

if __name__ == "__main__":
    choice = input("Choose mode (host/client): ").strip().lower()
    if choice == "host":
        server = Server()
        server.start()
    elif choice == "client":
        client = Client()
        client.start()
    else:
        print("What have you chosen from? Correct options are only host and client.")
