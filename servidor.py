from flask import Flask, send_file, render_template, request
import sys, io, datetime, qrcode
from PIL import Image #, ImageDraw, ImageFont
from registros import registro
from flask import Flask
app = Flask(__name__)

<<<<<<< HEAD
app = Flask(__name__, static_url_path = "/Users/Vinny/Projects/Python/Redes1---2018.2", static_folder = "/Users/Vinny/Projects/Python/Redes1---2018.2")
=======
#@app.route("/")

hoje = datetime.datetime.now()
request = open("request.txt", "r")
cpf = request.readline()[15:-1]
password = request.readline()[15:-1]
>>>>>>> d0229107ca449e1ae334fed70e1c14551c09a0b1

@app.route("/foto/")
def foto3x4():
<<<<<<< HEAD
	return render_template("F"+dre+".png", mimetype='image/gif')

=======
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
>>>>>>> d0229107ca449e1ae334fed70e1c14551c09a0b1
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

<<<<<<< HEAD
def makeQRC(cpf):
        qrSize = 450
        qrc = qrcode.make(cpf)
        qrc = qrc.resize((qrSize,qrSize))
        qrc.save("fotos/QR"+cpf+".png","PNG")

@app.route('/', methods=['GET','POST'])
def home():
	return render_template("index.html")

#@app.route('/action_page.php?cpf=<cpf>&senha=<password>')#, methods=['GET','POST'])
@app.route('/documento', methods=['POST'])
def documento():
	cpf = request.form.get('cpf')
	password = request.form.get('senha')
	
	#print("CPF = "+str(cpf)+"\nSenha="+str(password)+"\n\n")

	if (password == registro[cpf][4]):
		nome=registro[cpf][0]
		curso=registro[cpf][1]
		dre=registro[cpf][2]
		nascimento=registro[cpf][3]
		expedicao = datetime.date.today().strftime('%d/%m/%Y')
		makeQRC(cpf)
		
		if (datetime.date.today().month>=7):
			periodo=str(datetime.date.today().year)+".2"
		else:
			periodo=str(datetime.date.today().year)+".1"
		
		return render_template("documento.html",nome=nome, dre=dre, curso=curso, cpf=cpf, nascimento=nascimento,periodo=periodo,expedicao=expedicao)
	else:
		return render_template("erro.html")

if __name__ == "__main__":
	app.run(debug=true, port=5000)
=======
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
>>>>>>> d0229107ca449e1ae334fed70e1c14551c09a0b1
