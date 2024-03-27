import random

import requests

# https://opentdb.com/api.php?amount=10&category=1
# https://[host]/[resource]?[param=val]&[param2=val]

amount = 1
category = 18

url = f"https://opentdb.com/api.php?amount={amount}&category={category}"

response = requests.get(url)
print(response.status_code)
data = response.json()
print(data)
for trivia in data["results"]:
    answers = trivia["incorrect_answers"] + [trivia["correct_answer"]]
    # shuffle the array for random order
    random.shuffle(answers)

    print(f"{trivia['question']} \n-- Please select the correct answer:\n===")

    # enumerate(): returns a tuple of the index and the value for each list item
    # display all possible answers
    for i, a in enumerate(answers):
        print(f"{i}){a}")

    # ask the user for their choice
    choice = int(input(":"))
    if answers[choice] == trivia["correct_answer"]:
        print("correct, I guess.")
    else:
        print(f"Actually, {trivia['correct_answer']}")
