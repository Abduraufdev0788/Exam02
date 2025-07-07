def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b != 0:
        return a/b
    else:
        return "0 no'lishi mumkin emas"
    
a = float(input("1-sonni kiriting :"))
b = float(input("2-sonni kiriting :"))    
amallar = input("amallar + ,- , *, /")


if amallar == '+':
    natija = add(a, b)
elif amallar == '-':
    natija = subtract(a, b)
elif amallar == '*':
    natija = multiply(a, b)
elif amallar == '/':
    natija = divide(a, b)
else:
    natija = "Notogri amal kiritildi"

print("natija" , natija)