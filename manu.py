import sys
import os


def create_options(options):
    options_values = [0 for i in range(len(options))]
    options_values[0] = 1
    return options_values

def manu_display(options, options_values):
    os.system('clear')
    print("*" * 20 + " Main manu " + "*" * 20 + "\n")
    for i in range(len(options)):
        if options_values[i] == 0:
            print(" " * 12 + "     {}".format(options[i]))
        else:
            print(" " * 12 + "-->  {}".format(options[i]))


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


def move_cursor(options, options_values):
    manu_opt = options
    end = False
    while not end:
        list_positions = options_values
        pressedkey = getch()
        position = list_positions.index(1)
        if pressedkey == 's':
            if position != len(list_positions) - 1:
                list_positions[position] = 0
                list_positions[position + 1] = 1
            else:
                list_positions[position] = 0
                list_positions[0] = 1
        elif pressedkey == 'w':
            if position != 0:
                list_positions[position] = 0
                list_positions[position - 1] = 1
            else:
                list_positions[0] = 0
                list_positions[-1] = 1
        elif pressedkey == 'q':
            end = True
            return end
        elif pressedkey == 'e':
            manu_handle(list_positions)

        manu_display(manu_opt, list_positions)
        


def creat_list_of_students(filename='students.txt'):

    with open(filename) as file_to_open:
        list_from_file = file_to_open.readlines()

    for i in range(len(list_from_file)):
        list_from_file[i] = list_from_file[i].strip("\n").split(",")

    return list_from_file


def manu_handle(list_of_positions):
    index_positions = list_of_positions.index(1)

    if index_positions == 0:
        title_list = labels()
        list_of_students = creat_list_of_students()
        display_list_of_students(list_of_students, title_list)
        stop = input("\nPress 'enter' to live: ")


def labels():
    names_of_columns = ["Student's name", "Father's name", "Mother's name", 
                        "Adress", "Phone number", "Date", "Year"]

    return names_of_columns


def display_list_of_students(list_of_students, title_list):

    model_table = [title_list]
    for element in list_of_students:
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
    print(" " + "_"*(len(list_to_print[0]) - 2) + " ")
    for line in list_to_print:
        if line == list_to_print[-1]:
            print(line)
            print("|" + "_"*(len(list_to_print[0]) - 2) + "|")
        else:
            print(line)
            print("|" + "-"*(len(list_to_print[0]) - 2) + "|")




def main():
    os.system('clear')
    options = ['Disply list of students', 'Add new student', 'Delate student', 'Exit']
    options_values = create_options(options)
    manu_display(options, options_values)
    move_cursor(options, options_values)


        





if __name__ == '__main__':
    main()