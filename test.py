#a trivia game
#imports
import random
#questions and answers
trivia_questions = {
    "What is the capital city of Australia?": "Canberra",
    "Which planet in our solar system is known for its prominent rings?": "Saturn",
    "Who painted the famous artwork 'The Starry Night'?": "Vincent van Gogh",
    "What is the chemical symbol for the element Gold?": "Au",
    "How many bones are present in an adult human body?": "206",
    "Which ocean is the largest and deepest on Earth?": "Pacific Ocean",
    "What is the hardest natural substance known on Earth?": "Diamond",
    "In which year did the Titanic sink?": "1912",
    "Who is the author of the dystopian novel '1984'?": "George Orwell",
    "What is the currency used in Japan?": "Yen",
    "Which element has the atomic number 1 on the periodic table?": "Hydrogen",
    "What is the name of the longest river in the world?": "Nile",
    "Which country gifted the Statue of Liberty to the United States?": "France",
    "What pigment gives plants their green color?": "Chlorophyll",
    "Who was the first person to step foot on the Moon?": "Neil Armstrong",
    "What is the capital city of Canada?": "Ottawa",
    "Which animal is known as the largest mammal in the world?": "Blue Whale",
    "In which country were the first modern Olympic Games held?": "Greece",
    "What is the main gas found in the air that we breathe?": "Nitrogen",
    "Who discovered penicillin in 1928?": "Alexander Fleming",
    "What is the smallest prime number?": "2",
    "Which organ in the human body is responsible for pumping blood?": "Heart",
    "What is the name of the imaginary line that divides the Earth into Northern and Southern hemispheres?": "Equator",
    "Who wrote the famous play 'Romeo and Juliet'?": "William Shakespeare",
    "Which country is the largest by land area?": "Russia"
}
#main game function
def trivia_game():
    print("Welcome to the Trivia Game!")
    score = 0
    questions = list(trivia_questions.keys())
    questions_to_ask = 10
    selected_questions = random.sample(questions, questions_to_ask)
    for index, question in enumerate(selected_questions):
        print(f'Question {index + 1}: {question}')
        user_answer = input("Your answer: ").title().strip()
        correct_answer = trivia_questions[question]
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 10
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")
    print(f"Game Over! Your final score is: {score}/{questions_to_ask * 10}")
                                                     
trivia_game()

print("Would you like to play again? (yes/no)")
while True:
    if input().strip().lower() == "yes":
        trivia_game()
    else:
        print("Thank you for playing! Goodbye!")
        