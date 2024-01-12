import csv
import json
import ast
import re
import pydash

def convert_string_to_dict(s):
    s = re.sub(r'<[^:]+: \'(.*?)\'>', r"'\1'", s)
    
    return {"payload":ast.literal_eval(s)}

def main():
    with open('data.csv', 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        items_list = [convert_string_to_dict(row['body']) for row in reader]
    
    merchants_id= []

    for index, item in enumerate(items_list):
        executed_reason: str= pydash.get(item, "payload.executed_reason", default= None)
        if executed_reason is not None:
            match = re.search(r'\[(.*?)\]', executed_reason)
            if match:
                merchant_id = match.group(1)
                print (f"{index+1}-{merchant_id}")
                merchants_id.append(f"{index+1}-{merchant_id}")
        
    print(merchants_id)
        
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(items_list, json_file, ensure_ascii=False, indent=4)


def main2():
    with open('data_trigger.csv', 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        items_list = [convert_string_to_dict(row['body']) for row in reader]
    
    merchants_id= []

    for index, item in enumerate(items_list):
        executed_reason: str= pydash.get(item, "payload.executed_reason", default= None)
        if executed_reason is not None:
            match = re.search(r'\[(.*?)\]', executed_reason)
            if match:
                merchant_id = match.group(1)
                print (f"{index+1}-{merchant_id}")
                merchants_id.append(f"{index+1}-{merchant_id}")
        
    #print(merchants_id)
        
    #with open('output.json', 'w', encoding='utf-8') as json_file:
    #    json.dump(items_list, json_file, ensure_ascii=False, indent=4)
main()