print("Welcome to the Python Quiz!")
question = input("What does CPU stand for? ")
correct_answer = "Central Processing Unit"
score = 0
if question.lower() == correct_answer.lower():
    print("Correct!")
    score += 1 
else:
    print(f"Incorrect!\nThe correct answer is {correct_answer}.")
question_2 = input("What does RAM stand for? ")
correct_answer_2 = "Random Access Memory"    
if question_2.lower() == correct_answer_2.lower():
    print("Correct!")
    score += 1
else:
    print(f"Incorrect!\nThe correct answer is {correct_answer_2}.")
question_3 = input("What does GPU stand for? ")
correct_answer_3 = "Graphics Processing Unit"    
if question_3.lower() == correct_answer_3.lower():
    print("Correct!")
    score += 1
else:
    print(f"Incorrect!\nThe correct answer is {correct_answer_3}.")
print(f"\nYour score is: {score}")
percentage = (score / 3) * 100
print(f"Your percentage is: {percentage:.2f}%")
if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 50:
    print("You passed the quiz, but there's room for improvement.")
else:
    print("You did not pass the quiz. Better luck next time!") 