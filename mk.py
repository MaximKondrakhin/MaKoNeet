def program():
    print('Выберите номер операции:')
    print('1 - Регистрация')
    print('2 - Мой профиль')
    print('3 - Удалить мой профиль')
    number = int(input())

    if number == 1:
            messages = []
            print('Введите ID')
            message = input()
            messages.append(message + ' ')
            print('Введите фамилию')
            message = input()
            messages.append(message + ' ')
            print('Введите имя')
            message = input()
            messages.append(message + ' ')
            print('Введите группу')
            message = input()
            messages.append(message + ' ')
            print('Введите курс')
            message = input()
            messages.append(message + ' ')
            print('Введите номер телефона')
            message = input()
            messages.append(message + ' ')
            print('Придумайте пароль')
            message = input()
            messages.append(message + '\n')
            with open('reg.txt', 'a+') as z:
                for message in messages:
                    z.write(message)
            z.close()
            program()
            
    elif number == 2:
        try: 
            with open('reg.txt', 'a+') as z:
               z.seek(0)
               global x
               x = z.read().splitlines()
               print(x)
               z.close()
        except:
            print('Данные ввыедены не корректно!!!')           
            program()

    elif number == 3:
        try:
            open('reg.txt', 'w').close()
            program()
        except:
            print('Данные ввыедены не корректно!!!')

program()