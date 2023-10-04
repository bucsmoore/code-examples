# Selection

## Booleans

-bool

- True
- False

```py
print(bool(0))
print(bool(5))
print(bool("Hello"))
```

"True" is True
"False" is True

- False is an empty value
  - 0
  - []
  - ""
  - `None`

```py
x = 5  # assignment operator
y = 6

print(x == y)  # == equality
print(x != y)  # != bang/no equal
print(x > y)  #
print(x < y)  #
print(x >= y)  #
print(x <= y)  #
# print(x => y) ERROR

print(x and y)  # &&
# True and True = True,
# False and True = False
# True and False = False
print(x or y)  # ||
# True or True = True,
# False or True = True
# False or False = False
print(not y)  # !
# False = True

print(x is x)
print(x is y)

x = "He"
y = "Hello"
print(x in y)

x = "" #empty string is a substring of all strings
y = "Hello"
print(x in y) #True
```

## If Statements

## Vending Machine

`if` statement

```py
if <boolean expression>:
    <conditional code>
else: #no condition, optional
    <default code>
```

No Else

```py
if <boolean expression>:
    <conditional code>
```

# Events

OS catching user actions (or other actions), then storing them for your program to use

# Actions (events)

keyboard press
mouse click

# Algorithms (functions)

"put character on screen"
"close window"

# Talking to OS

```py
#events that happens since last call
events = pygame.event.get() #
```

## The event loop

Where you respond to events,
You can have multiple event loops, but only running per frame

### Event Objects

pygame.EVENT_NAME

shapes = [3, 4, 5]

for sh in shapes:
for \_ in range(sh):
...
