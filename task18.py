numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]

values = list(map(lambda x : {"value": x['value'] **2}, numbers))
print(values)