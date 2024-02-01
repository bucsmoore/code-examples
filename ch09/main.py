import json
import random

import requests


# Proxy class
class TriviaAPI:

    def __init__(self, category=18, amount=1):
        self.url = f'https://opentdb.com/api.php'
        self.params = f'amount={amount}&category={category}'

    def get(self):
        r = requests.get(f'{self.url}?{self.params}')
        response = r.json()
        if response.get('results'):
            return response['results']
        else:
            return None

    def change_category(self, category):
        pass
        #self.url = #...

def main():
    # trivia = TriviaAPI()
    # result = trivia.get()
    # print(result)
    var = 5
    res = input("Please enter a json formatted string:")

    result = json.loads(res) #dumps
    print(result['KEY'])
    del result['KEY']
    print(result)

    data_obj = {
        "key1": 9, 
        "key2":"hi"
    }
    
    

main()