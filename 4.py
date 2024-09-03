f = open("magical.txt", "r", encoding="UTF-8").readlines()
f.pop(0)
data = []
sl = {}

for i in f:
    i = i.strip().split("№")
    if i[1] != "-1" and i[1] != "0":
        data.append(f"{i[0]} осталось в наличии {i[1]} штук")
# Создаю данный список
for i in data:
    print(i)
# Вывожу его
