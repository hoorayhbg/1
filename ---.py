import random


start = input('вход платный - 10000  ')

if start == '+':
    print('оплата не прошла ')
    print("кина не будет")
    print("ладно")
    print('Если захотите закончить вводите "-".')
    print('Если захотите узнать счёт вводите "с".')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Камень, ножницы или бумага? (Вводите к, н или б): ")
        list_play = ['к', 'н', 'б']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'к' and user == 'н':
                rand_ball += 1
            if rand == 'к' and user == 'б':
                user_ball += 1
            if rand == 'н' and user == 'к':
                user_ball += 1
            if rand == 'н' and user == 'б':
                rand_ball += 1
            if rand == 'б' and user == 'н':
                user_ball += 1
            if rand == 'б' and user == 'к':
                rand_ball += 1
        elif user == 'с':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
        elif user == '-':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
            print('пока (∪.∪ )...zzz')
            break
        else:
            print('Вводите к, н или б')


if start == '-':
    print('грусняш ( *^-^)ρ(*╯^╰)')
else:
    print('придумайте где взять танки и введите "+". ')