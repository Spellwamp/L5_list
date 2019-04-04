from random import randint

random_list = []
user_list = []
end_list = []

while True:
    number_int = input('Exit: "Q"\nYour number:')
    if number_int != 'Q':
        user_list.append(int(number_int))
        continue
    elif number_int == 'Q':
        break

for _ in range(len(user_list)):
    a = randint(0, 2)
    random_list.append(a)

for i in random_list:
    for j in user_list:
        end_list.append(i + j)
        break

print(random_list)
print(user_list)
print(end_list)
