# 1 Числовая угадайка

from random import randint

print('Добро пожаловать в числовую угадайку')


def is_valid(number):
    return number.isdigit() and int(number) in range(1, 101)


def is_game():
    n = randint(1, 100)
    count = 1
    while True:
        print()
        print('Введите число от 1 до 100 (включительно):')
        num = input()
        if not is_valid(num):
            print('А может быть все-таки введем целое число от 1 до 100?')
        else:
            num = int(num)
            if num < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
                continue
            if num > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
                continue
            else:
                print('Вы угадали, поздравляем! Для этого вам потребовалось', count, 'попытка(ок)')
                break


def is_repeat_game():
    while True:
        print('Сыграем ещё разок?', 'Ответьте "ДА" или "НЕТ"', sep='\n')
        answer = input()
        if answer.upper() == 'ДА':
            is_game()
        if answer.upper() == 'НЕТ':
            break
        else:
            print('Я не понимаю Ваш ответ, ответьте еще раз')
            continue


is_game()
is_repeat_game()