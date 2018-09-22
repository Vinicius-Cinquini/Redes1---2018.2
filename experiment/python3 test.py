from PIL import Image
import io

def imageToByteArray():
	img = Image.open("originalImage.png")
	byteArray = io.BytesIO()
	img.save(byteArray, format="PNG")
	byteArray = byteArray.getvalue()
	return byteArray

def storeImageAsText():
        txtFile = open("storedBytes.txt","w+")
        txtFile.write(str(imageToByteArray()))
        txtFile.close()

def readImageFromTextFile():
	txtFile = open("storedBytes.txt", "r")
	myString = txtFile.readline()
	imageObj = Image.frombytes("RGB", (500,500), myString.encode('utf-8'), 'raw')
	imageObj.save ("reconstructedImage.png")
	txtFile.close()

storeImageAsText()
readImageFromTextFile()
