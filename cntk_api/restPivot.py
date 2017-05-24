import base64
from pj_6_scoreImage import *
import helpers
# Recebe uma cadeia de bytes, converte isso para uma imagem.
# pega a imagem e salva no diretorio onde o script 6 do cntk esta setado para reconhecimento


    # chamar esse metodo pelo WS, tem que passar a imagem em bytes e ele retorna string com json
def userRequest(imageJpgBytes):
    
    receiveImageJpgBytes(receiveImageJpgBytes)
    return getJSon()

def getJSon_Intelligent_promoter():
    #img = readImageToByte("D:/1.jpg")
    #myJson = {"imagem":str(img)}
    myJson =  generateJson()# gera o json do cntk
    return myJson

def getSavedJSon_Intelligent_promoter():
    myJson = json.loads(readTxtToString( recognizeDir+"return.json"))
    return myJson    





