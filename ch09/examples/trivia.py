#external library, much better than built in network library
#for shuffling possible answers later
import random

import requests


class TriviaAPI:

    def __init__(self, category=18, amount=1):
        self.url = f'https://opentdb.com/api.php?amount={amount}&category={category}'

    def get(self):
        r = requests.get(self.url)
        #response is just a json dictonary of values after .json() call
        response = r.json()
        #check to make sure I got a question, i.e. results
        if response.get('results'):
            return response['results']
        else:
            return None

    def change_category(self, category):
        pass
        #self.url = #...
        

def trivia():
    #Proxy Class
    tapi = TriviaAPI.TriviaAPI(amount=2)
    results = tapi.get()
    for trivia in results:
        #combine the incorrect and corrects into a single array
        answers = trivia['incorrect_answers'] + [trivia['correct_answer']]
        #shuffle the array for random order
        random.shuffle(answers)
        
        print(f"{trivia['question']} \n-- Please select the correct answer:\n===")
        
        #enumerate(): returns a tuple of the index and the value for each list item
        #display all possible answers
        for i, a in enumerate(answers):
            print(f"{i}){a}")

        #ask the user for their choice
        choice = int(input(":"))
        if answers[choice] == trivia['correct_answer']:
            print("correct, I guess.")
        else:
            print(f"Actually, {trivia['correct_answer']}")