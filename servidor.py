from flask import Flask, send_file, render_template, request
import sys, io, datetime, qrcode
from PIL import Image #, ImageDraw, ImageFont
from registros import registro
from flask import Flask
app = Flask(__name__)

app = Flask(__name__, static_url_path = "/Users/Vinny/Projects/Python/Redes1---2018.2", static_folder = "/Users/Vinny/Projects/Python/Redes1---2018.2")

@app.route("/foto/")
def foto3x4():
	return render_template("F"+dre+".png", mimetype='image/gif')
	
	foto = Image.open("F"+cpf+".png")
	byteArray = io.BytesIO()
	foto.save(byteArray, format="PNG")
	byteArray = byteArray.getvalue()
	return byteArray


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

def makeQRC(cpf):
        qrSize = 450
        qrc = qrcode.make(cpf)
        qrc = qrc.resize((qrSize,qrSize))
        qrc.save("fotos/QR"+cpf+".png","PNG")

@app.route('/', methods=['GET','POST'])
def home():
	return render_template("index.html")

@app.route('/documento', methods=['POST'])
def documento():
	cpf = request.form.get('cpf')
	password = request.form.get('senha')
	
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

if __name__ == "__main__":
	app.run(debug=true, port=5000)
