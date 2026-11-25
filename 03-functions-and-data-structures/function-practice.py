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

#list
fruits = ["apple", "banana", "orange", "grape"]
fruits[3] = "pineapple"
fruits.append("mango")
fruits.remove("banana")
print(fruits)

scores = [45, 80, 32, 90, 65]
for score in scores:
    if score >= 70:
        print(score)

scores = [45, 80, 32, 90, 65]
count = 0
for score in scores:
    if score < 50:
        count += 1
print(count)

numbers = [5, 10, 15, 20]
total = 0
for number in numbers:
    total += number
print(total)