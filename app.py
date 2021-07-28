from flask import Flask, request, jsonify, send_file
from starlette.responses import FileResponse

import socket
import os
import tqdm

app = Flask(__name__)
port = int(os.environ.get("PORT",5000))

@app.route("/")
def primeiro():
    return "oi"

@app.route("/func", methods=["GET"])
def dois():
    meu_nome = socket.gethostname()
    meu_ip = socket.gethostbyname(meu_nome)
    #public_ip = request.environ['HTTP_X_FORWARDED_FOR']
    return jsonify({'ip': request.remote_addr,
            'teste-ip': request.environ['REMOTE_ADDR'],
            'teste_remote_user':request.remote_user,
            'meu_nome': meu_nome,
            'meu_ip': meu_ip})

@app.route("/pegar", methods=["POST"])
@app.route("/pegar", methods=["GET"])
def index():
    meu_nome = socket.gethostname()
    meu_ip = socket.gethostbyname(meu_nome)
    #public_ip = request.environ['HTTP_X_FORWARDED_FOR']
    #print(f"PUBLIC IP - > {public_ip}")
    
    

    BUFFER_SIZE = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    SERVER = '72.14.176.154'
    PORT = 5049

    SEPARATOR = "<SEPARATOR>"

    #CONEXAO

    s.connect((SERVER,PORT))
    print("CONEXÂO Estabelecida com sucesso!")

    received = s.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    progress = tqdm.tqdm(range(filesize), f"Recebendo - {filename}", unit="B", unit_scale=True, unit_divisor=1024)



    ''' with open(filename, "wb") as f:
        # read the bytes from the file
        #while True:
        bytes_read = s.recv(BUFFER_SIZE)
        #  if not bytes_read:
        #     break
        f.write(bytes_read)
        progress.update(len(bytes_read))        '''

    with open(filename, 'wb') as file:
        bytes_read = s.recv(BUFFER_SIZE)

        file.write(bytes_read)
        response = send_file(
            filename_or_fp=filename,
            mimetype="text/plain",
            as_attachment=True,
            attachment_filename=filename
        )
        s.close()
        return response
    py_file = "testando.txt"
    
    #return {"ok?":filename,
    #"teste":FileResponse(path=py_file, media_type='text/plain', filename=py_file)}
    #return {'feito?':'sim',
        #"arquivo:": filename}
    


if __name__ == '__main__':
    app.run(debug=True)