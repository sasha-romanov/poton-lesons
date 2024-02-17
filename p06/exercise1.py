import random

list_1 = []
list_2 = []

for i in range(5):
    list_1.append(random.randint(0, 10))
    #list_1.append(0)
    list_2.append(random.randint(0, 10))

print(list_1, list_2, sep='\n')

list_3 = []
for i in  list_1:
    if i in list_2:
        list_3.append(i)
