def welcome():
    print("Welcome to the function practice module!")
welcome()    
def greet(name):
    print(f"Welcome, {name}!")
greet("Emmanuel")

def multiply(num1, num2):
    result = num1 * num2
    return result
answer = multiply(10, 5)
print(answer)

def calculate_total(price, quantity):
    total = price * quantity
    return total
amount = calculate_total(2000, 3)
print(f"Total cost: ₦{amount}")

def greet(name='guest'):
    print(f"Welcome, {name}!")
greet()    
greet("Emmanuel")

def get_student_info():
    name = "James"
    score = 85
    return name, score
student_name, student_score = get_student_info()
print(student_name)
print(student_score)