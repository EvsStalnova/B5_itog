def welcome():
    print('-----------------------')
    print()
    print('  Приветствуем Вас   \n'
          '        в игре       \n'
          '    крестики-нолики    ')
    print()
    print('-----------------------')
    print()
    print('Правила игры:\n'
          '1. Первым ходит Х \n'
          '2. Вводятся координаты от 0 до 2\n'
          '3. Сначала координата по горизонтали, потом по вертика, без пробелов и других символов')
    print()
welcome()

counter = [[' '] * 3 for i in range(3)]

def field():
    print('   0 | 1 | 2 |   ')
    print('-----------------')
    for i, j in enumerate(counter):
        print(f'{i}| {" | " .join(j)} | ')
        print('-----------------')
def checking():
    while True:
        intuser = input('Ваш ход: ')
        if len(intuser) != 2:
            print('Введите 2 координаты!')
            continue
        x, o = intuser
        if not x.isdigit() or not o.isdigit():
            print('Нужны только числа!')
            continue
        x, o = int(x), int(o)
        if 0 < x > 2 or 0 < o > 2:
            print('Вы вышли за пределы поля!')
            continue
        if counter[x][o] != " ":
          print('Клетка занята!')
          continue
        return x, o
def chec_win():
    win_combinate = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win_combinate:
        number_1 = []
        for s in i:
            number_1.append(counter[s[0]][s[1]])
        if number_1 == ['X', 'X', 'X']:
            print('Победа X! Поздравляем!')
            return True
        if number_1 == ['0', '0', '0']:
            print('Победа 0! Поздравляем!')
            return True
    return False

num = 0
while True:
    num += 1
    field()
    if num % 2 == 1:
        print('Ходит X!')
    else:
        print('Ходит 0!')
    x, y = checking()
    if num % 2 == 1:
        counter[x][y] = 'X'
    else:
        counter[x][y] = '0'
    if chec_win():
        break
    if num == 9:
        print('Ничья! Сыграйте еще раз!')
        break
print()