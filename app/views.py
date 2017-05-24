from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restPivot import * 

###################################################
# INICIO Funcoes - Projeto Intelligent Promoter
@csrf_exempt
def image_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
       
        #serializer = getJSon_Intelligent_promoter()
        serializer = getSavedJSon_Intelligent_promoter()

        return JsonResponse(serializer, safe=False)

   
      
# Fim Funcoes - Intelligent Promoter        
###############################################


###################################################
# INICIO Funcoes - Projeto dos Fungos

# coloquem seus codigos aqui

# Fim Funcoes - Projeto dos Fungos        
###############################################