# Игра на пайтон путешествие Эщкерестанца

import time
import state as s

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

running = True
while running:
    start_game = False
    print('------------------------')
    print('Меню Dark Fantasy.')
    print('1. Предыстория (Там начало игры)')
    print('2. Аккаунт')
    print('3. Ваши достижения')
    print('4. Выход')
    user_choice = int(input('Выберите пункт меню: '))

    if user_choice == 2:
        print('-----------------------')
        print('1. Зарегистрироваться (Если вы будете регестрировать новый аккаунт старый удалиться!)')
        print('2. Войти')
        user_account = int(input('Выберите пункт меню: '))
        if user_account == 1:
            f = open('txtfiles/account_info.txt', 'w', encoding='utf_8')

            account_login = input('Введите имя аккаунта (Только буквы!): ')
            accout_password = int(input('Придумайте пароль: '))
            login = f.write(f'Логин: {account_login}\n')
            password = f.write(f'Пароль: {accout_password}')
            print('Вы успешно зарегестрированы! Ваш логин и пароль сохранены в файле /txtfiles/account_info.txt')

            f.close()
        elif user_account == 2:
            account_login = input('Введите имя аккаунта: ')
            accout_password = input('Введите пароль: ')

            try:
                with open('txtfiles/account_info.txt', 'r', encoding='utf_8') as fa:
                    info = fa.read()
            except FileNotFoundError:
                print('Аккаунт не найден. Сначала зарегистрируйтесь.')
                continue

            lines = info.strip().split('\n')
            saved_login    = lines[0].replace('Логин: ', '')
            saved_password = lines[1].replace('Пароль: ', '')

            if saved_login == account_login and saved_password == accout_password:
                text = 'Добро пожаловать обратно!'
                for i in range(len(text)):
                    line = text[:i] + text[i].upper() + text[i+1:]
                    print('\r' + line, end='', flush=True)
                    time.sleep(0.1)
                print()

            else:
                print('Неправильный пароль или логин!')
    elif user_choice == 3:

        achivmient = open('.//txtfiles/achivmient.txt', 'r', encoding='utf_8')

        print('------------------------------')
        print(achivmient.read())

        achivmient.close()

    elif user_choice == 1:
            start_game = False
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            slow_print('Страна Эщкерестан это страна медных бычков, но к сожалению последние 100 лет их атакуют Джокеростан. Вы были призваны как великий герой который спасет Эщкеростан!', delay=0.05)
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            input('Нажмите Enter для продолжения')
            user4 = True
            while user4:
                user4 = False
                ready = input('Вы готовы?! (Да,нет): ')
                if ready.lower() == 'да':
                    start_game = True
                    user4 = False
                elif ready.lower() == 'нет':
                    print('Это не вопрос!')
                    user4 = True
                else:
                    print('Выбери да или нет!')
                    user4 = True
    elif user_choice == 4:
        running = False
    else:
        print('Выбери число.')

    if start_game == True:
        gold = 10
        hp = 100
        start_game = False
        print('---------------------------------------------------------------------------------------')
        slow_print('Вы появились в городе под названием - Меднобычковск - столица, страна: Эщкерестан.', delay=0.05)
        print('---------------------------------------------------------------------------------------')
        slow_print('Неизвестный (Вам): Эй! Вижу ты здесь новенький и мне кажется тебе нужно оружие и броня.', delay=0.05)
        choice1 = input('Вы пойдете с ним? (Да, нет): ')
        if choice1.lower() == 'да':
            slow_print('Вы пошли с ним', delay=0.05)
            slow_print(f'У вас {gold} монет', delay=0.05)
            print('-------------------------------------------')
            slow_print('Вы получили достижение!: Первые Гроши', delay=0.05)
            print('-------------------------------------------')
            slow_print('Все ваши достижения храняться в файле где хранится игра а сам файл тут ./путь_к_игре/txtfiles/achivmient.txt', delay=0.06)
            achivmient = open('.//txtfiles/achivmient.txt', 'a', encoding='utf-8')
            achivmient.write('Первые гроши - Получите 10 монет от хитклифа в подарок.\n')
            achivmient.close()
            slow_print('Хитклиф: Ну что вот мы и пришли вот моя кузня. И кстати мое имя Хитклиф а твоё?', delay=0.05)
            namehero = input('Ваше имя героя?: ')
            slow_print(f'Приятно познакомиться {namehero}', delay=0.05)
            slow_print('Вот мой ассортимент:', delay=0.05)
            slow_print(f'1. Меч воина - 5 монет\n2. Доспехи Воина - 5 монет\nУ вас {gold} монет', delay=0.05)
            slow_print('Хитклиф: Что будешь брать?', delay=0.05)
            userchoice = int(input('Выбери номер предмета: '))
            if userchoice == 1:
                slow_print(f'Вы приобрели меч Воина ваш остаток - {gold - 5} монет\nХитклиф: Может что-то еще?', delay=0.05)
                answer = input('Да/Нет: ')
                gold = 5
                if answer.lower() == 'да':
                    slow_print(f'Вы докупили Доспех Воина ваш остаток {gold - 5} монет', delay=0.05)
                    slow_print('Вы: Чёрт я потратил все деньги, надо бы где-то подзаробатать\nВы: О, похоже там я могу взять задание.', delay=0.05)
                    slow_print('Вы: Привет! Я хочу заработать немного.\nКвестодатель: Привет, убей парочку слабых джокеров и дам тебе 20 монет!\nНовое задание! Убить два слабых джокера', delay=0.05)
                    slow_print('Расказчик: Вы пошли за город\nНа вас сразу налетел джокер!', delay=0.05)
                    slow_print(f'Рассказчик: Фух ты смог убить его пока он тебя не убил, у тебя осталось {hp - 50} здоровья. Так продолжать нельзя', delay=0.02)
                    slow_print(f'Вы: Так стоп что-то выпало с того джокера\nВы получили фласку!', delay=0.05)
                    hp = 50
                    flaskdrink = input('Вы хотите выпить это? (Да/нет): ')
                    if flaskdrink.lower() == 'да':
                        slow_print(f'Вы выпили это. Теперь у вас {hp + 50} здоровья\nВы: Ого! Так фласка хилит на 50 здоровья', delay=0.04)
                        hp = 100
                        input('НА ВАС ОПЯТЬ НАПАЛ ДЖОКЕР ЖМИ ENTER!!!!')
                        slow_print(f'Рассказчик: Фух ты смог убить его пока он тебя не убил, у тебя осталось {hp - 10} здоровья.', delay=0.05)
                        slow_print(f'Вы: Опять что то выпало\nВы получили фласку!', delay=0.05)
                        hp = 90
                        flaskasave = input('Оставить фласку? На вас нет никаких эффектов (Да/Нет): ')
                        if flaskasave.lower() == 'да':
                            slow_print('Вы положили фласку в инвентарь.', delay=0.05)
                            inventory = input('Открыть Инвентарь? (Да/нет): ')
                            if inventory.lower() == 'да':
                                slow_print('1. Меч Воина\n2. Доспех Воина\n3. Фласка', delay=0.05)
                        if flaskasave.lower() == 'нет':
                            slow_print(f'Вы выпили фласку ваше здоровье {hp + 10}.\nИ кстати ваше макс.хп - 100\nОткрыть инвентарь?(Да/нет)', delay=0.05)
                            inventory = input('(Да/нет): ')
                            if inventory.lower() == 'да':
                                slow_print('1. Меч Воина\n2. Доспех Воина', delay=0.05)
                        slow_print(f'Задание выполнено вернитесь к квестодателю.\nВы: Фух ели смог выполнить задание.\nТак надо возврощаться пока на меня кто то еще не напал', delay=0.05)
                        gold = 20
                        slow_print(f'Вы: я вернулся вот тебе их головы жду награду.\nКвестодатель: Спасибо тебе, вот твои 20 монет.\n У вас {gold} монет', delay=0.05)
                        print('--------------------------------------------------------------')
                        slow_print('Вы получили новое достижение! - Выполните первое задание', delay=0.05)
                        print('--------------------------------------------------------------')
                        slow_print('Все ваши достижения храняться в файле где хранится игра а сам файл тут ./путь_к_игре/txtfiles/achivmient.txt', delay=0.06)
                        achivmient = open('.//txtfiles/achivmient.txt', 'a', encoding='utf-8')
                        achivmient.write('Первая подработка! - Выполните первое задание\n')
                        achivmient.close()
                        slow_print(f'У вас {gold} монет', delay=0.05)

                        money = 20
                        while True:
                            market = input('Вы хотите пойти в магазин? (Да/Нет): ')
                            if market.lower() == 'да':
                                market_level = int(input('Выберите уровень магазина.\n1. Дешёвый\n2. Средний\n3. Дорогой\nКакой выберете?: '))
                                whilee = True
                                while whilee:
                                    if market_level == 1:
                                        whilee = False
                                        market_level_menu = input('1. Оружие\n2. Броня\n3. Медикаменты\n4.Выйти из здания магазина\nВыберите категорию магазина: ')
                                        if market_level_menu == '1':
                                            status_buy = 'Куплено'
                                            print(f'--------\nОружие\n-------\n1.Ржавый нож (Обычный, цена - 8 монет, урон - 5ед. урона за удар)\n2.Деревянная бита (Обычный, цена — 10 монет, урон — 8 ед. за удар)')
                                            print(f'3.Кухонный топорик (Обычный, цена — 12 монет, урон — 10 ед. за удар)')
                                            weapon_choice1 = int(input('Выберите оружие: '))
                                            if weapon_choice1 == 1:
                                                slow_print(f'Вы купили Ржавый нож.', delay=0.05)
                                                money -= 8
                                                slow_print(f'У вас осталось {money}', delay=0.02)
                                            elif weapon_choice1 == 2:
                                                slow_print(f'Вы купили Деревянную биту.', delay=0.05)
                                                money -= 10
                                                slow_print(f'У вас осталось {money}', delay=0.02)
                                            elif weapon_choice1 == 3:
                                                slow_print(f'Вы купили Кухонный топор.', delay=0.05)
                                                money -= 12
                                                slow_print(f'У вас осталось {money}', delay=0.02)
                                            else:
                                                slow_print('Выберите цифру оружия')
                                        elif market_level_menu == '2':
                                            whilee = False
                                            slow_print('Магазин брони', delay=0.1)
                                            print(f'1.Рабочие перчатки (Обычный, цена — 4 монеты, защита — 2 ед.)\n2.Мотоциклетные наколенники (Обычный, цена — 10 монет, защита — 4 ед.)\n3.Строительная каска (Обычный, цена — 9 монет, защита — 3 ед.)')
                                            armor_choice1 = int(input('Выберите элемент брони: '))
                                            if armor_choice1 == 1:
                                                slow_print('Вы купили Рабочие перчатки.', delay=0.05)
                                                money -= 4
                                                slow_print(f'Ваш остаток монет {money}', delay=0.02)
                                            elif armor_choice1 == 2:
                                                slow_print('Вы купили Мотоциклетные наколенники.', delay=0.05)
                                                money -= 10
                                                slow_print(f'Ваш остаток монет {money}', delay=0.02)
                                            elif armor_choice1 == 3:
                                                slow_print('Вы купили Строительная каска.', delay=0.05)
                                                money -= 9
                                                slow_print(f'Ваш остаток монет {money}', delay=0.02)
                                            else:
                                                print('Выберите цифру брони.')
                                        elif market_level_menu == '3':
                                            whilee = False
                                            slow_print(f'Магазин медикаментов', delay=0.1)
                                            print(f'1.Бинт (Обычный, цена — 3 монеты, лечение — снимает кровотечение.)\n2.Активированный уголь (Обычный, цена — 2 монеты, лечение — снимает отравление желудка получение при битве)')
                                            print(f'3.Фласка (Редкий, цена - 10 монет, лечение - 50ед. HP)')
                                            medic_choice1 = int(input('Выберите медикамент: '))
                                            if medic_choice1 == 1:
                                                slow_print('Вы купили Бинт.', delay=0.05)
                                                money -= 3
                                                slow_print(f'Ваш остаток монет {money}', delay=0.02)
                                            elif medic_choice1 == 2:
                                                slow_print('Вы купили Активированый Уголь.', delay=0.05)
                                                money -= 2
                                                slow_print(f'Ваш остаток монет {money}', delay=0.02)
                                            elif medic_choice1 == 3:
                                                slow_print('Вы купили Фласку.', delay=0.05)
                                                money -= 10
                                                slow_print(f'Ваш остаток монет {money}', delay=0.02)
                                            else:
                                                print('Выберите цифру медикамента.')
                            elif market.lower() == 'нет':
                                break
                        
                        
                    elif flaskdrink.lower() == 'нет':
                        slow_print('Вы отказались пить фласку, а жаль так как вы опять умерли от кровоточения( Анлак', delay=0.02)
                elif answer.lower() == 'нет':
                    print('Нет так нет.\nВы умерли(')

            elif userchoice == 2:
                slow_print(f'Вы приобрели Доспех воина ваш остаток - {gold - 5} монет\nХитклиф: Может что-то еще?', delay=0.05)
                answer2 = input('Да/Нет: ')
                if answer2.lower() == 'да':
                    slow_print(f'Вы докупили Меч воина ваш остаток {gold - 5} монет', delay=0.05)
                elif answer2.lower() == 'нет':
                    slow_print('Вы умерли в первой драке т.к у вас были доспехи но не было оружия.', delay=0.05)

        elif choice1.lower() == 'нет':
            print('Вы не пошли с ним и умерли в первой битве без оружия.')
            print('----------')
            print('GAME OVER')
            print('----------')    