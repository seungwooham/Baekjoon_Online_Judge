x, y = map(int, input().split())

days = 0

for i in range(x-1,0,-1):
    if i== 2:
        days += 28
    elif i in (4, 6, 9, 11):
        days += 30
    else :
        days += 31

days += y-1

week_of_day = days%7

if week_of_day == 0:
    print('MON')
elif week_of_day == 1:
    print('TUE')
elif week_of_day == 2:
    print('WED')
elif week_of_day == 3:
    print('THU')
elif week_of_day == 4:
    print('FRI')
elif week_of_day == 5:
    print('SAT')
else :
    print('SUN')