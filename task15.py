import csv
with open('Input/grades.csv') as grades :
    reader = csv.DictReader(grades)
    max_student = 0
    max_grades = -1
    for i in reader:
        grade = int(i['grade'])
        if grade > max_grades:
            max_grades = grade
            max_student = i['name']
            
with open("Output/output15.txt", "w") as output_file:
    output_file.write(f"Bahosi eng yuqori o'quvchi: {max_student} - {max_grades}")