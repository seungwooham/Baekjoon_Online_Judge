num = int(input())
a = []
b = []

for i in range(num):
    a_tmp, b_tmp = input().split()
    a_tmp = int(a_tmp)
    b_tmp = int(b_tmp)
    a.append(a_tmp)
    b.append(b_tmp)

for i in range(num):
    print(a[i]+b[i])
