import sys
from PIL import Image, ImageDraw, ImageFont
import qrcode

def makeQRC (dre):
	qrSize = 450
	qrc = qrcode.make(dre)
	qrc = qrc.resize((qrSize,qrSize))
	qrc.save("QRC"+dre+".png","PNG") 










########## CHAMADAS ##########

makeQRC("123456789")


