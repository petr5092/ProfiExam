f = open('magical.txt', 'r', encoding='UTF-8').readlines()
data = []
sl = {}
for i in f:
    i = i.strip().split('№')
    if i[1] == '-1':
        data.append(i)
for i in data:
    for j in range(2, len(i)):
        sl[i[j]] = sl.get(i[j], 0) + 1
with open('magicaPotions.csv', 'w', encoding='UTF-8') as fo:
    print('magic_herbs,count_herbs', file=fo)
    for i in sl:
        answer = ','.join([str(i), str(sl[i])])
        print(answer, file=fo)
