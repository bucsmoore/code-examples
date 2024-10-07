## CH4: While Loops Notes

## Iteration

Looping through some collection

- if looping is possible, we call the data:

*Iterable*

list : []
str: ""

# Mutability

- Can it be changed?

- Immutable: cannot be changed
  - str, tuple
- Mutable: can be changed
  - list, dictionary


## Slicing

# range(0, 10)

someiterable[start:stop]
- start: inclusive
- stop: exclusive

# enumerate

```
for idx,value in enumerate(list):
    list[idx] = value * 2
```

## While Loop

```py
while <condition>: #ends when the condition is no longer True
    operations
    operations
done
```

## Tuples

- Tuples are lists
- Tuples are immutable
- Define: (1,2,3)


### Binary Search

- The fastest way to search a sorted list is to divide the problem set in half, and determine which half the answer is in, then repeat until you find the answer.

## Dictionaries