def buble(lst): 
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j][0] > lst[j + 1][0]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
#Использую сортировку пузырьком, где lst - список, который сортирую


f = open('magical.txt', 'r', encoding='UTF-8').readlines()
data = []
sl = {}
for i in f:
    i = i.strip().split('№')
    data.append(i)
data.pop(0)
#Создаю список в котором помещены все значения
data = buble(data)
#Испотзую сортировку
answer = []
for i in data:
    if 'Иван-чай' in i:
        answer.append(i)
#Создаю список в котором все зелья с Иван-Чай
for i in range(3):
    print(f'Зелье {answer[i][0]} имеет в свое составе иван-чай')
#Вписываю ответ
