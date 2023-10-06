while True:
    total = 5
    curr_answered = 0

    # 1799
    ans = int(input('Год рождения А. Пушкина? '))
    if ans == 1799:
        curr_answered += 1

    # 1814
    ans = int(input('Год рождения М. Лермонтова? '))
    if ans == 1814:
        curr_answered += 1

    # 1895
    ans = int(input('Год рождения С. Есенина? '))
    if ans == 1895:
        curr_answered += 1

    # 1812
    ans = int(input('Год рождения И. Гончарова? '))
    if ans == 1812:
        curr_answered += 1

    # 1828
    ans = int(input('Год рождения Л. Толстова? '))
    if ans == 1828:
        curr_answered += 1

    print('Количество правильных ответов: ', curr_answered)
    print('Количество ошибок: ', total - curr_answered)
    print('Процент правильных ответов: ', 100 * curr_answered / total)
    print('Процент неправильных ответов: ', 1 - curr_answered / total)

    print()
    ans = input('Начать сначала [да/нет]?')
    if ans = 'да':
        continue
    else:
        break
