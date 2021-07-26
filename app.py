from flask import Flask, request, render_template, redirect, jsonify
import os
import socket

app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

@app.route("/", methods=["GET"])
@app.route("/")
def index():
    meu_nome = socket.gethostname()
    meu_ip = socket.gethostbyname(meu_nome)
    return jsonify({'ip': request.remote_addr,
                'teste-ip': request.environ['REMOTE_ADDR'],
                'teste_remote_user':request.remote_user,
                'meu_nome': meu_nome,
                'meu_ip': meu_ip,
                'HTTP X FOWRWARD': request.environ['HTTP_X_FORWARDED_FOR']}),200

