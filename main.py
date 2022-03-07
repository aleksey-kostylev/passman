from pm import PasswordManager
from myrandpass import myrandpass

def main():
        password = {}

        pm = PasswordManager()

        print("""\nДобрый день! Добро пожаловать в менеджер паролей Password Manager. Выберите необходимую опцию.

    (1) Создать новый ключ (например: token.key)
    (2) Загрузить существующий ключ
    (3) Создать новый файл с паролями (например storage.pass)
    (4) Загрузить существующий файл с паролями
    (5) Добавить новый пароль
    (6) Найти пароль
    (q) Выход
        """)

        done = False

        while not done:
            choice = input('Выберите опцию из меню: ')
            if choice == '1':
                path = input('Укажите пусть к файлу: ')
                pm.create_key(path)
            elif choice == '2':
                path = input('Укажите пусть к файлу: ')
                pm.load_key(path)
            elif choice == '3':
                path = input('Укажите пусть к файлу: ')
                pm.create_password_file(path, password)
            elif choice == '4':
                path = input('Укажите пусть к файлу: ')
                pm.load_password_file(path)
            elif choice == '5':
                site = input('Укажите название сервиса: ')
                login = input('Укажите логин: ')
                password = myrandpass() 
                pm.add_password(site, login, password)
            elif choice == '6':
                site = input('Пароль к какому сервису вам нужен: ')
                print(f'Логин и пароль для сервиса {site} это {pm.get_password(site)}')
            elif choice == 'q':
                done = True
                print('Досвидания!')
            else:
                print('Выбрана неправильная опция!')

if __name__ == '__main__':
    main()