def make_students_list(file_name="students.txt"):
    
    students_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            students_list.append(line.rstrip().split(","))
    #print (students_list)

    return students_list

#make_students_list()


def print_table(necessary_list, category_list, number):
    data_to_print = [category_list] + [necessary_list[number]]
    print (data_to_print)
    list_len_records = []
    longest_length_of_word = []
    for i in range(len(data_to_print)):
        list_len_records.append([])
        for record in data_to_print[i]:
            list_len_records[i].append(len(record))
        longest_length_of_word.append((max(list_len_records[i])))
    for index, record in enumerate(data_to_print):
        line = '|'.join(str(x).ljust(max(longest_length_of_word)) for x in record)
        if index == 0:
            print("-" * len(line))
        print(line)
        if index == 0 or index + 1 == len(data_to_print):
            print("-" * len(line))

necessary_list = make_students_list()
category_list = ['Nazwisko i imię', 'klasa', 'data urodzenia', 'imiona rodziców', 'adres domowy', 'telefon', 'E-mail']

                 
print_table(necessary_list, category_list, 1)

                 
