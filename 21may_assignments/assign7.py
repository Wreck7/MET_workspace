# Assignment 7: 🧑‍🎓 Student Grades (Dict of Tuples)
# 📘 Objective:
# Check if a student has passed based on average marks.
# ✅ Steps:
# 1. Create a dictionary with student names as keys and a tuple of 3 marks as values:
# students = {
#    "Alice": (85, 90, 78),
#    "Bob": (50, 45, 60)
# }
# 2. Ask the user to input a student name.
# 3. Use if to check if the student exists.
# 4. If found:
# • Calculate the average using the tuple.
# • If average ≥ 60: print "Passed"
# • Else: print "Failed"
# 5. If student not found, print "Student not found."


students = {
   "Alice": (85, 90, 78),
   "Bob": (50, 45, 60)
}

student_names = list(students.keys())

username_input = input('enter your name: ').capitalize()

if username_input in student_names:
    average = sum(students[username_input]) // len(students[username_input])
    # print(average)
    if average >= 60:
        print('passed')
    else:
        print('failed')
else:
    print('student not found!')

# print(student_names)



