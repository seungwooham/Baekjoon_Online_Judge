num_sbj = int(input())
score = list(map(int, input().split()))
print(sum(score)*100/max(score)/num_sbj)