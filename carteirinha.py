import sys
from PIL import Image, ImageDraw, ImageFont
import qrcode

#nome='Fulano de Tal com Sobrenome Comprido'
#dre='987654321'
#cpf='123.456.789-10'
#curso='Engenharia de Computação e Informação'
#periodoAtual='2018.2'
#diaN = 1
#mesN = 1
#anoN = 2001
#dataN = str(diaN).zfill(2) + '/' + str(mesN).zfill(2) + '/' + str(anoN)

nome=sys.argv[1]
dre=sys.argv[2]
cpf=sys.argv[3]
curso=sys.argv[4]
periodoAtual=sys.argv[5]
dataN=sys.argv[6]




def imprimir(x,y,texto,tamanho,drawobj):
	f = ImageFont.truetype('KeepCalm-Medium.ttf', tamanho)
	drawobj.text((x,y), texto, font=f, fill=(0,0,0,255))

img = Image.open("fundo.png")
txt = Image.new('RGBA', img.size, (255,255,255,0))
fnt = ImageFont.truetype('KeepCalm-Medium.ttf', 40)

foto = Image.open("3x4.png")
fotoL = 390
fotoA = int(fotoL/3*4)
#foto.resize((30,40),Image.ANTIALIAS)
foto.thumbnail((fotoL,fotoA))
img.paste(foto,(780,190))
margem = 60
altura = [70, 125, 170, 215, 260, 305]
d = ImageDraw.Draw(txt)

imprimir (margem, altura[0], nome,40,d)
imprimir (margem, altura[1], curso,27,d)
imprimir (margem, altura[2], 'Universidade Federal do Rio de Janeiro',27,d)
imprimir (margem, altura[3], 'DRE: '+dre+'    CPF: '+cpf,27,d)
imprimir (margem, altura[4], 'Data de nascimento: ' + dataN,27,d)
imprimir (margem, altura[5], 'Documento válido durante o período '+periodoAtual,27,d) #inserir data do fim do período?

qrSize = 450
qrc = qrcode.make(dre)
qrc = qrc.resize((qrSize,qrSize))

img.paste(qrc,(120,305))
out = Image.alpha_composite(img, txt)
out.save("carteirinha.png", "PNG")


