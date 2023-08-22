# protocols
# - http
# - xml
# - json: javascript object notation
#   - string formats, not file formats
#   - int, float, string, bool, list, dictionary, None
#   - {}:dictionary, [] : list

import json

# data = {
#     "num": 1,
#     "msg": "Hello World",
# }

# json_string = json.dumps(data)
# print(json_string, type(json_string))

# json_data = json.loads(json_string)

# for k, v in json_data.items():
#     print(k, v)

# fptr = open("assets/data.json", "w")  # .json is a convention, it's not a file type
# fptr.write(json_string)
# fptr.close()

# data_str = open("assets/data.json", "r").read()
# data = json.loads(data_str)
# print(data, type(data))

# data = json.load(open("assets/data.json", "r"))
# print(data, type(data))

# fptr = open("assets/data.json", "w")
# data = json.dump(data, fptr)
# fptr.close()
# print(data, type(data))


def main():
    #'a' - appends to the file
    idea = input("Enter an idea: ")

    file_pointer = open("assets/ideas.txt", "r")  # modes: 'r', 'w', 'a'
    data = json.load(file_pointer)
    print(data)
    data.append(idea)
    file_pointer.close()

    file_pointer = open("assets/ideas.txt", "w")
    json.dump(data, file_pointer)
    file_pointer.close()  # always close files


main()
