def mult(x, y):
    accumulator = 0
    for i in range(y):
        accumulator = accumulator + x
    return accumulator


def pow(a, b):
    accumulator = 1
    for i in range(a):
        accumulator = accumulator + b
    return accumulator


def square(z):
    # return pow(z, 2)
    return mult(z, z)


n1 = int(input("enter a num: "))
n2 = int(input("enter another num: "))
result = mult(n1, n2)
result2 = pow(n1, n2)
result3 = square(n1)

print(result, result2, result3)

# write
# - if the file exists, it is immediate deleted
fref = open("data/data.txt", "w")
file_str = str(result)
file_str += "\n" + str(result2)
file_str += "\n" + str(result3)
fref.write(file_str)
fref.close()

# read
fref = open("data/data.txt", "r")

# single_line = fref.readline()
# print(single_line)
# single_line = fref.readline()
# print(single_line)

whole_file_as_str = fref.read()
print(whole_file_as_str)
fref.close()
# append
fref = open("data/data.txt", "a")
fref.write("\n\n Add this line")
