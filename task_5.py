from random import randint

random_list = []

for _ in range(20):
    a = randint(-5, 4)
    random_list.append(a)

range_random_list = 0

print('Your list: {0}'.format(random_list))

while range_random_list < len(random_list):
    if random_list[range_random_list] < 0:
        del random_list[range_random_list]
    else: range_random_list += 1

print('New list: {0}'.format(random_list))
