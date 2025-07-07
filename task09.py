with open('Input/numbers.txt', 'r') as nums :
    numbers = [int(num) for num in nums]
    max_num = max(numbers)
    
with open('Output/output09.txt', 'w') as results :
    results.write(f"Eng katta son: {max_num}")