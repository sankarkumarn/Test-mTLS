from flask import Flask, request
from OpenSSL import SSL

app = Flask(__name__)

# Specify the path to the server certificate and private key files
CERT_FILE = 'path/to/server_certificate.pem'
KEY_FILE = 'path/to/server_private_key.pem'

# Specify the path to the CA certificate file (optional, if client verification is required)
CA_CERT_FILE = 'path/to/ca_certificate.pem'

# Enable SSL/TLS context
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_certificate_file(CERT_FILE)
context.use_privatekey_file(KEY_FILE)

# Optional: Load the CA certificate for client verification
if CA_CERT_FILE:
    context.load_verify_locations(CA_CERT_FILE)
    context.verify_mode = SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT

# Route for the protected resource
@app.route('/protected', methods=['GET'])
def protected_resource():
    # Verify client certificate
    if request.environ.get('SSL_CLIENT_VERIFY') != 'SUCCESS':
        return 'Unauthorized', 401

    # Get client certificate
    client_cert = request.environ.get('SSL_CLIENT_CERT')

    # Process the client certificate
    # Add your authentication logic here

    return 'Authenticated', 200

if __name__ == '__main__':
    app.run(ssl_context=context, host='0.0.0.0', port=5000)
