import gui


def import_schedule(file_name="grafik.txt"):
    """
    imports day list from txt file formatted in csv way
    -> returns sorted list of days
    """
    schedule_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            schedule_list.append(line.rstrip().split(","))
    #print (schedule_list)
    return schedule_list


def display_schedule(week_list):
    for day in week_list:
        print('\n' + day[0] + ':')
        for i in range(1,len(day)):
            print('\t' + day[i])

def make_days_list(file_name="grafik.txt"):
    """
    imports data (here: days) from txt file formatted in csv way
    -> returns sorted list of labels - first elements of listed lists (here days)
    """
    days_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            days_list.append(line.rstrip().split(",")[0])
    # print (days_list)
    return days_list


def choose_day():
    pass

def start_module():
    while True:
        week_list = import_schedule()
        display_schedule(week_list)
        decision = input("Jeśli chcesz edytować, wciśnij [enter]")
        if decision == '':
            title = "Edycja planu"
            days_list = make_days_list()
            text = "Wybierz dzień do edycji"
            gui.print_menu(title, days_list, quit_opt=True)
            choice = gui.choose_option(days_list, text)
            if choice == 1:
                pass
                #gui.print_menu("piątek", )
            elif choice == 'q':
                return False

    


def main():
    start_module()

    

if __name__ == '__main__':
    main()
