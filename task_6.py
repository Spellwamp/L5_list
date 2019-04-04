from random import randint

random_list = []
list_p = []
for _ in range(20):
    a = randint(0, 20)
    random_list.append(a)

for i in range(len(random_list)):
    if random_list[i] != 0:
        if random_list[i] % 2 == 0:
            list_p.append(i)

print('Random list: {0}\nNew list: {1}'.format(random_list, list_p))
