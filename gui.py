def print_menu(title, menu_commands, quit_opt=False):
    """
    arg1: str of menu title
    arg2 : list of commends
    function displays grafical menu
    """
    enumerated_commands = dict(enumerate(menu_commands))
    print(' ', title, '(wybierz z listy)', ': \n')
    for number in enumerated_commands:
        print(' ', number, '--->', enumerated_commands[number])
    if quit_opt is True:
        print(' ', 'q', '--->', 'Menu główne')



def choose_option(input_number):

    pass

def display_enumerated_students(students_list):
    enumerated_students = dict(enumerate(students_list))
    for number in enumerated_students:
        print




