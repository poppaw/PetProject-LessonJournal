import sys
import data_operations
import gui



def main():
    # while not 0: ?
    title = "Menu główne"
    menu_commands = ['wyświetl listę uczniów', 'dodaj/usuń ucznia',
                     'tygodniowy grafik zajęć', 'statystyki', 'terminy egzaminów',
                     'inwentarz materiałów dydaktycznych']
    gui.print_menu(title, menu_commands)
    choice = gui.choose_option(menu_commands)
    if choice == 1:
        title = "Lista uczniów"
        menu_commands = data_operations.make_students_list()
    gui.print_menu(title, menu_commands, True)


if __name__ == '__main__':
    main()
