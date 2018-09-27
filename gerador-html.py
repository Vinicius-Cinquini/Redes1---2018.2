import sys, io, datetime, qrcode
#import os.path
from os import path
from PIL import Image
from array import array

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

def lerResposta():
        f = open("resposta.txt","r")
        status = f.readline()
        if (status == "STATUS         0 OK\n"):
            nome = f.readline()[16:-1]
            curso = f.readline()[16:-1]
            dre = f.readline()[16:-1]
            nascimento = f.readline()[16:-1]
            foto = f.readline()[16:]
            cpf = lerRequest()
                # print (nome)
                # print (curso)
                # print (cpf)
                # print (nascimento)

            reconstruirFoto3x4() ####################################################
            gerarDocumento(dre, nome, curso, cpf, nascimento, foto)
                
                #return [nome, curso, cpf, nascimento, foto]

        elif (status[14] == "1"):
            print("Senha incorreta")
        elif (status[14] == "2"):
            print("Usuário não cadastrado")
        elif (status[14] == "3"):
            printf("Usuário inativo")
        elif (status[14] == "4"):
            prinft("Erro desconhecido; favor dirigir-se à secretaria.")
        else:
            print("Erro de leitura do arquivo resposta.txt")

def reconstruirFoto3x4():
	arq = open("resposta.txt","r")
	for i in range(0,6):
		byteString = arq.readline()[15:-1]
	#f3x4 = Image.frombytes("RGB", (850, 1134), byteString.encode('utf-8'),'raw')
	f3x4 = Image.frombytes("RGB", (850, 1134), byteString.encode('utf-16'),'raw')
	f3x4.save("FC"+dre+".png")
	

'''
	arq = open("resposta.txt", "r")
	for i in range(0,6):
		byteArray = arq.readline()[15:-1]
	#print(str(i)+" : "+byteArray)
	f = open("FC"+dre+".png","w+")
	f.write(byteArray)
	f.close()
	#image = Image.open(io.BytesIO(byteArray))
	#image.show()
'''


def gerarDocumento(dre, nome, curso, cpf, nascimento, foto):
        makeQRC(dre)
        #nome, curso, cpf, nascimento, foto = lerResposta()

        f = open("D"+cpf+".html","w")
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
        f.write("<img src=\"F"+cpf+".png\" class=\"wdn-stretch rounded-corners\">")
        f.write("<img src=\"QR"+dre+".png\" class=\"wdn-stretch qrc\">")
        f.write("</div>")
        f.write("</body></html>")
        f.write("")
        f.close()

def lerRequest():
	f = open('request.txt')
	s = f.readline()[15:-1]
	f.close()
	return s

dre = lerRequest()
lerResposta()
#os.remove('resposta.txt')

