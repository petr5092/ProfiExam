def binary_search(lst, cur):
    answer = []
    l = 0
    r = len(lst) - 1
    while l <= r:
        mid = (l + r) // 2
        if lst[mid][2] == cur:
            answer.append(mid)
            lst.pop(mid)
        if lst[mid][2] < cur:
            l = mid + 1
        else:
            r = mid - 1
    return answer


cur = ''
while cur != 'стоп':
    cur = input()
    f = open('magical.txt', 'r', encoding='UTF-8').readlines()
    data = []
    sl = {}
    fake_data =[]
    for i in f:
        i = i.strip().split('№')
        data.append(i)
        fake_data.append(i)
    data.pop(0)
    data.sort(key=lambda x: x[2])
    fake_data.sort(key=lambda x: x[2])
    answer = binary_search(data, 'Трава удачи четырехлистника')
    mina = float('inf')
    if answer:
        for i in answer:
            if min(mina, int(fake_data[i][1])) != mina:
                mina = int(fake_data[i][1])
                answer1 = fake_data[i]
        print(f'{cur} используется в {answer1[0]}, его количество составляет : {answer1[1]}')
    else:
        print('Такую траву мы не используем')
