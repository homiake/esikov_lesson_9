field = list(range(1, 10))


def Draw_and_refresh_field():
    global field
    print('\n')
    for i in range(3):
        print(f'{field[0 + i * 3]} | {field[1 + i * 3]} | {field[2 + i * 3]}')
        if i != 2:
            print('-' * 10)
        else:
            print('\n')


def Answer_player(x_or_o):
    check = False
    while not check:
        player_answer = input(f'Куда поставим {x_or_o}: ')
        try:
            player_answer = int(player_answer)
        except:
            print('Попробуй еще раз ввести целое число: ')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer - 1]) not in "XO"):
                field[player_answer - 1] = x_or_o
                check = True
            else:
                print('Эта клетка уже занята.Будь внимательней!')


def Win():
    global field
    winning_values = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for cell in winning_values:
        if field[cell[0]] == field[cell[1]] == field[cell[2]]:
            return field[cell[0]]
    return False


def Game_tic_tac_toe():
    global field
    move = 0
    count = 0
    win = False
    while not win:
        Draw_and_refresh_field()
        if move == 0:
            Answer_player('X')
            move = 1
            count += 1
        else:
            Answer_player('O')
            move = 0
            count += 1
        if count > 4:
            Draw_and_refresh_field()
            tmp = Win()
            if tmp:
                win = True
                print('ВЫИГРАЛ: ', tmp)
                break
        if count == 9:
            print('ПОБЕДИЛА ДРУЖБА')
            break