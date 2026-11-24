# Student Grade Calculator for grade calculation based on scores
print("Welcome to the Student Grade Calculator!")

# Get user input for student name and scores
student_name = input("Enter the student's name: ")
marks_obtained = float(input("Enter the marks obtained: "))

#Decision making based on the marks obtained
if marks_obtained > 100 or marks_obtained < 0:
    print("invalid format please try again")
else:
    if marks_obtained >= 90:
        print(f"{student_name} has scored an A grade.")
    elif marks_obtained >= 80:
        print(f"{student_name} has scored a B grade")
    elif marks_obtained >= 70:
        print(f"{student_name} has scored a C grade")
    elif marks_obtained>= 60:
        print(f"{student_name} has scored a D grade")
    else:
        print(f"{student_name} has scored an F grade")