def create_hash(n):
    s = 0
    for i in range(len(n)):
        s += ord(n[i]) * 71**i
    return s % 10**9


# Создаю хэш для значения n


f = open("magical.txt", "r", encoding="UTF-8").readlines()
f.pop(0)
data = []
sl = {}
sl_h = {}
for i in f:
    i = i.strip().split("№")
    h = create_hash(i[0])
    sl_h[h] = i[0]
    sl[h] = sl.get(h, 0) + 1
# Cоздаю хэш таблицу
maxim = max(sl.values())
for i in sl:
    if sl[i] == maxim:
        print(f"Зелье с максимальным количеством рецептов {sl_h[i]} - {sl[i]}")
# Вывожу ответ
