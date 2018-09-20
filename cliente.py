import sys, datetime, qrcode

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

def lerArquivo():
	f = open("resposta.txt","r")
	status = f.readline()
	if (status == "STATUS         0 OK\n"):
		nome = f.readline()
		curso = f.readline()
		cpf = f.readline()
		nascimento = f.readline()
		foto = f.readline()
		
		nome = nome[15:len(nome)-1]
		curso = curso[15:len(curso)-1]
		cpf = cpf[15:len(cpf)-1]
		nascimento = nascimento[15:len(nascimento)-1]
		foto = foto[15:len(foto)-1]
		
		# print (nome)
		# print (curso)
		# print (cpf)
		# print (nascimento)
		
		return [nome, curso, cpf, nascimento, foto]
	else:
		print("Erro de leitura do arquivo resposta.txt")


def gerarDocumento():
        dre = sys.argv[1]
        makeQRC(dre)
                
        nome, curso, cpf, nascimento, foto = lerArquivo()

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


################


lerArquivo()
gerarDocumento()
