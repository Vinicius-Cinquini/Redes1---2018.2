import sys 

def gerarRequest():
    dre=sys.argv[1]
    password=sys.argv[2]
    arq=open("request.txt","w")
    arq.write("GET            "+dre+"\n")
    arq.write("PASSWORD       "+password+"\n\n")
    arq.close()

gerarRequest()


