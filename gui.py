import sys
import os

def print_menu(title, menu_commands, quit_opt=False, add_opt=False):
    """
    arg1: str of menu title
    arg2 : list of strings (commands)
    fruitless function displays grafical menu. 
    it works in cooperation with choose_option() function
    """
    os.system('clear')
    enumerated_commands = dict(enumerate(menu_commands, start=1))
    print('\n ', title, '(do wyboru)', ': \n')
    for number in enumerated_commands:
        print(' ', '[' + str(number) + ']', '--->', enumerated_commands[number])
    if add_opt is True:
        print(' ', '[+]', '--->', 'Dodaj pozycję')
    if quit_opt is True:
        print('\n ', '[enter]', '--->', 'Poprzednie menu')
        print('\n ', '[q]', '--->', 'Menu główne')
    print('\n ', '[0]', '--->', 'Zakończenie programu\n')
    return enumerated_commands


def choose_option(menu_commands=None, text="Wpisz numer pozycji"):
    """
    arg1: if given, should be an list object,
    arg2: str
    return: str or int value or closes application
    """
    inputed_value = input(text + ': ')
    if inputed_value == '0':
            print("Do widzenia")
            sys.exit(0)
    elif inputed_value == 'q' or inputed_value == '':
        choice = inputed_value
    elif menu_commands is True:
        if inputed_value.isdigit() and int(inputed_value) in range(1, len(menu_commands)+1):
            choice = int(inputed_value)
    else:
        print("Nie ma takiej pozycji")
        return
        
    return choice



"""def display_enumerated_students(students_list):
    enumerated_students = dict(enumerate(students_list))
    for number in enumerated_students:
        print"""




