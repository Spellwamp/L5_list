from random import randint

random_list = []
for _ in range(20):
    a = randint(0, 20)
    random_list.append(a)

print(random_list)
if random_list.index(min(random_list)) > random_list.index(max(random_list)):
    random_list[random_list.index(min(random_list))], random_list[random_list.index(max(random_list))] = random_list[
                                                                                                             random_list.index(
                                                                                                                 max(
                                                                                                                     random_list))], \
                                                                                                         random_list[
                                                                                                             random_list.index(
                                                                                                                 min(
                                                                                                                     random_list))]
else:
    random_list[random_list.index(max(random_list))], random_list[random_list.index(min(random_list))] = random_list[
                                                                                                             random_list.index(
                                                                                                                 min(
                                                                                                                     random_list))], \
                                                                                                         random_list[
                                                                                                             random_list.index(
                                                                                                                 max(
                                                                                                                     random_list))]
print(random_list)
