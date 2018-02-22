import sys

def print_menu(title, menu_commands, quit_opt=False):
    """
    arg1: str of menu title
    arg2 : list of strings (commands)
    fruitless function displays grafical menu
    """
    enumerated_commands = dict(enumerate(menu_commands, start=1))
    print(' ', title, '(do wyboru)', ': \n')
    for number in enumerated_commands:
        print(' ', number, '--->', enumerated_commands[number])
    if quit_opt is True:
        print('\n ', 'q', '--->', 'Menu główne')
    print('\n ', '0', '--->', 'Zakończenie programu\n')
    return enumerated_commands


def choose_option(menu_commands, text="Wpisz numer pozycji"):
    inputed_value = input(text + ': ')
    while inputed_value != 'q':
        if inputed_value == '0':
            print("Do widzenia")
            sys.exit(0)
        if inputed_value.isdigit() and int(inputed_value) in range(1, len(menu_commands)+1):
            choice = int(inputed_value)
            return choice
        else:
            print("Nie ma takiej pozycji")
            return choose_option(menu_commands, text="Wpisz numer pozycji")
    choice = "q"
    return choice



"""def display_enumerated_students(students_list):
    enumerated_students = dict(enumerate(students_list))
    for number in enumerated_students:
        print"""




