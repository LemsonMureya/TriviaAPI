import requests
import random
import time
from threading import Thread
from pytimedinput import timedInput
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
url = 'https://the-trivia-api.com/api/questions?categories=science&limit=10&region=US&difficulty=medium'
response = requests.get(url)
data = response.json()
score = 0
total = 10 
#end of example

#global variable used for the countdown
count = True 

# Testing function examples
def func1(x):
  x = x-1
  return x


def func2(x,y):
  return x+y

# run the countdown for each question
def runn():
    i=15
    print('Choose an Answer: ')
    print(i, end = '')
    while i>=0:
        i-=1
        time.sleep(1) #sleep one second
        if count == False:
          break;
        print('\r'+str(i)+ ' ', end='', flush=True) #update timer


for i in data:
    print()
    print("********************************")
    print(f"Score : {score} / 10")  # change this, it will not always be out of 10

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
  
    # the user has 15 seconds
    answer, timedOut = timedInput(timeout = 16) 
    count = False
    print()

    # test if user gives correct input,

    if timedOut: # if ran out of time
        print("Sorry you ran out of time!")
        print(f"Correct Answer: {i['correctAnswer']}")
    elif answer == correct: # if correct
        score+=1
        print("Congratulations you are correct!")
    elif answer == 'q': #to quit
       break;
    else: #if incorrect
        print("Wrong! :(")
        print(f"Correct Answer: {i['correctAnswer']}")
    print("********************************")
    time.sleep(2)
    count = True;

print(f"Your Score is: {score}/{total}")

# display categories
def print_categories():
  pass

# get category selection and return it
def get_category():
   pass

# get the difficulty (easy, medium, hard) and return it
def get_difficulty():
    pass

# get input on the number of questions and return it
def get_questions():
    pass

# create the quiz and returns the list of questions
def create_quiz(category, difficulty, questions):
    pass

# takes the list of questions as parameter and runs the quiz
def run_quiz(quiz):
    pass

# takes user response, and the correct answer? 
# (may not be needed)
def compare_answers(response, correct_answer):
    pass
    # print the many different responses

# if __name__ == '__main__':
