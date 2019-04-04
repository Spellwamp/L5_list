from random import randint

random_list = []
random_list_p = []
random_list_m = []

for _ in range(20):
    a = randint(-5, 4)
    random_list.append(a)

for i in random_list:
    if i < 0:
        random_list_m.append(i)
    elif i > 0:
        random_list_p.append(i)

print('Your list: {0}\n+: {1}\n-: {2}'.format(random_list, random_list_p, random_list_m))
