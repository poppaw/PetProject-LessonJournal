import sys
import data_operations
import gui


def main():
    while True:
        title = "Menu główne"
        menu_commands = ['wyświetl listę uczniów', 'dodaj/usuń ucznia',
                         'tygodniowy grafik zajęć', 'statystyki',
                         'terminy egzaminów',
                         'inwentarz materiałów dydaktycznych']
        gui.print_menu(title, menu_commands)
        choice = gui.choose_option(menu_commands)
        if choice == 1:
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
                         
    





if __name__ == '__main__':
    main()
