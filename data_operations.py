def make_students_list(file_name=students.txt):
    """
    imports students list from txt file formatted in csv way
    -> returns sorted list of students' names
    """
    return students_list
    pass


def add_student(students_list):
    pass


def export_data(list_or_dict, file_name):
    with open (file_name, 'a') as f:
        pass


def make_grades_list(file_name="grades.txt"):
    """
    imports grades which each student has so far been collected
    -> dict of dicts of grades, whith name of students as a keys and nested dicts (pairs of 'task:rate') as values, i.e.
    grades = {'kowalski':{'czytanie':5, 'granie':4}, 
    'ślusarski':{'czytanie':3, 'granie':2}
    }
    """
    pass


def count_average_grade(grades, student_name):
    """
    arg1 = dict of grades
    arg2 = str of student's name
    counts average of all grades of choosen student (in a given period of time? Can we fix it??)
    returns float numer with the accuracy of one decimal place
    """
    return periodical_student_grades
