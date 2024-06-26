import os

# Путь к файлу справочника
FILE_PATH = 'phonebook.txt'

def load_phonebook():
    phonebook = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            for line in file:
                phonebook.append(line.strip().split(', '))
    return phonebook

def save_phonebook(phonebook):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(', '.join(entry) + '\n')

def display_phonebook(phonebook):
    for entry in phonebook:
        print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}")

def add_entry(phonebook):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    phonebook.append([surname, name, patronymic, phone])

def search_entry(phonebook):
    search_term = input("Введите имя или фамилию для поиска: ")
    for entry in phonebook:
        if search_term in entry:
            print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}")

def update_entry(phonebook):
    search_term = input("Введите имя или фамилию для обновления записи: ")
    for entry in phonebook:
        if search_term in entry:
            print(f"Найденная запись: Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}")
            surname = input("Введите новую фамилию (оставьте пустым для пропуска): ") or entry[0]
            name = input("Введите новое имя (оставьте пустым для пропуска): ") or entry[1]
            patronymic = input("Введите новое отчество (оставьте пустым для пропуска): ") or entry[2]
            phone = input("Введите новый номер телефона (оставьте пустым для пропуска): ") or entry[3]
            entry[:] = [surname, name, patronymic, phone]
            print("Запись обновлена.")
            return

def delete_entry(phonebook):
    search_term = input("Введите имя или фамилию для удаления записи: ")
    for entry in phonebook:
        if search_term in entry:
            phonebook.remove(entry)
            print("Запись удалена.")
            return

def main():
    phonebook = load_phonebook()
    while True:
        print("\nВыберите необхлдимое действие")
        print("1. Показать все записи")
        print("2. Добавить запись")
        print("3. Найти запись")
        print("4. Обновить запись")
        print("5. Удалить запись")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            display_phonebook(phonebook)
        elif choice == '2':
            add_entry(phonebook)
            save_phonebook(phonebook)
        elif choice == '3':
            search_entry(phonebook)
        elif choice == '4':
            update_entry(phonebook)
            save_phonebook(phonebook)
        elif choice == '5':
            delete_entry(phonebook)
            save_phonebook(phonebook)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
