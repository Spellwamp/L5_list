user_list = []

while True:
    number_int = input('Exit: "Q"\nYour number:')
    if number_int != 'Q':
        user_list.append((number_int))
        continue
    elif number_int == 'Q':
        break


d = eval(' * '.join(user_list))
s = 0

for i in user_list:
    s += int(i)

print('Сумма: {0}\nДобуток: {1}'.format(s, d))
