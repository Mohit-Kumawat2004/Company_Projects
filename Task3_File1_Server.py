import socket
import threading

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

class Client(threading.Thread):
  """
  Represents a connected client to the chat server.
  """
  def _init_(self, sock, addr):
    super()._init_()
    self.sock = sock
    self.addr = addr

  def run(self):
    print(f"Connected by {self.addr}")
    while True:
      try:
        data = self.sock.recv(1024)
        if not data:
          break
        for client in clients:
          if client != self:
            client.send(data)  # Broadcast message to all connected clients (except sender)
      except:
        print(f"Client {self.addr} disconnected")
        break
    self.sock.close()
    clients.remove(self)

clients = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  print("Server listening on port", PORT)
  while True:
    conn, addr = s.accept()
    client = Client(conn, addr)
    clients.append(client)
    client.start()

# Wait for all threads to finish
for client in clients:
  client.join()

print("Server shutting down")
