import requests
import re
import json


def attribute_is_list(key, list, file):
    if len(list)==0:
        file.write("list name=\"" + key +  "\",--empty-- \n")
    else:
        file.write("list name=\"" + key +  "\",--start-- \n")

        while len(list)!=0:

            list_value = list.pop()

            if(type(list_value) is dict and len(list_value) != 0):
                attribute_is_dict(key, list_value, file)

            if(type(list_value) is str):
                attribute_is_str("attribute",list_value, file)
                        
            if(type(list_value) is list):
                attribute_is_list(list_value, file)

        file.write("list name=\"" + key +  "\",--end-- \n")


def attribute_is_dict(key,attributes_dict, file):
    if len(attributes_dict)==0:
        file.write("dictionary name=\"" + key +  "\",--empty-- \n")
    else:
        file.write("dictionary name=\"" + key +  "\",--start-- \n")

        for inner_key in attributes_dict:
            if type(attributes_dict.get(inner_key)) is dict:

                attribute_is_dict(inner_key,attributes_dict.get(inner_key), file)

            else:
                attribute_is_str("attribute",inner_key, file)

        file.write("dictionary name=\"" + key +  "\",--end-- \n")


def attribute_is_str(string, attribute, file):    

        file.write(string +","+attribute + "," + "\n")


def input_datasets_to_list(file_name):
    input_datasets = open(file_name,'r')
    return input_datasets.readlines()


def main():

    datasets = input_datasets_to_list('datasets.txt')
    for line in datasets:
        
        dataset = line.split()[0]
        request_url = line.split()[1]    


        file = open("keys_list_tourism_" + dataset + ".csv", "w+")
        file.write("type identifier," + "attribute name" + "\n\n")

        json_request = requests.get(request_url)
        json_data = json_request.json()


        for key in json_data:
            value = json_data.get(key)
            
            if type(value) is list:
                attribute_is_list(key, value, file)

            elif type(value) is dict:
                attribute_is_dict(key, value, file)
            
            else:
                attribute_is_str("attribute",key, file)

        file.close()

if __name__ == "__main__":
    main()
