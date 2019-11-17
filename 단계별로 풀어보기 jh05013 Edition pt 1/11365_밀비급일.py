lines = []

while True:
    lines_tmp = input()
    if lines_tmp=='END':
        break
    else:
        lines.append(lines_tmp)

for i in range(len(lines)):
    print(lines[i][::-1])