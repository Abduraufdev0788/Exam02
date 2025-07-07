import json

with open("Input/students.json") as f:
    dic = json.load(f)
    Names = list()
    for i in dic:
        if i['name'].title().startswith("A"):
            Names.append(i['name'])
    a = {"a_names" : Names}
    
    
    
with open('Output/output14.json', 'w') as results:
    results.write(json.dumps(a,indent=4))
    