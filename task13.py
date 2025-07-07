import json

with open("Input/students.json") as f:
    dic = json.load(f)
    Names = list()
    for i in dic:
        if len(i['name']) > 5:
            Names.append(i['name'])
    a = {"long_names" : Names}
    
    
    
with open('Output/output13.json', 'w') as results:
    results.write(json.dumps(a,indent=4))
    