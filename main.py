from flask import Flask, render_template, request, jsonify
import qrcode
from io import BytesIO
from base64 import b64encode
from werkzeug.utils import url_quote
import socket

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()
    data = request.form.get('link')
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)
    base64_img = 'data:image/png;base64,' + b64encode(memory.getvalue()).decode('ascii')

    return render_template('index.html', data=base64_img)


@app.route('/health', methods=['GET'])
def health():
    return jsonify(
        status="UP"
    )


@app.route('/fetchdetails', methods=['GET'])
def fetchdetails():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return render_template('details.html', hostname=hostname, ip=ip_address)
    except:
        return render_template('details.html', hostname='NULL', ip='NULL')


app.run(host="0.0.0.0", port=5000)
