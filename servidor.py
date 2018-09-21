import sys, io, datetime, qrcode
#from PIL import Image #, ImageDraw, ImageFont
import registros

hoje = datetime.datetime.now()

request = open("request.txt", "r")
dre = request.readline()[15:-1]
password = request.readline()[15:-1]
#print ("DRE solicitado: "+dre)
#print ("Senha digitada: "+password)


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

def foto3x4():
        foto = Image.open("F"+sys.argv[1]+".png")
        byteArray = io.BytesIO()
        foto.save(byteArray, format="PNG")
        byteArray = byteArray.getvalue()
        return byteArray

"""
def montarMensagem(registro):
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
        arq.write("STATUS         0 OK\n")
        arq.write("NOME           "+registro[dre][0]+"\n")
        arq.write("CURSO          "+registro[dre][1]+"\n")
        arq.write("CPF            "+registro[dre][2]+"\n")
        arq.write("NASCIMENTO     "+registro[dre][3]+"\n")
        #arq.write("FOTO           "+str(foto3x4())+"\n\n")
        arq.close()


######## EXECUTANDO ########

#montarMensagem(registro)
montarArquivo(registro)

