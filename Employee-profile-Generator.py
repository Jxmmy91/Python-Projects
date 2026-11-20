# Employee Profile Generator but i made use of both string concatenation and f-string formatting to display the employee information in a more readable format. The program prompts the user for their first name, last name, age, and address, and then generates a profile card with all the relevant details.
# i also made use of input() function to get user input and store it in variables. The program also includes a sample employee code and extracts the department, year code, and initials from it using string slicing. Finally, the program prints out all the information in a clear and organized manner.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
full_name = first_name + " " + last_name
address = input("Enter your address: ")
print(f"Hello, my name is {full_name} and I am {age} years old.")
print(f"My address is {address}.")
employee_info = full_name + " is " + age + " years old and lives at " + address
print(employee_info)
experience_years = 5
experience_info = "Experience: " + str(experience_years) + " years" 
print(experience_info)
position = "Cybersecurity Analyst"
salary = 75000
employee_card = f"Employee Card:\nName: {full_name}\nAge: {age}\nAddress: {address}\nPosition: {position}\nSalary: ${salary}\nExperience: {experience_years} years"
print(employee_card)
employee_code = "DEV-2026-JX-911"
department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
print(department)
print(year_code)
print(initials)