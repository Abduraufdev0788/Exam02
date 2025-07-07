def sozlar_soni(matn: str) -> dict:
    sozlar = matn.split()
    natija = {}
    for soz in sozlar:
        if soz in natija:
            natija[soz] += 1
        else:
            natija[soz] = 1

    return natija

matn = input("matnni kiriting: ")
print(sozlar_soni(matn))
