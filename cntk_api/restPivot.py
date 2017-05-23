import base64
from pj_6_scoreImage import *
import helpers
# Recebe uma cadeia de bytes, converte isso para uma imagem.
# pega a imagem e salva no diretorio onde o script 6 do cntk esta setado para reconhecimento


    # chamar esse metodo pelo WS, tem que passar a imagem em bytes e ele retorna string com json
def userRequest(imageJpgBytes):
    receiveImageJpgBytes(receiveImageJpgBytes)
    return getJSon()



def getJSon():
    myJson =  generateJson()# gera o json do cntk
    myJson = applyPrecisionToJSon(3.0,myJson) # aplica um nivel de precisao ex. 2.0 = 20% de precisao
    return myJson

def receiveImageJpgBytes(imageJpgBytes,destPath):
    fh = open(destPath, "wb")
    fh.write( base64.b64decode(imageJpgBytes))
    fh.close()

def readImageToByte(source):
    imageStr =""
    with open(source, "rb") as imageFile:
        imageStr = base64.b64encode(imageFile.read())
    return imageStr


