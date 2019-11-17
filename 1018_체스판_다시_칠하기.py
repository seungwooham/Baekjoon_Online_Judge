a, b = map(int, input().split())

input_board = [list(input()) for _ in range(a)]

# while True:
#     try:
#         input_board.append(list(input().split()[0]))
#     except EOFError:
#         break

# 멀쩡한 보드 두개 만들어서 비교하자
board_1=[]
board_2=[]

# 보드 만드는 과정
for i in range(a):
    if i%2==0:
        board_1.append(list('WB'*(b//2)+'W'*(b%2)))
        board_2.append(list('BW'*(b//2)+'B'*(b%2)))
    else:
        board_2.append(list('WB'*(b//2)+'W'*(b%2)))
        board_1.append(list('BW'*(b//2)+'B'*(b%2)))

# 이제 비교해봅시다

compare_1 = []
compare_2 = []
tmp_1 = []
tmp_2 = []

for i in range(a):
    for j in range(b):
        if input_board[i][j]==board_1[i][j]:
            tmp_1.append(0)
        else:
            tmp_1.append(1)
        
        if input_board[i][j]==board_2[i][j]:
            tmp_2.append(0)
        else:
            tmp_2.append(1)
    compare_1.append(tmp_1)
    compare_2.append(tmp_2)
    tmp_1 = []
    tmp_2 = []

cnt_1 = 0
cnt_2 = 0
cnt = 99999

for i in range(a-7):
    for j in range(b-7):
        for i_2 in range(i,i+8):
            cnt_1 += sum(compare_1[i_2][j:j+8])
            cnt_2 += sum(compare_2[i_2][j:j+8])

        if cnt > min(cnt_1, cnt_2):
            cnt = min(cnt_1, cnt_2)
        cnt_1 = 0
        cnt_2 = 0

print(cnt)