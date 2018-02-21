def make_students_list(file_name="students.txt"):
    
    students_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            students_list.append(line.rstrip().split(",")[0])
    print (students_list)

    return students_list

make_students_list()
