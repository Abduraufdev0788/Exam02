def ortacha_qiymat(sonlar):
    a = 0
    count = 0
    for son in sonlar:
        a += son
        count += 1
    return a / count
def yuqori_qiymat_olgan_talabalar(sonlar, qiymat):
    return [item for item,value in sonlar.items() if value > qiymat]

students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
print("o'rtacha Baho:", ortacha_qiymat(students.values()))
print("4.25 dan yuqorilar: ", yuqori_qiymat_olgan_talabalar(students, ortacha_qiymat(students.values())))

