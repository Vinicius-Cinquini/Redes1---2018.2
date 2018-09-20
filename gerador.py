import sys
import qrcode
import datetime
#import registros

def makeQRC(dre):
	qrSize = 450
	qrc = qrcode.make(dre)
	qrc = qrc.resize((qrSize,qrSize))
	qrc.save("QR"+dre+".png","PNG") 
	

hoje = datetime.datetime.now()

def periodoAtual():
	p = 0
	if (hoje.month >=6):
		p=2
	else:
		p=1
	return (str(hoje.year)+"."+str(p))

def mes(data):
	return ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"][data.month-1]

#def gerarDocumento(dre, nome, curso, cpf, nascimento, periodoAtual):
def gerarDocumento(dre, registro):
	nome = registro[dre][0]
	curso = registro[dre][1]
	cpf = registro[dre][2]
	nascimento = registro[dre][3]

	f = open("D"+dre+".html","w")
	f.write("<html><head><title>Documento de Registro do Estudante - "+dre+"</title></head>")
	f.write("<body bgcolor=#000>")
	f.write("<style> ")
	f.write("#fundo {")
	f.write("    background: #fff;")
	f.write("    color: #000;")
	f.write("    font-size: 12;")
	f.write("    border-radius: 25px;")
	f.write("    padding: 20px;")
	f.write("    width: 428px;")
	f.write("    height: 270px;")   
	f.write("    font-family: \"Verdana\", Verdana, sans-serif;")
	f.write("}")
	f.write("#nome {")
	f.write("    color: #000;")
	f.write("    font-size: 20;")
	f.write("}")
	f.write("")
	f.write("img.rounded-corners {")
	f.write("    border-radius: 25px;")
	f.write("    position: absolute;")
	f.write("    left: 320px;")
	f.write("    top: 80px;")
	f.write("    height: 180px;")
	f.write("}")
	f.write("")
	f.write("img.qrc {")
	f.write("    border-radius: 30px;")
	f.write("    position: absolute;")
	f.write("    left: 100px;")
	f.write("    top: 145px;")
	f.write("    height: 160px;")
	f.write("}")
	f.write("")
	f.write("</style>")
	f.write("<div id=\"fundo\">")
	f.write("<div id=\"nome\">"+nome+"</div>")
	f.write(curso+"<br>")
	f.write("Universidade Federal do Rio de Janeiro<br>")
	f.write("DRE: "+dre+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CPF: "+cpf+"<br>")
	f.write("Data de nascimento: "+nascimento+"<br>")
	f.write("Data de expedição: "+str(hoje.day)+" de "+mes(hoje)+" de "+str(hoje.year)+"<br>")
	f.write("Documento válido durante o período "+periodoAtual()+"<br>")
	f.write("<img src=\"F"+dre+".png\" class=\"wdn-stretch rounded-corners\">")
	f.write("<img src=\"QR"+dre+".png\" class=\"wdn-stretch qrc\">")
	f.write("</div>")
	f.write("</body></html>")
	f.write("")
	f.close()

######## REGISTROS #########
#Salvar em outro arquivo e importar?
registro = {
        "123456789" : [
                "Fulano de Tal com Sobrenome Comprido",
                "Engenharia de Computação e Informação",
                "000.111.222-33",
                "01/01/2001"
                ],

        "000000000" : [
                "Doctor Stephen Strange",
                "Artes Místicas Kamartajianas",
                "012.543.678-90",
                "10/07/1963"
                ],

	"000000001" : [
		"Luna Lovegood",
		"Magia e Bruxaria",
		"123.987.345-65",
		"13/02/1981"
		],

	"000000002" : [
		"Mordenkainen de Yatil",
		"Magia Vanciana e Economia de Slots",
		"135.246.753-02",
		"10/12/1972"
		],
	
	"000000003" : [
		"Robin \"Avatar\" Daraen",
		"Tática Mágica com Ênfase em Fogo e Trovão",
		"246.135.864-97",
		"13/02/1981"
		],

	"000000004" : [
		"Dorian Pavus",
		"Arcanática Tevinteriana",
		"192.168.000-01",
		"25/12/1982"
		]
}

######## EXECUTANDO ########

dre=sys.argv[1]
makeQRC(dre)
gerarDocumento(dre, registro)

#gerarDocumento("123456789", "Fulano de Tal e Qual Júnior", "Capacitação Profissional em Telessaúde", "000.111.222-33", "01/01/2001", periodoAtual())

