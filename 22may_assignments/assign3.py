#Assign 3
#Ask for student name, and grade
#Create a function display_student_info(name, grade)
#It should print output as below
## Name: Ravi
## Grade: A

student = {
    'name': input('enter your name: '),
    'grade': input('enter your grade: ') 
}

def display_student_info(name, grade):
    print(f'Name: {name}\nGrade: {grade}')

display_student_info(student['name'], student['grade'])