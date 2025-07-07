import json

with open("Input/students.json") as f:
    dic = json.load(f)
    Names = list()
    for i in dic:
        Names.append(i['name'])
    Names.sort()  
    a = {'sorted_names': Names}
    
    
with open('Output/output12.json', 'w') as results:
    results.write(json.dumps(a,indent=4))
    