#import data_operations
import gui


def main():
    title = "Menu główne"
    menu_commands = ['wyświetl listę uczniów', 'dodaj / usuń ucznia',
                     'tygodniowy grafik zajęć', 'statystyki', 'terminy egzaminów',
                     'inwentarz materiałów dydaktycznych']
    gui.print_menu(title, menu_commands)


if __name__ == '__main__':
    main()
