import sys
import os
from termcolor import colored


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def position(coordinate, list_length):
    
    key_pressed = getch()
    position = coordinate
    
    if key_pressed == 's':
        if position == list_length - 1:
            position = 0
        else:
            position += 1
    elif key_pressed == 'w':
        if position == 0:
            position = list_length -1
        else:
            position -= 1
    elif key_pressed == 'q':
        sys.exit(0)
    elif key_pressed == 'e':
        return 'e'

    return position


def display_manu(options, index, title="Main"):
    os.system('clear')
    print("*" * 20 + title + " manu " + "*" * 20 + "\n")
    
    for i in range(len(options)):
        if i == index:
            line = colored(" " * 12 + "-->  {}".format(options[i]), 'blue')
            print(line)
        else:
            print(" " * 12 + "     {}".format(options[i]))

    return index


def manu_use():
    index = 0
    options = main_manu_options()
    length_of_option_list = len(options)
    
    while index != 'e':
        coordinate = display_manu(options, index)
        index = position(coordinate, length_of_option_list)

    return coordinate


def student_manu_use():
    index = 0
    options = student_options_manu()
    length_of_option_list = len(options)
    
    while index != 'e':
        coordinate = display_manu(options, index, "Students's")
        index = position(coordinate, length_of_option_list)

    return coordinate



def main_manu_options():

    options = ['Display list of students', 
               'Add or romove student', 
               'Show week schedule', 
               'Statistics', 
               'Anual exams',
               'Inventory of didactic materials']

    return options


def student_options_manu():

    options = ["Main information about student",
               "List of student's degrees",
               "Student's attendance",
               "Repertoire reworked",
               "Studen's profile",
               "Quit"]

    return options

def create_list_from_file(filename):

    with open(filename) as file_to_open:
        list_from_file = file_to_open.readlines()

    for i in range(len(list_from_file)):
        list_from_file[i] = list_from_file[i].strip("\n").split(",")

    return list_from_file


def labels(number):
    names_of_columns = [["Student's name", "Class", "Date of birth",
                         "Parent's name", "Adress", "Phone", "E-mail"],
                        ["Student's name", "Reading", "Gama", "Etude", "Memory playing"],
                        ["Week", "Mon", "Tue", "Wed", "Thur", "Fri"]]

    return names_of_columns[number]



def display_table(list_of_lists, title_list, index):
    os.system('clear')
    model_table = [title_list]
    for element in list_of_lists:
        model_table.append(element)

    column_sizes = [0] * len(title_list)

    for list_ in model_table:
        i = 0
        for element in list_:
            if len(element) > column_sizes[i]:
                column_sizes[i] = len(element)
            i += 1


    string = "|"
    for number in column_sizes:
        string += " {:^" + str(number) + "} |"
    list_to_print = list()
    for line in model_table:
        list_to_print.append(string.format(*line))

    print(" " * 9 + "_"*(len(list_to_print[0]) - 2) + " ")
    
    for i in range(len(list_to_print)):
        if i == len(list_to_print) - 1:
            if i == index:
                print("-->" + " " * 5 + list_to_print[i])
                print(" " * 8 + "|" + "_"*(len(list_to_print[0]) - 2) + "|")
            else:
                print(" " * 8 + list_to_print[i])
                print(" " * 8 + "|" + "_"*(len(list_to_print[0]) - 2) + "|")
        elif i == index and index == 0:
            index = 1
            print(" " * 8 + list_to_print[i])
            print(" " * 8 + "|" + "-"*(len(list_to_print[0]) - 2) + "|")
        else:
            if i == index:
                print("-->" + " " * 5 + list_to_print[i])
                print(" " * 8 + "|" + "-"*(len(list_to_print[0]) - 2) + "|")
            else:
                print(" " * 8 + list_to_print[i])
                print(" " * 8 + "|" + "-"*(len(list_to_print[0]) - 2) + "|")

    return index

def use_table(filename, number):
    index = 1
    title_list = labels(number)
    list_of_lists = create_list_from_file(filename)
    length_of_table = len(list_of_lists) + 1
    while index != 'e':
        coordinate = display_table(list_of_lists, title_list, index)
        index = position(coordinate, length_of_table)

    return coordinate - 1


def choose_element_from_list(list_, index):

    row = list_[index]

    return row


def export_to_file(table, filename, mode='w'):

    with open(filename, mode) as file_to_open:
        
        for i in range(len(table)):
            table[i] = ",".join(table[i])
            file_to_open.write(table[i] + "\n")


def change_element(row_index, number, filesname):

    table = create_list_from_file(filesname)
    row_from_table = table[row_index]
    max_row_indexes = len(row_from_table)
    corect_input = False
    while not corect_input:
        try:
            which_element_to_change = input("Enter number of element you want to change "
                                + "(1-" + str(max_row_indexes) + ")" + " or 'q' to exit: ")
            if which_element_to_change == 'q':
                corect_input = True
                return corect_input
            else:
                element_index = int(which_element_to_change) -1
                change_data = input("Please enter new data: ")
                row_from_table[element_index] = change_data
                table[row_index] = row_from_table
                export_to_file(table, filesname)
                os.system('clear')
                title_list = labels(number)
                display_table([row_from_table], title_list, 0)
            
        except:
            print("Only numbers in scope please!")


