sugar_kilo = int(input())
num_pack = 0

while sugar_kilo > 0:
    if sugar_kilo%5 != 0:
        sugar_kilo -= 3
        num_pack += 1
        if sugar_kilo < 0:
            num_pack = -1
            break
    elif sugar_kilo%5 == 0:
        sugar_kilo -= 5
        num_pack += 1

print(num_pack)