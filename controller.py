import model
import view
        
def open_file():
    with open('book.txt', "r", encoding="UTF-8") as data:      
        model.phonebook = data.read().split("\n")
    return model.phonebook

def start():
    open_file()
    view.print_book()
    main_menu()

def main_menu():
    while True:
        print('0 - просмотр списка')
        print('1 - добавление контакта')
        print('2 - изменение контакта')
        print('3 - удаление контакта')
        print('4 - поиск контакта')
        print('5 - сохранить файл')
        print('6 - копировать и изменить контакт')
        print('9 - выход из меню')
        choice = int(input('Выберите пункт меню: '))
        match(choice):
            case 9: 
                break
            case 0:
                view.print_book()
            case 1:
                add_contact()               
            case 2:
                change_contact()
            case 3:
                delete_contact()
            case 4:
                find_contact()
            case 5:
                with open('book.txt', "w", encoding="UTF-8") as data:
                    data.writelines('\n'.join(model.phonebook))
            case 6:
                copy_contact()

def add_contact():
    name = input('Введите имя ')
    surname = input('Введите фамилию ')
    phone_number = input('Введите телефон ')
    comment = input('Введите комментарий ')
    model.phonebook.append(name + '; ' + surname + '; ' + phone_number + '; ' + comment+ ';')
    view.print_book()

def change_contact():
    number = int(input('Введите номер контакта для изменения '))
    element = int(input('Выберите, что изменить: 0 - имя, 1 - фамилия, 2 - номер телефона, 3 - комментарий '))
    new_elem = input('Введите новое значение ')
    elem = model.phonebook.pop(number).split(';')
    elem[element] = new_elem
    model.phonebook.insert(number, '; '.join(elem))
    view.print_book()

def delete_contact():
    number = int(input('Введите номер контакта для удаления '))
    model.phonebook.pop(number)
    view.print_book()

def find_contact():
    find = input('Введите искомое значение ')
    for i in range(len(model.phonebook)):
        if find in model.phonebook[i]:
            print(model.phonebook[i])
        
def copy_contact():
    number = int(input('Введите номер контакта для копирования '))
    model.phonebook.append(model.phonebook[number])
    element = int(input('Выберите, что изменить: 0 - имя, 1 - фамилия, 2 - номер телефона, 3 - комментарий '))
    new_elem = input('Введите новое значение ')
    elem = model.phonebook.pop(-1).split(';')
    elem[element] = new_elem
    model.phonebook.insert(-1, '; '.join(elem))
    view.print_book()