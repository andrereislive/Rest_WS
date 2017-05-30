import json



#json_file = 'd:\Django-Workspace\RestServer\cntk_api\json.json'
#json_data = open(json_file)
#data = json.load(json_data)
myJson = {"clean_image": None, "recognized_objects": [{"score": "6.87916", "bottom": "1140", "right": "654", "nms": "False", "top": "648", "left": "473", "label": "azeite andorinha"}, {"score": "5.2365", "bottom": "822", "right": "972", "nms": "False", "top": "609", "left": "855", "label": "azeite andorinha2"}], "processed_image": ""}
data = {"shelf_share_objects":None}
#data['range'].append(10)


objects_array =  {"share_percentage": "10", "product": "produto1"}
objects_array1 =  {"share_percentage": "10", "product": "produto"}

data = [objects_array]
data.append(objects_array1)

myJson["shelf_share_objects"] = data

print( myJson["recognized_objects"][1]["label"])
