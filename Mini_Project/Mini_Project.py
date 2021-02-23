import re       # importing regular Expression Module
n_key = int(input("Enter the No.of Keys"))  # No.of Keys
keys = []  # creating a List to store Keys
for i in range(n_key):  # Reading N times
    keys.append(input("Enter Key Words"))  # appending list with Keys
print(keys)
pattern = r""
file_input = open("input.txt", "r")  # file_output = open("new_file.txt", "w")
key1=[]
for line in file_input:
    # print(line, end='')
    key1 = re.findall("Software", line)

print(len(key1))

    # file_output.write(line)

# for line in file_input:
    # print(line, end='')
    # file_output.write(line)
# file_output.close()
file_input.close()
