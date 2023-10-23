# Functions Class Notes

- Algorithms
- Data

Vending Machine

- money
- item_code

money, item_code -> Vending Machine -> item

GUI - abstract interface

- Interface
- Black Box
  - Takes input
  - Produces out
  - Who cares how?

```py
def function_name():
    #python code
```

## Max Value

- ask the user for 3 numbers
- tell the user what number is the largest

### In Class Code - Monday 10/16

```py
# "hello" -> print -> None
val = print("hello")  # x -> func -> result
# print(val)


def myfunc():
    # Any valid python
    print("hi")
    print("bye")


myfunc()
myfunc()


def find_max():
    max = numbers[0]
    if numbers[1] > max:
        max = numbers[1]
    if numbers[2] > max:
        max = numbers[2]

    print(max)


# Driver Code

number = input("Please enter 3 numbers separated by commas: ")
numbers = number.split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

find_max()

# other code

number = input("Please enter 3 numbers separated by commas: ")
numbers = number.split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

find_max()

for i in range(100):
    number = input("Please enter 3 numbers separated by commas: ")
    numbers = number.split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    find_max()
```

## Parameters

- Single Responsibility Principle
  - "A code block, function, or class should be responsible for one thing"
- Always get data outside of a function

## SCOPE

- Global
  - anything not in a function (or class)
  - Global scope is accessible anywhere in the file
- Local
  - limited to the function (or class) that it was defined in
  - parameters are define in the function
