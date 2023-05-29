import tls
import socket

def main():
    # Create a TLS context and load the client certificate and key.
    context = tls.create_default_context()
    context.load_cert_chain("client.crt", "client.key")

    # Create a socket and connect to the server.
    sock = socket.socket()
    sock.connect("localhost", 443)

    # Wrap the socket in a TLS wrapper.
    tls_sock = tls.wrap_socket(sock, context=context)

    # Send a message to the server.
    tls_sock.sendall("Hello, world!")

    # Receive a message from the server.
    data = tls_sock.recv(1024)

    # Close the socket.
    tls_sock.close()

    # Print the message from the server.
    print(data)

if __name__ == "__main__":
    main()
