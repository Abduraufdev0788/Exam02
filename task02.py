def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Hisobda yetarli mablag' mavjud emas.")
        return balance
    return balance - amount

def check_balance(balance):
    print(f" Balansingiz: {balance} so'm")

balance = 100000
print("1) deposit")
print("2) withdraw")
print("3) check_balance")
operation = input("quyidagilardan birini tanlang :")


if operation == "1":
    amount = int(input("depsit summani kiriting: "))
    balance = deposit(balance, amount)
    print(f" Yangi balans: {balance} so'm")

elif operation == "2":
    amount = int(input("depsit summani kiriting: "))
    balance = withdraw(balance, amount)
    print(f" Yangi balans: {balance} so'm")

elif operation == "3":
    check_balance(balance)

else:
    print(" Noto'g'ri amal kiritildi.")
