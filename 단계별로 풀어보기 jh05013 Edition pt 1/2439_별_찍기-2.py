a = int(input())

for i in range(a):
    print(" "*(a-i-1)+'*'*(i+1))


# 이렇게 하면 이상하게도 * 앞에 공백이 출력된다
# When you try this, there is a strange space before printing
# for i in range(a):
#     print(" "*(a-i-1), '*'*(i+1))
