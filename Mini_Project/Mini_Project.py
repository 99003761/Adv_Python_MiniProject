import re


def read_keys(n_key):
    keys = []  # creating a List to store Keys

    for j in range(n_key):  # Reading N times
        keys.append(input("Enter KeyWords{}: ".format(j+1)))  # appending  Keys

    return keys


def remove_lines(in_file_path):
    file_input = open(in_file_path, "r")  # input file Handler
    file_out = open("buf.txt", "w")  # out put file handler

    str_line2 = []

    for line in file_input:  # for loop for line count and line adding
        str_line = line.split()
        str_line2.append(str_line)
        file_out.write(str(str_line2))
    file_out.close()

    file_out = open(in_file_path, "w")
    for line in str_line2:
        if len(line[1]) > 2:
            file_out.write(str(line) + '\n')

# closing input file
    file_out.close()
    file_input.close()


def gen_patter(keyword):
    new_pat = "(?i){}".format(keyword)
    return new_pat


def search_keyword(keyword, in_file):
    input_file = open(in_file, "r")
    out_path = "{}.txt".format(keyword)
    out_file = open(out_path, "w")
    pat = gen_patter(keyword)

    mt1 = []
    count = 1

    for line in input_file:  # for loop for line count and line adding
        mt1.append(re.findall(pat, line))
        out_file.write(str(count) + '\t' + str(re.findall(pat, line)) + '\n')
        count += 1  # line count

    new_list = list(filter(None, mt1))

    match_found = len(new_list) + 1
    match = "{} found {} times in the given Files".format(keyword, match_found)
    out_file.write(match)
    out_file.close()  # closing file
    input_file.close()

    remove_lines(out_path)

    print("{} found {} times in the given Files".format(keyword, match_found))
    print()


N_key = int(input("Enter No.Of Key:"))
file_path = "input.txt"

KeyWords = read_keys(N_key)  # keywords list

for i in range(N_key):
    search_keyword(KeyWords[i], file_path)
