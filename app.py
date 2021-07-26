from flask import Flask, request, render_template, redirect, jsonify
import os
import socket

app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

@app.route("/")
def primeiro():
    return "oi"

@app.route("/func", methods=["GET"])
def dois():
    meu_nome = socket.gethostname()
    meu_ip = socket.gethostbyname(meu_nome)
    public_ip = request.environ['HTTP_X_FORWARDED_FOR']
    return jsonify({'ip': request.remote_addr,
            'teste-ip': request.environ['REMOTE_ADDR'],
            'teste_remote_user':request.remote_user,
            'meu_nome': meu_nome,
            'meu_ip': meu_ip,
            'HTTP X FOWRWARD': request.environ['HTTP_X_FORWARDED_FOR']}),200

@app.route("/pegar", methods=["GET"])
@app.route("/pegar")
def index():
    meu_nome = socket.gethostname()
    meu_ip = socket.gethostbyname(meu_nome)
    public_ip = request.environ['HTTP_X_FORWARDED_FOR']


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to the server 
    SERVER = public_ip
    PORT = 5050

    s.connect((SERVER,PORT))
    print("Aguardando ---- CLIENTE em processo")
    s_msg = s.recv(1024)
    print(f"Mensagem do SERVIDOR: {s_msg.decode()}")
    c_msg = input("Envie uma mensagem para o servidor ---")
    s.send(c_msg.encode('utf-8'))    

    return jsonify({'ip': request.remote_addr,
            'teste-ip': request.environ['REMOTE_ADDR'],
            'teste_remote_user':request.remote_user,
            'meu_nome': meu_nome,
            'meu_ip': meu_ip,
            'HTTP X FOWRWARD': request.environ['HTTP_X_FORWARDED_FOR']}),200
