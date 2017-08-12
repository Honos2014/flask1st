from flask import Flask
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/home/ender/Sync/scripts/pythonweb/cert.pem', '/home/ender/Sync/scripts/pythonweb/cert.pem')

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=5000, debug=True,ssl_context=context)
