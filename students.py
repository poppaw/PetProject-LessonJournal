from gui import print_menu, choose_option, print_table
from data_operations import generate_list_from_txt, extract_first_element
    

def make_students_list():
    """
    imports students list from .txt file formatted in csv way
    -> returns list of students' names
    """
    students_data_list = generate_list_from_txt("students.txt")
    students_list = extract_first_element(students_data_list)
    return students_list

def start_module():
    
    title = "Lista uczniów"
    students_data_list = generate_list_from_txt("students.txt")
    students_list = make_students_list()
    #quit_opt = True
    text = "Wybierz ucznia"
    print_menu(title, students_list, quit_opt=True, add_opt=True)
    choice = choose_option(students_list, text)
    for student in students_list:
        if choice == students_list.index(student)+1:
            student_number = students_list.index(student)
            title = student
            menu_commands = ['Dane ucznia', 'Oceny bieżące ucznia',
                             'Egzaminy',
                             'Frekwencja ucznia',
                             'Przerobiony repertuar',
                             'Charakterystyka ucznia']
            print_menu(title, menu_commands, quit_opt=True)
            choice = choose_option(menu_commands)
            if choice == 1:
                category_list = ['Nazwisko i imię', 'klasa',
                                 'data urodzenia',
                                 'imiona rodziców',
                                 'adres domowy',
                                 'telefon', 'E-mail']
                print_table(students_data_list, category_list, student_number)
                    
                
