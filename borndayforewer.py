while True:
    ans = int(input('Год рождения А.С Пушкина?'))
    if ans == 1799:
        while True:
            ans2 = input('День рождения А.С Пушкина?')
            if ans2 == '6 июня':
                print('Верно')
                break
            else:
                print('Неверный день рождения')
        break
    else:
        print('Неверный год рождения')

