"""
Description: This file Demonstrate the searching Keywords of user inputs in 
the Given Text file, and Creating Individual text file for each Keywords.
Author Details
Ps No           : 99003761
Name            : Santosh Kariyavar
E-mail          : santosh.kariyavar@ltts.com
Contact         : 8951096674
Date Of creation: 26/02/2021
"""

import re


class ReadKey:

    def __init__(self, path):
        self.file_path = path
        self.new_file = self.make_input_file(self.file_path)
        self.n_key = int(input("Enter No.Of Key:"))
        self.keys = self.read_keys(self.n_key)  # keywords list

    def read_keys(self, n_key):

        keys = []  # creating a List to store Keys
        for j in range(n_key):  # Reading N times
            keys.append(input("Enter Keys{}: ".format(j + 1)))  # Reading Keys
        return keys

    def make_input_file(self, in_path):

        file_input = open(in_path, "r")  # Input file handler
        out_path = "new_input_file.txt"
        file_output = open(out_path, "w")  # Output file Handler
        count = 1
        for line in file_input:  # for loop for line count and line adding
            file_output.write(str(count) + '\t' + line)  # adding line numbers
            count += 1  # line count
        file_output.close()  # closing file
        file_input.close()
        return out_path

    def count_keys(self, key, path):
        count = 0
        pattern = re.compile(key, re.I)

        with open(path, "rt") as file_lines:
            for line in file_lines:
                count += len(re.findall(pattern, line))
        return count


class SearchKey:

    def __init__(self, key, path):  # keys and new_input_file path
        self.key = key
        self.path = path

    def search_with_line(self, key, file_paths):
        count = 0
        keywords = []
        lines = 0
        pattern = re.compile(key, re.I)

        with open(file_paths, "rt") as file_lines:
            for line in file_lines:
                lines += 1

                if pattern.search(line) is not None:  # checking for empty line
                    keywords.append((lines, line.rstrip('\n')))
            for keys in keywords:
                count += 1
                with open("{}.txt".format(key), 'a') as file_keys:
                    file_keys.writelines(keys[1] + '\n')
        file_lines.close()
        file_keys.close()


file_path = "input.txt"  # file path with name to be Searched for Keywords

obj1 = ReadKey(file_path)  # object created from ReadKey Class
obj2 = SearchKey(obj1.keys, obj1.new_file)  # object by SearchKey Class
print()

for i in range(obj1.n_key):

    obj2.search_with_line(obj1.keys[i], obj1.new_file)
    no_of_keys = obj1.count_keys(obj1.keys[i], "{}.txt".format(obj1.keys[i]))
    text = "'{}' found {} times in Given File".format(obj1.keys[i], no_of_keys)
    with open("{}.txt".format(obj1.keys[i]), "a") as file:
        file.write('\n'+text)
    print(text)
