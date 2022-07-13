import requests
import json


def indent(level,file):
    for i in range(level):
        file.write("    ")

def attribute_is_list(key,list, file, indent_level):
    indent(indent_level,file)
    file.write("<dictionary_list name=\"" + key +  "\"> \n")
    
    list_value = list.pop()

    if(type(list_value) is dict and len(list_value) != 0):
        attribute_is_dict(list_value, file, indent_level + 1)
    
    if(type(list_value) is str):
        attribute_is_str("attribute",list_value, file, indent_level + 1)
                
    if(type(list_value) is list):
        attribute_is_list(list_value, file, indent_level + 1)
    
    indent(indent_level,file)
    file.write(" </dictionary_list> \n")

def attribute_is_dict(attributes_dict, file, indent_level):
    for key in attributes_dict:
         if type(attributes_dict.get(key)) is dict:
            indent(indent_level,file)
            file.write("<dictionary name=\"" + key + "\"> \n")
            attribute_is_dict(attributes_dict.get(key), file, indent_level + 1)
            indent(indent_level,file)
            file.write("</dictionary> \n")

         else:
             attribute_is_str("attribute",key, file, 2)

def attribute_is_str(string, attribute, file, indent_level):    
        indent(indent_level,file)
        file.write("<" + string + ">"+ "\n")
        indent(indent_level + 1, file)
        file.write("<name> " + attribute + " </name> \n")
        indent(indent_level, file)
        file.write("</" + string + ">" + "\n")

def main():
    #accomodation dataset call
    request_url = "https://tourism.api.opendatahub.bz.it/v1/Accommodation/5CEA544EE34639034F07B79D4AEEB603_REDUCED?idsource=lts&availabilitychecklanguage=en&roominfo=1-18%2C18&bokfilter=hgv&source=sinfo&detail=0&removenullvalues=false"
    dataset = "accomodation"

    #event dataset call
    #request_url = "https://tourism.api.opendatahub.bz.it/v1/Event/BFEB2DDB0FD54AC9BC040053A5514A92_REDUCED?removenullvalues=false"
    #dataset = "event"

    #request_url = "https://tourism.api.opendatahub.bz.it/v1/Weather?language=en&extended=true"
    #dataset = "weather"

    #request_url = ""
    #dataset = ""

    file = open("keys_list_tourism_" + dataset + ".xml", "w+")
    file.write("<dataset name=\"" + dataset + "\"> \n")

    json_request = requests.get(request_url)
    json_data = json_request.json()

    indent(1,file)
    file.write("<attributes> \n")

    for key in json_data:
        value = json_data.get(key)
        if type(value) is list and len(value) != 0:
            attribute_is_list(key, value, file, 2)

        elif type(value) is list and len(value) == 0:
            attribute_is_str("list",key, file, 2)

        elif type(value) is dict:
            attribute_is_dict(value, file, 2)
        
        else:
            attribute_is_str("attribute",key, file, 2)

    indent(1,file)
    file.write("</attributes>\n")
    file.write("</dataset>")
    file.close()

if __name__ == "__main__":
    main()
