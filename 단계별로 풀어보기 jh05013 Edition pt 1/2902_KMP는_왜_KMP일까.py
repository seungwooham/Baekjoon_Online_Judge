in_str = input()
a = []

a.append(in_str[0])

for i in range(len(in_str)):
    if in_str[i] == '-':
        a.append(in_str[i+1])

for i in range(len(a)):
    print(a[i], end='')