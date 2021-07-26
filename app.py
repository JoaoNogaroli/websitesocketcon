from flask import Flask, request, render_template, redirect, jsonify
import os
app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

@app.route("/", methods=["GET"])
@app.route("/")
def index():
    return jsonify({'ip': request.remote_addr}),200

@app.route("/ip", methods=["GET"])
def func_ip():
    return jsonify({'teste-ip': request.environ['REMOTE_ADDR']}),200