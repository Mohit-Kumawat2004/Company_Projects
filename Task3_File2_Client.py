import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  username = input("Enter your username: ")
  print(f"Connected to server as {username}")

  while True:
    message = input(f"{username}> ")
    s.sendall(f"{username}: {message}".encode())
    if message == "/quit":
      break

print("Disconnected from server")
