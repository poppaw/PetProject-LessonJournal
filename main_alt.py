import sys
import data_operations
import gui
import students
import schedule


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
            students.start_module()
        #elif choice == 2:
            #pass
        elif choice == 3:
            schedule.start_module()
        #elif choice == 4:
            #stats.start.module()
        #elif choice == 5:
            #exams.start_module()
        #elif choice == 6:
            #inventory.start_module()
        elif choice == 'q':
            main()
        
            
                         
    





if __name__ == '__main__':
    main()
