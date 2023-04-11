def add_person():
    last_name = input('Введите фамилию: ') # 'Иванов'
    name = input('Введите имя: ') # 'Иван'
    surname = input('Введите отчество: ') #'Иванович'
    phone = input('Введите номер телефона: ') #'9784561230'
    data = open('phonebook.txt', 'a', encoding='utf-8')
    data.writelines([last_name, ' ', name, ' ', surname, ' ', phone, '\n'])
    data.close()


def print_data():
    with open('D:\обучение\python\dz8\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def search():
    search_name = input('Введите данные: ')
    with open('D:\обучение\python\dz8\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

def load_data():
    with open('D:\обучение\python\dz8\phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read().splitlines()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line[:-1] not in text_data:
                    data.write(line)

def edit_data():
    search_name = input('Введите имя или фамилию для редактирования: ')
    lines_to_write = []

    with open('D:\обучение\python\dz8\phonebook.txt', 'r', encoding='utf-8') as data:
        found = False
        for line in data:
            if search_name in line:
                found = True
                print("Найден контакт:", line.strip())
                print("Введите новые данные:")
                last_name = input('Введите фамилию: ')
                name = input('Введите имя: ')
                surname = input('Введите отчество: ')
                phone = input('Введите номер телефона: ')
                lines_to_write.append(f"{last_name} {name} {surname} {phone}\n")
            else:
                lines_to_write.append(line)

        if not found:
            print("Контакт не найден.")

    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        data.writelines(lines_to_write)


def delete_data():
    search_name = input('Введите имя или фамилию для удаления: ')
    lines_to_write = []

    with open('D:\обучение\python\dz8\phonebook.txt', 'r', encoding='utf-8') as data:
        found = False
        for line in data:
            if search_name in line:
                found = True
                print("Удален контакт:", line.strip())
            else:
                lines_to_write.append(line)

        if not found:
            print("Контакт не найден.")

    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        data.writelines(lines_to_write)


def ui():
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - изменить контакт
6 - удалить контакт''')
    user_input = input('Введите нужный вариант: ')
    if user_input == '1':
        add_person()
    elif user_input == '2':
        search()
    elif user_input == '3':
        load_data()
    elif user_input == '4':
        print_data()
    elif user_input == '5':
        edit_data()
    elif user_input == '6':
        delete_data()


def main():
    ui()

if __name__ == "__main__":
    main()