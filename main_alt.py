import sys
import os
import data_operations
import gui
import students
import schedule


def main():
    """
    inicjuje program
    wyświetla komunikat powitalny i pyta czy rozpocząć
    """
    print("Witaj w programie BELFER")
    choice = gui.choose_option(menu_commands=None, text="Wciśnij [enter] by rozpocząć, [0] by zakończyć")
    if choice == '':
        display_main_menu()
    else:
        main()


def display_main_menu():
    """
    wyświetla menu główne
    i obsługuje wybory podmenu (wywołania funkcji modułów podrzędnych)
    """
    while True:
        title = "Menu główne"
        menu_commands = ['wyświetl listę uczniów',
                         'tygodniowy grafik zajęć', 'statystyki',
                         'terminy egzaminów',
                         'inwentarz materiałów dydaktycznych']
        gui.print_menu(title, menu_commands)
        choice = gui.choose_option(menu_commands)
        if choice == 1:
            students.start_module()
        elif choice == 2:
            schedule.start_module()
        #elif choice == 3:
            #stats.start.module()
        #elif choice == 4:
            #exams.start_module()
        #elif choice == 5:
            #inventory.start_module()
        elif choice == 'q':
            return main()
            
        
            
                         
    





if __name__ == '__main__':
    main()
