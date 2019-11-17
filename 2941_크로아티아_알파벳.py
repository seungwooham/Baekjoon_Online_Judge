str_in = input()
str_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for str_ in str_list:
    str_in = str_in.replace(str_, '*')

print(len(str_in))