def attendance_table(number):
    headlines = labels(2)

    table = []

    for i in range(number):
        table.append(["-"] * len(headlines))

    return table


def add_rows(name_of_student):
    amount = int(input("Enter number of rows: "))
    rows = attendance_table(amount)
    export_to_file(rows, name_of_student + ".txt", 'a')


def export(list_, filename, mode='a'):
    
    with open(filename, mode) as file_to_write:
        line = ",".join(list_)
        file_to_write.write(line + "\n")



def attendance_check(name_of_student):
    ask = input("Display attendance table (d) or edit to make change (e): ")
    if ask == 'd':
        headlines = labels(2)
        try:
            table = create_list_from_file(name_of_student + ".txt")
            display_table(table, headlines, 0)
        except:
            print("File is empty or doesn't exist. Creat it by adding some rows.")
        info = input("To see information about student's presence press 'x' else press enter: ")
        if info == 'x':
            attendance_count(name_of_student)
            stop = input("To leave press enter: ")
    elif ask == 'e':
        ask_about_rows = input("For adding more rows enter 'a' else 'enter': ")
        if ask_about_rows == 'a':
            add_rows(name_of_student)
            print("New rows has been added.")
        else:
            corect_input = False
            while not corect_input:
                headlines = labels(2)
                table = create_list_from_file(name_of_student + ".txt")
                row_index = use_table(name_of_student + ".txt", 2)
                max_table_index = len(headlines)
                try:
                    which_element_to_change = input("Enter number of element you want to change "
                                        + "(1-" + str(max_table_index) + ")" + " or 'q' to exit: ")
                    if which_element_to_change == 'q':
                        corect_input = True
                        return corect_input
                    else:
                        element_index = int(which_element_to_change) -1
                        change_data = input("Please enter new data: ")
                        table[row_index][element_index] = change_data
                        export_to_file(table, name_of_student + ".txt", 'w')
                        new_table = create_list_from_file(name_of_student + ".txt")
                        display_table(new_table, headlines, 0)
                except:
                    print("Only numbers in scope please!")


def average_grades(list_):

    list_of_grades = []
    for element in list_:
        one_student = []
        for i in range(len(element)):
            if i == 0:
                one_student.append(element[i])
            else:
                one_student.append(float(element[i]))
        list_of_grades.append(one_student)

    student_avg_grades = []
    for element in list_of_grades:
        student = [element[0], sum(element[1:])/(len(element) - 1)]
        student_avg_grades.append(student)

    return student_avg_grades


def attendance_count(name_of_student):

    list_of_attendance = create_list_from_file(name_of_student + ".txt")
    absence = 0
    presence = 0
    for element in list_of_attendance:
        presence += element.count('x')
        absence += element.count('*')

    average_presence = round((presence/(presence + absence)) * 100, 2)

    print(name_of_student + ": presence: " + str(presence) + 
         " absence: " + str(absence) + " average: " + str(average_presence) + "%")


def add_to_list(list_of_lists, element, index):

    list_of_repertoire = list_of_lists
    for i in range(len(list_of_repertoire)):
        if i == index:
            list_of_repertoire[i].append(element)
        else:
            list_of_repertoire[i].append("?")

    return list_of_repertoire





def submenus(choose):
    if choose == 0:
        row_index = use_table('students.txt', 0)
        list_ = create_list_from_file('students.txt')
        name_of_student = list_[row_index][0]
        chosen_student = choose_element_from_list(list_, row_index)
        length_of_row = len(chosen_student)
        end = False
        while not end:
            manu_position = student_manu_use()
            if manu_position == 0:
                title_list = labels(0)
                display_table([chosen_student], title_list, 0)
                change_element(row_index, 0, 'students.txt')
            elif manu_position == 1:
                headlines = labels(1)
                grade_list = create_list_from_file('grades_seb.txt')
                row_from_grade_list = grade_list[row_index]
                display_table([row_from_grade_list], headlines, 0)
                change_element(row_index, 1, 'grades_seb.txt')
                ask = input("If you want to see student's grade's average press 'x' else press enter: ")
                if ask == 'x':
                    list_of_grades = create_list_from_file('grades_seb.txt')
                    avg_list = average_grades(list_of_grades)
                    students_avg = avg_list[row_index]
                    print(name_of_student + ": average grade: " + str(students_avg))
                    stop = input("Press enter to leave: ")
            elif manu_position == 2:
                attendance_check(name_of_student)
            elif manu_position == 3:
                leave = False
                while not leave:
                    list_of_students_rep = create_list_from_file('repertuar.txt')
                    headlines = ['#'] * len(list_of_students_rep[0])
                    display_table(list_of_students_rep, headlines, 0)
                    ask = input("If you want to add more repertoire press 'x' elss press enter: ")
                    if ask == 'x':
                        element = input("Type repertoire you want to add: ")
                        new_list = add_to_list(list_of_students_rep, element, row_index)
                        export_to_file(new_list, 'repertuar.txt')
                    else:
                        leave = True

            elif manu_position == 5:
                end = True







def main():
    while True:
        choose = manu_use()
        submenus(choose)
    
    






if __name__ == '__main__':
    main()

