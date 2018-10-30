from flask import Flask, send_file, render_template, request
import sys, io, datetime, qrcode
from pathlib import Path
from PIL import Image #, ImageDraw, ImageFont
from registros import registro
from flask import Flask
app = Flask(__name__)

app = Flask(__name__, static_url_path = "/Users/Vinny/Projects/Python/Redes1---2018.2", static_folder = "/Users/Vinny/Projects/Python/Redes1---2018.2")

status=['CPF inválido.',
	'Senha incorreta.',
	'Usuário sem foto; favor dirigir-se à secretaria.',
	'Matrícula inativa.'
]

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
	erro = -1
	verbose=True

	if cpf=='' or cpf not in registro:
		erro=0
		if verbose:
			print("CPF em branco ou não existe no banco")
		return render_template("erro.html",explicacao=status[erro])

	if password == registro[cpf][4]:
		if verbose:
			print("Senha correta")
		foto=Path("fotos/F"+cpf+".png")
		if foto.is_file():
			if verbose:
				print("Foto ok")
			if registro[cpf][5]==1:	#matrícula ativa
				if verbose:
					print("Matrícula ativa")
				nome=registro[cpf][0]
				curso=registro[cpf][1]
				dre=registro[cpf][2]
				nascimento=registro[cpf][3]
				expedicao = datetime.date.today().strftime('%d/%m/%Y')
				makeQRC(cpf)
				
				if datetime.date.today().month>=7:
					periodo=str(datetime.date.today().year)+".2"
				else:
					periodo=str(datetime.date.today().year)+".1"
				
				return render_template("documento.html",nome=nome, dre=dre, curso=curso, cpf=cpf, nascimento=nascimento,periodo=periodo,expedicao=expedicao)
			elif registro[cpf][5]==0:
				if verbose:
					print("Matrícula inativa")
				erro=3
		else:
			if verbose:
				print("Foto não encontrada")
			erro=2
	else:
		if verbose:
			print("Senha incorreta")
		erro=1

	if verbose:
		print("Renderizando página de erro...")
	return render_template("erro.html",explicacao=status[erro])

if __name__ == "__main__":
	app.run(debug=true, port=5000)
