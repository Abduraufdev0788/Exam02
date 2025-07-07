def calculate_tax(salary):
    if salary > 5000000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return int(tax)

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    net = salary - tax
    return int(net)


salary = int(input("maoshni kiriting: "))

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print(f"Soliq: {tax:,} so'm")
print(f"Sof maosh: {net_salary:,} so'm")
