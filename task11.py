import json

with open("Input/students.json") as f:
    text = f.read()
    dic = json.loads(text)
    count  = 0
    for i in dic:
        count +=1
    
    a = {"count" : count}
    
with open('Output/output11.json', 'w') as results:
    results.write(json.dumps(a,indent=4))
    