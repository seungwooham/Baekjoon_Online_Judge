num_string = int(input())
num = []
string = []

for i in range(num_string):
    num_tmp, string_tmp = input().split()
    num_tmp = int(num_tmp)
    num.append(num_tmp)
    string.append(string_tmp)

for i in range(num_string):
    for j in range(len(string[i])):
        print(string[i][j]*(num[i]), end='')
    print('')