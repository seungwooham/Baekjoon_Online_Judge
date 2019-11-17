text_list = list(input())

for i in range(int(len(text_list)/10)+1):
    print(''.join(text_list[10*i:10*(i+1)]))