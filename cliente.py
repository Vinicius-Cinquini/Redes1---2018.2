import sys 

def gerarRequest():
    cpf=sys.argv[1]
    password=sys.argv[2]
    arq=open("request.txt","w")
    arq.write("GET             "+cpf+"\n")
    arq.write("PASSWORD        "+password+"\n\n")
    arq.close()

gerarRequest()


