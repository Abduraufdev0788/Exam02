students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]
names = list()
for name in students:
    names.append(name['name'])

a = min(names, key=len)
print(a)