numbers = [
    {'value': -5}, 
    {'value': 10}, 
    {'value': -1}, 
    {'value': 7}
]

values = list(filter(lambda x : x['value'] > 0, numbers))
print(values)