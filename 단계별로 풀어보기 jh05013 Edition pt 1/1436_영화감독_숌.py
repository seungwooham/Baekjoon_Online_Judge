num = int(input())
small_list = []

for i in range(10001):
    if str(i).count('666'):
        small_list.append(i)

print(small_list[num-1])