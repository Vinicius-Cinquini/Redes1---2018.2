nome = "N"
curso = "C"
cpf = "CPF"
nascimento = "Nasc."

def gerarDocumento(registro):
        dre = sys.argv[1]
        makeQRC(dre)
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



