# target = int(input())
# break_num = int(input())

# if (break_num==0):
#     pass
# else:
#     break_button = []
#     break_button = list(map(int, input().split()))

# if target == 100:
#     print(0)
# else :
#     min_chg = abs(100-target)
#     for i in range(1000001):
#         num_list = list(map(int, str(i)))
#         if set(num_list)&set(break_button):
#             pass
#         else:
#             min_chg = min(min_chg, len(num_list)+abs(i-target))
#     print(min_chg)

enable_btn_set = {str(x) for x in range(11)}
print(enable_btn_set)
print(type(enable_btn_set))
