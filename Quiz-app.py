print("Welcome to the Python Quiz!")
question = input("What does CPU stand for? ")
correct_answer = "Central Processing Unit"
score = 0
if question.lower() == correct_answer.lower():
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
question_2 = input("What does RAM stand for? ")
correct_answer_2 = "Random Access Memory"    
if question_2.lower() == correct_answer_2.lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print(f"Your score is: {score}")