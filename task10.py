with open('Input/numbers.txt', 'r') as nums :
    numbers = [int(num) for num in nums]
    numbers.sort()
    
    
with open('Output/output10.txt', 'w') as results :
    for number in numbers:
        results.write(f"{number}\n")
    