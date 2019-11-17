num_case = int(input())

total = []

for i in range(num_case):
    one_line = list(map(int, input().split()))
    total.append(one_line)

for i in range(len(total)):
    cnt = 0
    total_mean = sum(total[i][1:])/(len(total[i])-1)
    frac = 1/(len(total[i])-1)
    for j in range(1, len(total[i])):
        if total[i][j] > total_mean:
            cnt += frac
    print(format(cnt*100, '.3f'), '%', sep='')