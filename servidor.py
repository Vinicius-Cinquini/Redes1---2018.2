import sys, io, datetime, qrcode
from PIL import Image #, ImageDraw, ImageFont
from registros import registro
from flask import Flask
app = Flask(__name__)

#@app.route("/")

hoje = datetime.datetime.now()
request = open("request.txt", "r")
cpf = request.readline()[15:-1]
password = request.readline()[15:-1]

def foto3x4():
	foto = Image.open("F"+cpf+".png")
	byteArray = io.BytesIO()
	foto.save(byteArray, format="PNG")
	byteArray = byteArray.getvalue()
	return byteArray


"""def montarMensagem(registro):
        dre = sys.argv[1]
        mensagem =              "STATUS         0 OK\n"
        mensagem = mensagem +   "NOME           "+registro[dre][0]+"\n"
        mensagem = mensagem +   "CURSO          "+registro[dre][1]+"\n"
        mensagem = mensagem +   "CPF            "+registro[dre][2]+"\n"
        mensagem = mensagem +   "NASCIMENTO     "+registro[dre][3]+"\n"
        mensagem = mensagem +   "FOTO           "+str(foto3x4())+"\n\n"
        print (mensagem)
"""
def montarArquivo(registro):
        #dre = sys.argv[1]
        arq = open("resposta.txt","w+")
        arq.write("STATUS          0 OK\n")
        arq.write("NOME            "+registro[cpf][0]+"\n")
        arq.write("CURSO           "+registro[cpf][1]+"\n")
        arq.write("DRE             "+registro[cpf][2]+"\n")
        arq.write("NASCIMENTO      "+registro[cpf][3]+"\n")
        arq.write("FOTO            "+str(foto3x4()))
        arq.close()

def montarFalhaAut():
    arq = open("resposta.txt","w+")
    arq.write("STATUS          1 FALHA DE AUTENTICAÇÃO\n")
    arq.close()

def montarFalhaCPF():
    arq = open("resposta.txt","w+")
    arq.write("STATUS          1 FALHA DE AUTENTICAÇÃO\n")
    arq.close()

@app.route('/')
def main():
    if (not (cpf in registro)):
        montarFalhaCPF()
    elif (password == registro[cpf][4]):
        montarArquivo(registro)
    else:
        montarFalhaAut()

#montarMensagem(registro)
#montarArquivo(registro)

#main()
