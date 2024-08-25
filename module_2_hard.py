number = int(input('Введите число из камня в первом поле '))
list = []
if 2 < number < 21:
    for i in range(1, number):
        for j in range(1, number):
            if i >= j:
                continue
            elif number % (i + j) == 0 and i + j != 2 and j != 1:
                first = i
                second = j
                list.append(i)
                list.append(j)
    print('Введите этот пароль во вторую вставку, чтобы открылась дверь: ', *list, sep='')
else:
    print('Камня с таким числом нет!')
