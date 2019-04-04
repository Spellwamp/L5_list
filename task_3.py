from random import randint

random_list = []

int_p = 0
int_m = 0
int_zero = 0

for _ in range(20):
    a = randint(-5, 4)
    random_list.append(a)

for i in random_list:
    if i < 0:
        int_m += 1
    elif i == 0:
        int_zero += 1
    elif i > 0:
        int_p += 1

print('Your list: {0}\n+: {1}\n-: {2}\n0: {3}'.format(random_list, int_p, int_m, int_zero))
