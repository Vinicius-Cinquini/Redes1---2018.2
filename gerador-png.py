import sys, io, datetime, qrcode
#import os.path
from os import path
from PIL import Image, ImageDraw, ImageFont
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
            #dre = f.readline()[15:-1]
            nome = f.readline()[15:-1]
            curso = f.readline()[15:-1]
            dre = f.readline()[15:-1]
            nascimento = f.readline()[15:-1]
            foto = f.readline()[15:]
           # cpf = lerRequest()
            print ("Nome: "+nome)
            print ("Curso: "+curso)
            print ("DRE: "+dre)
            print ("Nascimento: "+nascimento)
            print ("CPF: "+lerRequest())

            reconstruirFoto3x4() ####################################################
            gerarDocumento(dre, nome, curso, lerRequest(), nascimento, foto)
                
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
	f3x4.save("FC"+lerRequest()+".png")
	

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


def imprimir(x,y,texto,tamanho,drawobj):
    f = ImageFont.truetype('KeepCalm-Medium.ttf', tamanho)
    drawobj.text((x,y), texto, font=f, fill=(0,0,0,255))


def gerarDocumento(dre, nome, curso, cpf, nascimento, foto):
    #makeQRC(dre)
    #img = Image.open("fundo.png")
    img = Image.open("F"+lerRequest()+".png")
    #img.rectangle(xy=[(0,0) , (900,500)],fill=(255,255,255,255))
    rect = ImageDraw.Draw(img)
    rect.rectangle(xy=[(0,0) , (900,500)],fill=(255,255,255,255))
    txt = Image.new('RGBA', img.size, (255,255,255,0))
    fnt = ImageFont.truetype('KeepCalm-Medium.ttf', 40)

    foto = Image.open("F"+lerRequest()+".png")
    fotoL = 390
    fotoA = int(fotoL/3*4)
    foto.thumbnail((fotoL,fotoA))
    img.paste(foto,(780,190))
    margem = 60
    altura = [70, 125, 170, 215, 260, 305]
    d = ImageDraw.Draw(txt)

    imprimir (margem, altura[0], aluno[cpf][0],40,d)
    imprimir (margem, altura[1], aluno[cpf][1],27,d)
    imprimir (margem, altura[2], 'Universidade Federal do Rio de Janeiro',27,d)
    imprimir (margem, altura[3], 'DRE: '+dre+'    CPF: '+aluno[cpf][2],27,d)
    imprimir (margem, altura[4], 'Data de nascimento: ' + aluno[cpf][3],27,d)
    imprimir (margem, altura[5], 'Documento válido durante o período '+periodoAtual,27,d) #inserir data do fim do período?

    qrSize = 450
    qrc = qrcode.make(dre)
    qrc = qrc.resize((qrSize,qrSize))

    img.paste(qrc,(120,305))
    out = Image.alpha_composite(img, txt)
    out.save("carteirinhas/"+cpf+".png", "PNG")


def lerRequest():
    f = open('request.txt')
    s = f.readline()[15:-1]
    f.close()
    return s

dre = lerRequest()
lerResposta()
#os.remove('resposta.txt')

