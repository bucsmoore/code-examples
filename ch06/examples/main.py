import json

# json is a string format, not a file format

# files
# - saved program state

# Operating System: - manage files
# request the file from OS
# - where
# - name
# - how to use it

# - working with files is one-way


def main():
    # file_pointer = open("assets/ideas.txt", "r")  # FILE
    # ideas = file_pointer.read()
    # print(ideas)
    # ideas = file_pointer.readlines()
    # print(ideas[1])
    # ideas = file_pointer.readline()
    # print(ideas)
    # file_pointer.close()  # close the file to reste the file cursor
    # file_pointer = open("assets/ideas.txt", "r")
    # ideas = file_pointer.readline()
    # print(ideas)

    # file_pointer = open("assets/ideas.txt", "a")  # the file gets truncated

    # idea = input("Enter an idea: ")
    # ideas = []
    # ideas.append(idea)

    # # character for a line break "\n"
    # for i in ideas:
    #     file_pointer.write(i + "\n")
    #     # x = 5 / 0

    # # always close files when writing
    # file_pointer.close()

    # file_contents = open("assets/ideas.txt", "r").read()  # truncate the file
    # print(file_contents, type(file_contents))
    # data = json.loads(file_contents)
    # print(data, type(data))

    # file_pointer = open("assets/ideas.txt", "r")  # modes: 'r', 'w', 'a'
    # file_contents1 = file_pointer.readline() # first line as a string
    # file_contents2 = file_pointer.readline() # second line as a string
    # file_contents_rest = file_pointer.read() #entire files in a single string
    # file_contents = file_pointer.readlines() #each lines as a sting in a list
    # for line in file_pointer:
    #     print(line)

    # file streams - one way

    #'w' - deletes any existing file, truncate the file
    file_pointer = open("assets/ideas.txt", "w")  # modes: 'r', 'w', 'a'
    file_pointer.write("Hello World")  # does nto add the newline <enter> like print
    file_pointer.write("\n")  # \n
    file_pointer.close()  # always close files

    #'a' - appends to the file
    file_pointer = open("assets/ideas.txt", "a")  # modes: 'r', 'w', 'a'
    file_pointer.write("Hello World")  # does nto add the newline <enter> like print
    file_pointer.write("\n")  # \n
    file_pointer.close()  # always close files


main()
