import gui
import data_operations

def start_module():
    
    title = "Lista uczniów"
    menu_commands = data_operations.make_students_list()
    quit_opt = True
    text = "Wybierz ucznia"
    gui.print_menu(title, menu_commands, quit_opt)
    choice = gui.choose_option(menu_commands, text)
    for student in menu_commands:
        if choice == menu_commands.index(student)+1:
            title = student 
            menu_commands = ['Dane ucznia', 'Oceny ucznia',
                             'Frekwencja ucznia',
                             'Przerobiony repertuar',
                             'Charakterystyka ucznia']
            gui.print_menu(title, menu_commands, quit_opt)
            choice = gui.choose_option(menu_commands)
