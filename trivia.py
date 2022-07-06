import requests
import random
import time
from threading import Thread
from pytimedinput import timedInput
from pytimedinput import timedKey
# install pytimedinput!!!

# https://the-trivia-api.com/
# user can choose number of questions(up to 20)
# desired difficulty (easy, medium, hard), and question category

# should have method to print categories, and get response
# method to get difficulty
# method to get number of questions

# can store quiz in database if user wishes to return to a a past quiz?

# data is a list where each element is a dictionary for each question
# ( has the question, the correct answers and incorrectAnswers)

# iterate through each question's dictionary

# this is an example url and quiz
url = 'https://the-trivia-api.com/api/' \
+ 'questions?categories=science&limit=10&region=US&difficulty=medium'
response = requests.get(url)
data = response.json()
score = 0
total = 10
# end of example

# global variable used for the countdown
count = True 


# Testing function examples
def func1(x):
    x = x - 1
    return x


def func2(x, y):
    return x + y


# run the countdown for each question
def runn():
    i = 15
    print('Choose an Answer: ')
    print(i, end = '')
    while i >= 0:
        i -= 1
        time.sleep(1)  # sleep one second
        if count is False:
            break
        print('\r' + str(i) + ' ', end = '', flush = True)  # update timer




# display categories
def print_categories():
    print(
      '''
      0- Arts & Literature       5- History
      1- Film & TV               6- Music
      2- Food & Drink            7- Science
      3- General Knowledge       8- Society & Culture
      4- Geography               9- Sports & Leisure

      ''')


# get category selection and return it
def get_category():
    print_categories()
    categories = ['arts_and_literature', 'film_and_tv', 'food_and_drink', 'general_knowledge', 'geography',
                  'history', 'music', 'science', 'society_and_culture', 'sports_and_leisure']
    
    # get response and check if it is an integer
    check_integer = True
    while check_integer:
        try:
            response = input("Please choose a category: ")
            response = int(response)
            category = categories[response]  # if int, use as index to get category
            check_integer = False  # end the loop if successful
        except:  # if the input is not a number or not in the range 0-9, continue loop
            print('Please input a number 0-9')
    return category

# get the difficulty (easy, medium, hard) and return it
def get_difficulty():
    
    difficulty_choices = { "1": "easy", "2" : "medium" , "3" : "hard"}

    chosen_difficulty = input("Please select difficulty: 1-3 ")
    print(" 1. Easy \n 2. Medium \n 3. Hard")
    
    difficulty = difficulty_choices.get(chosen_difficulty) #gets the corresponing difficulty level// test for invalid input
    return difficulty
# get input on the number of questions and return it
def get_questions():
    
    questions = input("How many questions would you like to answer?: ")
    return questions

# create the quiz and returns the list of questions
def create_quiz(category, difficulty, questions):
    url = 'https://the-trivia-api.com/api/questions?categories=' \
        + category +'&limit=' \
        + questions + '&region=US&difficulty=' + difficulty
    response = requests.get(url)
    data = response.json()
    return data


# takes the list of questions as parameter and runs the quiz
def run_quiz(quiz,total):
    score = 0
    total = total
    global count  # boolean used for countdown
    for i in quiz:
        print()
        print("********************************")
        print(f"Score : {score} / {total}")  # change this, it will not always be out of 10

        # print question    
        print(i['question'])

        # list all answer choices
        # print them in a random order'])
        list_i = [i['correctAnswer']] + i['incorrectAnswers']

        a = random.choice(list_i)
        list_i.remove(a)
        b = random.choice(list_i)
        list_i.remove(b)
        c = random.choice(list_i)
        list_i.remove(c)
        d = list_i[0]

        # determine which choice is the right answer
        if i['correctAnswer'] == a:
            correct = 'a'
        elif i['correctAnswer'] == b:
            correct = 'b'
        elif i['correctAnswer'] == c:
            correct = 'c'
        else:
            correct = 'd'
          
        # prompt user to select an option    
        print(f" (a) {a}")
        print(f" (b) {b}")
        print(f" (c) {c}")
        print(f" (d) {d}")
        print(f" press \"q\" to quit")

        # start the countdown
        t = Thread(target=runn)
        t.start()
      
        # the user has 15 seconds and can only select a,b,c,d, or q
        answer, timedOut = timedKey(timeout = 16, allowCharacters='abcdq') 
        count = False
        print()

        # test if user gives correct input,
        if timedOut: # if ran out of time
            print("Sorry you ran out of time!")
            print(f"Correct Answer: {i['correctAnswer']}")
        elif answer == correct: # if correct
            score+=1
            print("Congratulations you are correct!")
        elif answer == 'q': # to quit
          break;
        else: # if incorrect
            print("Wrong! :(")
            print(f"Correct Answer: {i['correctAnswer']}")
        print("********************************")
        time.sleep(2)
        count = True;
        
    print(f"Your Score is: {score}/{total}")


# takes user response, and the correct answer? 
# (may not be needed)
def compare_answers(response, correct_answer):
    pass
    # print the many different responses


if __name__ == '__main__':
    # testing 
    category = get_category()
    difficulty = get_difficulty()
    questions = get_questions()
    quiz = create_quiz(category, difficulty, questions)
    #quiz = create_quiz('arts_and_literature', 'easy', '10')
    run_quiz(quiz, int(questions))
    # run_quiz(quiz, 11)
