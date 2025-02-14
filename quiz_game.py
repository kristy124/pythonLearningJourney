quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "answer": 3  # Answer is "Paris" (option 3)
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 2  # Answer is "Mars" (option 2)
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": 4  # Answer is "Pacific Ocean" (option 4)
    }
]

# Initialize score and lists to keep track of correct and incorrect responses
score = 0
correct_questions = []
incorrect_questions = []

print("Welcome to the Quiz Game!")
print("--------------------------\n")

# Iterate over each question in the quiz
for idx, q in enumerate(quiz_questions, start=1):
    print(f"Question {idx}: {q['question']}")
    
    # Display the options numbered for easy selection
    for option_idx, option in enumerate(q['options'], start=1):
        print(f"  {option_idx}. {option}")
    
    # Get user input and validate it
    try:
        user_answer = int(input("Enter the number of your answer: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue  # Skip to the next question if input is invalid

    # Check if the user's answer matches the correct answer
    if user_answer == q['answer']:
        print("Correct!\n")
        score += 1
        correct_questions.append(q)
    else:
        print("Incorrect!")
        correct_option = q['options'][q['answer'] - 1]
        print(f"The correct answer is: {correct_option}\n")
        incorrect_questions.append(q)

# Display the final results
total_questions = len(quiz_questions)
print("Quiz Complete!")
print("--------------------------")
print(f"Your score: {score} out of {total_questions}\n")

# List the questions answered correctly
if correct_questions:
    print("Questions you answered correctly:")
    for q in correct_questions:
        print(f"- {q['question']}")
else:
    print("You did not answer any questions correctly.")

print("\nQuestions you answered incorrectly:")
# List the questions answered incorrectly along with the correct answer
if incorrect_questions:
    for q in incorrect_questions:
        correct_option = q['options'][q['answer'] - 1]
        print(f"- {q['question']} (Correct Answer: {correct_option})")
else:
    print("Great job! You answered everything correctly!")