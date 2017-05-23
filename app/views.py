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
       
        serializer = getJSon()

        return JsonResponse(serializer, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ImageInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

      
# Fim Funcoes - Intelligent Promoter        
###############################################


###################################################
# INICIO Funcoes - Projeto dos Fungos

# coloquem seus codigos aqui

# Fim Funcoes - Projeto dos Fungos        
###############################################