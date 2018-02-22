import gui
import data_operations

def start_module():
    
    title = "Lista uczniów"
    students_list = data_operations.make_students_list()
    quit_opt = True
    text = "Wybierz ucznia"
    gui.print_menu(title, students_list, quit_opt, add_opt)
    choice = gui.choose_option(students_list, text)
    for student in students_list:
        if choice == students_list.index(student)+1:
            title = student
            menu_commands = ['Dane ucznia', 'Oceny ucznia',
                             'Frekwencja ucznia',
                             'Przerobiony repertuar',
                             'Charakterystyka ucznia']
            gui.print_menu(title, menu_commands, quit_opt)
            choice = gui.choose_option(menu_commands)
