import csv
with open('Input/grades.csv') as grades :
    reader = csv.DictReader(grades)
    count = 0
    for i in reader:
        grade = int(i['grade'])
        if grade == 5:
            count += 1
            
            
with open("Output/output16.txt", "w") as output_file:
    output_file.write(f"5 baho olganlar soni : {count}")