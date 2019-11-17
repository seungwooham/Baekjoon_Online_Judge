def split(word):
    return list(word)

word_input = split(input())

alpha = 'a'
alpha_list = [-1]*(26)

for i in range(0,26):
    for j in range(len(word_input)):
        if word_input[j]==alpha:
            if alpha_list[i] != -1:
                pass
            else: alpha_list[i]=j
    alpha = chr(ord(alpha)+1)

for i in range(len(alpha_list)):
    print(alpha_list[i], end=' ')