with open('Input/numbers.txt', "r") as nums:
    numbers = [int(num) for num in nums]
    a = 0 
    for i in numbers:
        a += i
with open('Output/output08.txt', 'w') as result:
    result.write(f"yigindi: {a}")