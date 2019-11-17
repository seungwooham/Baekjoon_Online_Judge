E, S, M = map(int, input().split())

for i in range(1,7981):
    if (i-S)%28 == 0:
        if (i-M)%19 == 0:
            if (i-E)%15 == 0:
                print(i)
                break
            else : None
        else : None
    else: None