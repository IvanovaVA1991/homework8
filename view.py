import controller
import model

def print_book():
    for i, item in enumerate(model.phonebook):
        print(i , item)