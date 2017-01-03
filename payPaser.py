page = 'AF Schedule Area 077R Northern Mississippi (RUS) Effective_ 17 April 2016.html'
#'AF Schedule Area 124R Memphis, Tennessee (RUS) Effective_ 17 April 2016.html'


def table_parser(filename):
    file = open(filename)
    table = []
    num = 0
    for line in file:
        if 'Grade' in line:
            num += 1
        if num > 0:
            num += 1
        if 3 <= num < 21:
            line = line.rstrip()
            if line != '':
                split_line = line.split(' ')
                split_line = [x for x in split_line if x != '']
                strip_line = split_line[:16]
                table.append(strip_line)
    WG = []
    WL = []
    WS = []
    for l in table:
        # WG.append(l[0:1])
        # WL.append(l[0:1])
        # WS.append(l[0:1])
        WG.append((l[1:6]))
        WL.append(l[6:11])
        WS.append(l[11:16])

    file.close()
    return WG, WL, WS


data = table_parser(page)


for l in data[0]:
    print(l)
print('')
for l in data[1]:
    print(l)
print('')
for l in data[2]:
    print(l)