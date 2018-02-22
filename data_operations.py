import schedule

def make_students_list(file_name="students.txt"):
    """
    imports students list from txt file formatted in csv way
    -> returns sorted list of students' names
    """
    students_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            students_list.append(line.rstrip().split(",")[0])
    # print (students_list)
    return students_list
    

def import_all_data():
    make_students_list(file_name="students.txt")
    schedule.import_schedule()




def add_student(students_list):
    new_student = input("Wpisz: Nazwisko[spacja]Imię: ")
    students_list.append(new_student)
    repertuar_list.append(new_student)
    return students_list
    # or updated_students_list = students_list.append(new_student)
    # return updated_students_list


def export_data(list_or_dict, file_name):
    with open (file_name, 'a') as f:
        pass


def make_grades_list(file_name="grades.txt"):
    """
    imports grades which each student has so far been collected
    -> returns dict of dicts of grades,
    whith name of students as a keys
    and nested dicts (pairs of 'task:rate') as values,
    i.e., grades = {'kowalski':{'czytanie':5, 'granie':4},
    'ślusarski':{'czytanie':3, 'granie':2}
    }
    """
    pass


def count_average_grade(grades, student_name):
    """
    arg1 = dict of grades
    arg2 = str of student's name
    counts average of all grades of choosen student (in a given period of time? Can we fix it??)
    ->returns float numer with the accuracy of one decimal place
    """
    return periodical_student_grades
