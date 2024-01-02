def create_student():
    student = {}
    student['class'] = input("Enter class name: ")
    student['name'] = input("Enter student name: ")
    student['age'] = int(input("Enter student age: "))
    student['grade'] = int(input("Enter student grade: "))
    return student

def find_highest_grade_student(students_list):
    highest_grade_student = None
    for student in students_list:
        if highest_grade_student is None or student['grade'] > highest_grade_student['grade']:
            highest_grade_student = student
    return highest_grade_student


students = []
classes = {}

# a
n = int(input("Enter the number of student: "))
for i in range (n):
    print(f"Enter information for student {i+1}: ")
    student = create_student()
    print()
    students.append(student)

for student in students:
    class_name = student['class']
    if class_name not in classes:
        classes[class_name] = [student]
    else:
        classes[class_name].append(student)

print("Class list: ")
for student in students:
    print("Class: {}, Name: {}, Age: {}, Grade: {}".format(student['class'], student['name'], student['age'], student['grade']))
print()

# b
print("The class list of student: ")
for class_name, student_list in classes.items():
    student_name = []
    for student in student_list:
        student_name.append(student['name'])
    student_list_str = ', '.join(student_name)
    print("Class {}: [{}].".format(class_name, student_list_str))
print()

# c
highest_grade_student = find_highest_grade_student(students)
print(f"The student with the highest grade is: {highest_grade_student['name']}")
