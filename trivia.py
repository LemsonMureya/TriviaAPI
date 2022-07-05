import requests
import random
import time

# https://the-trivia-api.com/
url = 'https://the-trivia-api.com/api/questions?categories=science&limit=10&region=US&difficulty=medium'
response = requests.get(url)
data = response.json()
score = 0
total = 10

# user can choose number of questions(up to 20)
# desired difficulty (easy, medium, hard), and question category

# should have method to print categories, and get response
# method to get difficulty
# method to get number of questions

# can store quiz in database if user wishes to return to a a past quiz?

# data is a list where each element is a dictionary for each question
# ( has the question, the correct answers and incorrectAnswers)

# iterate through each question's dictionary
for i in data:
    print()
    print(f"Score : {score} / 10")

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
# prompt user to select an option    
    print(f" (a) {a}")
    print(f" (b) {b}")
    print(f" (c) {c}")
    print(f" (d) {d}")

    
    # test if user gives correct input,
    answer = input("please choose an answer: ")
