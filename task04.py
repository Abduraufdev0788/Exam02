def name(Name:str):
    a = Name.title().split(" ")
    
    if len(a) == 3 :
        return f"{a[1]} {a[2]} {a[0]}"
    elif len(a) == 4 :
        return f"{a[1]} {a[2]} {a[3]} {a[0]}"
    else:
        return "formatni togri kiriting"
    
Name = input("Familya Ism Sharifingizni kriting: ")

print(name(Name))