import time
import importlib
from restPivot import *
import PARAMETERS
locals().update(importlib.import_module("PARAMETERS").__dict__)

start_time = time.time()
imageInBytes = readImageToByte(recognizeDir+"1.jpg")
receiveImageJpgBytes(imageInBytes, recognizeDir+"newImage.jpg")

print("FIM DO PROCESSAMENTO")

print("Levou %s segundos de processamento ---" % (time.time() - start_time))