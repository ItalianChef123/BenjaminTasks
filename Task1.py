list = []
score = 0
for i in range(7):
    num = int(input("Give number"))
    list.append(num)
for i in list:
    if i == 4 or i == 8:
        score = score + 2
if 9 in list:
    score = 0
print(score)