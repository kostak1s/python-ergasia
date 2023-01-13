import calendar
import datetime
import csv

file = open('events.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
events = []
for x in csvreader:
        events.append(x)

is_event = []
for line in events:
    i = 0
    for date in events:
        if line[0] == date[0]:
            i += 1
    is_event.append([line[0], i])

class Month:
    def __init__(self):
        """Αντλείται το τρέχον έτος, ο μήνας και η ημέρα σε μορφή yyyy, mm, dd."""
        self.year = int(str(datetime.datetime.today()).split("-")[0])  # Τρέχον έτος.
        self.month = int(str(datetime.datetime.today()).split("-")[1])  # Τρέχον μήνας.
        self.day = int(str(datetime.datetime.today()).split("-")[2][0:2])  # Τρέχον ημέρα.


def anazitisi(current_year, current_month):
    print("=== Αναζήτηση γεγονότων ====")
    year_anaz = input("Εισάγετε έτος:")
    month_anaz = input("Εισάγετε μήνα:")
    events_anaz(year_anaz, month_anaz)
    input("Πατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:")
    calendar_(current_year, current_month)
    main_menu(current_year, current_month)


def events_anaz(year_anaz, month_anaz):
    """Η λίστα lines περιέχει κάθε event/σειρά σε ξεχωριστό string.
     Η μορφή κάθε γραμμής της λίστας lines είναι για παράδειγμα:
     2022-12-4,13:30,60,Python course και η πρώτη γραμμή δείχνει
     το τι αντιπροσωπεύει κάθε στοιχείο επόμενης γραμμής."""
    lines = events
    # Η μεταβλητή counter είναι ο αριθμός που εκτυπώνεται μπροστά
    # από το γεγονός και τα τακτοποίηση σε αριθμημένη λίστα.
    counter = -1
    i = -1
    # Μέσα απο την επανάληψη εκτυπώνονται όποια στοιχεία
    # ταιριάζουν στον χρόνο και μήνα που έχει δώσει ο χρήστης.
    for event in lines:
        i += 1
        if str(lines[i]).split("-")[0][2:] == year_anaz and str(lines[i]).split("-")[1] == month_anaz:
            counter += 1
            print(f"{counter}. [{str(lines[i]).split(',')[-1][2:-2]}] -> Date: {str(lines[i]).split(',')[0][2:-1]}, Time: {str(lines[i]).split(',')[1][2:-1]}, Duration: {str(lines[i]).split(',')[2][2:-1]}")
            if i == len(lines) - 1:  # Για να αποφευχθεί η υπερχείλιση στην λίστα.
                break


def last_month(j, current_year, current_month):
    """Εάν ο τρέχον μήνας είναι ο Ιανουάριος, τότε ο προϊγούμενος μήνας
    είναι ο Δεκέμβριος του προϊγούμενου έτους, σε οποιαδήποτε άλλη
    περίπτωση για να βρούμε τον προϊγούμενο μήνα αφαιρείται μία μονάδα
    από τον τρέχον μήνα."""
    if current_month == 1:
        if calendar.monthcalendar(current_year - 1, 12)[-1][j] != 0:
            print(f"   {calendar.monthcalendar(current_year - 1, 12)[-1][j]} |", end="")
            return last_month(j + 1, current_year, current_month)
        else:  # Για να αποφευχθούν οι άσκοπες επαναλήψεις.
            return
    else:
        if calendar.monthcalendar(current_year, current_month - 1)[-1][j] != 0:
            print(f"   {calendar.monthcalendar(current_year, current_month - 1)[-1][j]} |", end="")
            return last_month(j + 1, current_year, current_month)
        else:  # Για να αποφευχθούν οι άσκοπες επαναλήψεις.
            return


def next_month(j, current_year, current_month):
    """Εάν ο τρέχον μήνας είναι Δεκέμβριος, τότε ο προϊγούμενος μήνας
    είναι ο Ιανουάριος του προϊγούμενου έτους, σε οποιαδήποτε άλλη
    περίπτωση για να βρούμε τον προϊγούμενο μήνα προστίθεται μία μονάδα
    στον τρέχον μήνα."""
    if current_month == 12:
        if calendar.monthcalendar(current_year + 1, 1)[0][j] != 0 and j <= 5:
            print(f"    {calendar.monthcalendar(current_year + 1, 1)[0][j]} |", end="")
            return next_month(j + 1, current_year, current_month)
        elif j == 6:  # Τελευταία επανάληψη.
            print(f"    {calendar.monthcalendar(current_year + 1, 1)[0][j]}")
            return
        return next_month(j + 1, current_year, current_month)
    else:
        if calendar.monthcalendar(current_year, current_month + 1)[0][j] != 0 and j <= 5:
            print(f"    {calendar.monthcalendar(current_year, current_month + 1)[0][j]} |", end="")
            return next_month(j + 1, current_year, current_month)
        elif j == 6:  # Τελευταία επανάληψη.
            print(f"    {calendar.monthcalendar(current_year, current_month + 1)[0][j]}")
            return
        return next_month(j + 1, current_year, current_month)


# Ημερολόγιο
def calendar_(current_year, current_month):
    print(f"""
―――――――――――――――――――――――――――――――――――――――――――――――――
{months[current_month]}    {current_year}
_________________________________________________
  ΔΕΥ |  ΤΡΙ |  ΤΕΤ |  ΠΕΜ |  ΠΑΡ |  ΣΑΒ |  ΚΥΡ

""", end="")
    # Σε περίπτωση που δεν χρειάζεται να εμφανιστούν
    # οι μέρες του προϊγούμενου μήνα.
    if calendar.monthcalendar(current_year, current_month)[0][0] == 0:
        last_month(0, current_year, current_month)
    # Δείκτης που μετρά της εβδομάδες.
    i = -1
    for week in calendar.monthcalendar(current_year, current_month):
        i += 1
        # Δείκτης που μετρά της ημέρες μιας εβδομάδας.
        day_counter = 0
        for day in calendar.monthcalendar(current_year, current_month)[i]:
            day_counter += 1
            # Αν η ημέρα ανήκει στον τρέχον μήνα.
            if day != 0:
                # Η λογική μεταβλητή flag δείχνει αν η ημέρα έχει κάποιο γεγονός ή όχι.
                flag = False
                # Αν είναι η τελευταία μέρα της εβδομάδας.
                if day_counter == 7:
                    for event in is_event:
                        if event[0] == f"{current_year}-{current_month}-{day}":
                            # Υπολογισμός κενού ανάμεσα στις αγκύλες
                            # και στο νούμερο της ημέρας.
                            flag = True
                            if day < 10:
                                print(f"[ *{day}]")
                            else:
                                print(f"[*{day}]")
                            break
                    if flag == False:
                        # Υπολογισμός κενού ανάμεσα στις αγκύλες
                        # και στο νούμερο της ημέρας.
                        if day < 10:
                            print(f"[  {day}]")
                        else:
                            print(f"[ {day}]")
                else:
                    for event in is_event:
                        if event[0] == f"{current_year}-{current_month}-{day}":
                            # Υπολογισμός κενού ανάμεσα στις αγκύλες
                            # και στο νούμερο της ημέρας.
                            flag = True
                            if day < 10:
                                print(f"[ *{day}] |", end="")
                            else:
                                print(f"[*{day}] |", end="")
                    if flag == False:
                        # Υπολογισμός κενού ανάμεσα στις αγκύλες
                        # και στο νούμερο της ημέρας.
                        if day < 10:
                            print(f"[  {day}] |", end="")
                        else:
                            print(f"[ {day}] |", end="")
        # Αν δεν χρειάζεται να εμφανιστούν οι μέρες του
        # επόμενου μήνα τότε να αλλάξει σειρά.
        if calendar.monthcalendar(current_year, current_month)[i][-1] != 0:
            print("\n")
    # Σε περίπτωση που δεν χρειάζεται να εμφανιστούν
    # οι μέρες του επόμενου μήνα.
    if calendar.monthcalendar(current_year, current_month)[-1][-1] == 0:
        next_month(0, current_year, current_month)


# Κυρίως μενού
def main_menu(current_year, current_month):
    print("""
_________________________________________________
Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις
παρακάτω επιλογές:
    "-" για πλοήγηση στον προηγούμενο μήνα
    "+" για διαχείριση των γεγονότων του ημερολογίου
    "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα""")
    answer = input("    -> ")
    if answer == "q":
        quit()
    elif answer == "":  # Αν η απάντηση του χρήστη είναι ENTER.
        # Αν ο τρέχον μήνας είναι ο Δεκέμβριος, τότε ο επόμενος
        # μήνας θα είναι ο Ιανουάριος του επόμενου έτους.
        if current_month == 12:
            calendar_(current_year + 1, 1)
            main_menu(current_year + 1, 1)
        else:  # Αλλιώς προστίθεται μία μονάδα στον τρέχον μήνα.
            calendar_(current_year, current_month + 1)
            main_menu(current_year, current_month + 1)
    elif answer == "-":
        # Αν ο τρέχον μήνας είναι ο Ιανουάριος, τότε ο προϊγούμενου
        # μήνας είναι ο Δεκέμβριος του προϊγούμενου έτους.
        if current_month == 1:
            calendar_(current_year - 1, 12)
            main_menu(current_year - 1, 12)
        else:  # Αλλιώς αφαιρείται μία μονάδα από τον τρέχον μήνα.
            calendar_(current_year, current_month - 1)
            main_menu(current_year, current_month - 1)
    elif answer == "*":
        anazitisi(current_year, current_month)
    elif answer == "+":
        opt_managment()
    else:
        calendar_(current_year, current_month)
        main_menu(current_year, current_month)


def opt_managment():
    """ Τλοποιεί το μενού διαχείρισης γεγονότων με έλεγχο εγκυρότητας ώστε να επιλέγεται σωστή επιλογή"""    
    print('----------------------------------------------------')
    print('\033[1m' + 'Διαχείριση γεγονότων ημερολογίου,' + '\033[0m', 'επιλέξτε ενέργεια')
    opt_1 = '1 Καταγραφή νέου γεγονότος'
    opt_2 = '2 Διαγραφή γεγονότος'
    opt_3 = '3 Ενημέρωση γεγονότος'
    opt_0 = '0 Επιστροφή στο κυρίως μενού' 
    error_messenge =  'Δώσατε λανθασμένη ενέργεια. Παρακαλώ επιλέξτε ενέργεια'
    while True:
        selection = input(opt_1 + '\n' + opt_2 + '\n' + opt_3 + '\n' + opt_0 + '\n' + '->')
        if selection == '0':
            opt0()
        elif selection == '1':
            opt1()
        elif selection == '2': 
            opt2()
        elif selection == '3':
            opt3()
        else:
            print(error_messenge)


def date_inp():
    """Εισάγει με έλεγχο εγκυρότητας ημερομηνία από τον χρήστη ώστε να είναι πραγματική ημερομηνία και το έτος 
    να είναι μεγαλύτερο του 2022, σε μορφή ΥΥΥΥ-ΜΜ-DD """
    while True:
        valid = True
        error_messenge = 'Δώσατε λανθασμένη ημερομηνία.'
        date = input('Δώσε ημερομηνία γεγονότος σε μορφή ΥΥΥΥ-ΜΜ-DD' + '\n' + '->')
        if date[0:3].isdigit() == True and date[4] == date[7] == '-' and date[5:6].isdigit() and date[-2:].isdigit:
            year,month,day = date.split('-')  # Χωρίζει το string όταν υπάρχει παύλα
            year,month,day = int(year), int(month), int(day),
            if year > 2022:
                try:
                    datetime.datetime(year,month,day)  # Ελέγχει αν η ημερομηνία είναι πραγματική
                except ValueError :                    # Εαν η ημερομηνία δεν είναι πραγματική (περίπτωση ValueError)
                    valid = False                      # κάνει την τιμή της 'σημαίας' valid False
            else:
                valid = False
        else:
            valid = False
        if valid:
            return(date)
        else:
            print(error_messenge)

def time_inp():
    """Εισάγει με έλεγχο εγκυρότητας ημερομηνία από τον χρήστη ώστε να είναι πραγματική ώρα γεγονότος, σε μορφή HH:MM """
    error_messenge = 'Δώσατε λανθασμένη ώρα.'
    while True:
        time = input('Δώστε ώρα γεγονότος σε μορφή HH:MM' + '\n' + '->')
        if time[0:1].isdigit() == time[3:4].isdigit() == True and time[2] == ':':
            hour , minute = time.split(':')
            hour , minute = int(hour) , int(minute)
            if hour in range(24) and minute in range(60): # Έλεγχει αν η ώρα λαμβάνει τιμές 0-23 και τα λεπτά τιμές 0-59
                return time
            else:
                print(error_messenge)
        else:
            print(error_messenge)


def duration_inp():
    error_messenge = 'Δώσατε λανθασμένη διάρκεια.'
    while True:
        duration = input('Δώστε διάρκεια γεγονότος' + '\n' + '->')
        if duration.isdigit():
            duration = int(duration)
            if duration > 0:
                return duration
            else:
                print(error_messenge)
        else:
            print(error_messenge)


def title_inp():
    """Εισάγει το τίτλος γεγονότος με έλεγχο εγκυρότητας ώστε να είναι string και να μην περιέχει το χαρακτήρα ,"""
    error_messenge = 'Δώσατε λανθασμένο τίτλο.'
    while True:
        title = input('Δώστε τίτλο γεγονότος' + '\n' + '->')
        if ',' not in title:
            return title
        else:
            print(error_messenge)


def opt1():
    """Υλοποιεί την επιλόγη 1 με την βοήθεια των συναρτήσεων date_inp, time_inp, duration_inp, title_inp.
    Δηλαδή ζητά διαδοχικά όλα τα στοιχεία ενός νέου γεγονότος, θα δημιουργεί το γεγονός και θα το προσθέτει στη λίστα των γεγονότων.
    Στο τέλος επιστρέφει στο μενού διαχείρισης γεγονότων."""
    date = date_inp()
    time = time_inp()
    duration = duration_inp()
    title = title_inp()
    events.append([date, time, duration, title])
    for event in is_event:
        if date != event[0]:
            is_event.append([date, 1])
        else:
            for event in is_event:
                if is_event[0] == date:
                    is_event[event] = [date, is_event[1] + 1]
                    break
    opt_managment()


def events_search(year_anaz, month_anaz):
    """Η λίστα lines περιέχει κάθε event/σειρά σε ξεχωριστό string.
     Η μορφή κάθε γραμμής της λίστας lines είναι για παράδειγμα:
     2022-12-4,13:30,60,Python course και η πρώτη γραμμή δείχνει
     το τι αντιπροσωπεύει κάθε στοιχείο επόμενης γραμμής."""
    lines = events
    # Η λίστα ls περιλαμβάνει όλα τα events που πληρούν τα κριτήρια της αναζήτησης
    ls = []
    # Η μεταβλητή counter είναι ο αριθμός που εκτυπώνεται μπροστά
    # από το γεγονός και τα τακτοποίηση σε αριθμημένη λίστα.
    counter = -1
    i = -1
    # Μέσα απο την επανάληψη εκτυπώνονται όποια στοιχεία
    # ταιριάζουν στον χρόνο και μήνα που έχει δώσει ο χρήστης.
    for event in lines:
        i += 1
        if str(lines[i]).split("-")[0][2:] == year_anaz and str(lines[i]).split("-")[1] == month_anaz:
            counter += 1
            ls.append(events[i])
            print(f"{counter}. [{str(lines[i]).split(',')[-1][2:-2]}] -> Date: {str(lines[i]).split(',')[0][2:-1]}, Time: {str(lines[i]).split(',')[1][2:-1]}, Duration: {str(lines[i]).split(',')[2][2:-1]}")
            if i == len(lines) - 1:  # Για να αποφευχθεί η υπερχείλιση στην λίστα.
                break
    return ls


def month_inp():
    """Εισάγεται o μήνας του γεγονότος προς διαγραφή με έλεγχο εγκυρότητας ωστε να είναι ακέραιος και 1<=month<=12"""
    error_messenge = 'Δώσατε λανθασμένο μήνα γεγονότος προς διαγραφή.'
    month = input('Δώστε μήνα γεγονότος προς διαγραφή.' + '\n' + '->')
    if month.isdigit():
        month = int(month)
        if month in range(1,13):
            return month
        else:
            print(error_messenge)
    else:
        print(error_messenge)


def year_inp():
    """Εισάγεται το έτος του γεγονότος προς διαγραφή με έλεγχο εγκυρότητας 'ωστε να είναι ακέραιος μεγαλύτερος του 2022"""
    error_messenge = 'Δώσατε λανθασμένο έτος γεγονότος προς διαγραφή.'
    while True:
        year = input('Δώστε έτος γεγονότος προς διαγραφή.' + '\n' + '->')
        if year.isdigit():
            year = int(year)
            if year > 2022:
                return year
            else:
                print(error_messenge)
        else:
            print(error_messenge)


def opt2():
    """ Υλοποιεί την επιλόγη 2 με την βοήθεια των συναρτήσεων year_inp, month_inp, events_search. Γίνεται είσοδος έγκυρου έτους 
    και μήνα από το χρήστη και στην συνέχεια γίνεται αναζήτηση γεγονότων με βάση συγκεκριμένο μήνα όπου  εμφανίζεται αριθμημένη
    λίστα με τα γεγονότα του μήνα έπειτα ο χρήστης καλείται να δώσει τον αριθμό του γεγονότος προς διαγραφή."""
    
    if len(events) > 0:  # Ελέχει εάν υπάρχουν γεγονότα καταχωρημένα
        year = year_inp()  
        month = month_inp()
        month_events = events_search(year, month)
        flag = len(month_events)
        if flag > 0:  # Ελέχει εάν υπάρχουν γεγονότα καταχωρημένα για τον μήνα
            error_messenge = 'Δώσατε λανθασμένο αριθμό γεγονότος προς διαγραφή.'
            while True:
                key = input('Δώστε αριθμό γεγονότος προς διαγραφή')
                if key.isdigit():
                    key = int(key)
                    if key >= 0 and key <= flag:
                        events.remove(month_events[key])
                        date = month_events[key][0]
                        for event in is_event:
                            if is_event[0] == date:
                                is_event[event] = [date, is_event[1] - 1]
                                if is_event[1] == 0:
                                    is_event.remove(event)
                                break
                        break
                    else:
                        print(error_messenge)
                else:
                    print(error_messenge)
        else:
            print('Δεν υπάρχει κανένα γεγονός καταχωρημένο τον μήνα που επιλέξατε.')                
    else:
        print('Δεν υπάρχει κανένα γεγονός καταχωρημένο.')
    opt_managment()


def opt3():
    """ Υλοποιεί την επιλόγη 2 με την βοήθεια των συναρτήσεων year_inp, month_inp, change_date, change_time, change_duration,change_title.
    Γίνεται είσοδος έγκυρου έτους και μήνα από το χρήστη και στην συνέχεια γίνεται αναζήτηση γεγονότων με βάση συγκεκριμένο μήνα όπου  
    εμφανίζεται αριθμημένη λίστα με τα γεγονότα του μήνα έπειτα ο χρήστης καλείται να δώσει τον αριθμό του γεγονότος προς ενημέρωση.
    Έπειτα ζητείται η νέα τιμή του κάθε στοιχείου. Αν δεν εισαχθεί κάποια τιμή τότε διατηρείται η αρχική."""

    def change_date(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο μια νέα ημερομηνία για το γεγονός"""
        
        while True:
            valid = True
            error_messenge = 'Δώσατε λανθασμένη ημερομηνία.'
            date = input('\n' + 'Ημερομηνία γεγονότος '+ '(' + str(ls[0]) + '):')
            if date == '':
                return ls[0]
            elif date[0:3].isdigit() == True and date[4] == date[7] == '-' and date[5:6].isdigit() and date[-2:].isdigit:
                year,month,day = date.split('-')  # Χωρίζει το string όταν υπάρχει παύλα
                year,month,day = int(year), int(month), int(day)
                if year > 2022:
                    try:
                        datetime.datetime(year,month,day)  # Ελέγχει αν η ημερομηνία είναι πραγματική
                    except ValueError:                     # Εαν η ημερομηνία δεν είναι πραγματική (περίοπτωση ValueError)
                        valid = False                      # κάνει την τιμή της 'σημαίας' valid False
                else:
                    valid = False
            else:
                valid = False
            if valid:
                return(date)
            else:
                print(error_messenge)
    
    def change_time(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο μια νέα ώρα για το γεγονός"""
        
        error_messenge = 'Δώσατε λανθασμένη ώρα.'
        while True:
            time = input('Ώρα γεγονότος '+ '(' + str(ls[1]) + '):')
            if time == '':
                return ls[1]
            elif time[0:1].isdigit() == time[3:4].isdigit() == True and time[2] == ':':
                hour , minute = time.split(':')
                hour , minute = int(hour), int(minute)
                if hour in range(24) and minute in range(60):
                    return time
                else:
                    print(error_messenge)
            else:
                print(error_messenge)

    def change_duration(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο μια νέα διάρκεια για το γεγονός"""
        
        error_messenge = 'Δώσατε λανθασμένη διάρκεια.'
        while True:
            duration = input('Διάρκεια γεγονότος '+ '(' + str(ls[2]) + '):')
            if duration == '':
                return ls[2]
            elif duration.isdigit():
                duration = int(duration)
                if duration > 0:
                    return duration
                else:
                    print(error_messenge)
            else:
                print(error_messenge)

    def change_title(ls):
        """Δέχεται σαν είδοδο ένα γεγονός σε μορφή λίστας και δίνει ως έξοδο ένα νέο τίτλο για το γεγονός"""

        error_messenge = 'Δώσατε λανθασμένο τίτλο.'
        while True:
            title = input('Τίτλος γεγονότος '+ '(' + ls[3] + '):')
            if title == '':
                return ls[3]
            elif ',' not in title:
               return title
            else:
                print(error_messenge)

    year = year_inp()
    month = month_inp()
    if len(events) > 0:
        month_events = events_search(year,month)
        flag = len(month_events)
        if flag > 0:
            error_messenge = 'Δώσατε λανθασμένο αριθμό γεγονότος προς ενημέρωση.'
            while True:
                key = input('Επιλέξτε γεγονός προς ενημέρωση:')
                if key.isdigit():
                    key = int(key)
                    if key >= 0 and key <= flag:
                        events.remove(month_events[key])
                        date = month_events[key][0]
                        for event in is_event:
                            if is_event[0] == date:
                                is_event[event] = [date, is_event[1] - 1]
                                if is_event[1] == 0:
                                    is_event.remove(event)
                                break
                        event = month_events[key]
                        new_date = change_date(event)
                        event[0] = new_date
                        new_time = change_time(event)
                        event[1] = new_time
                        new_duration = change_duration(event)
                        event[2] = new_duration
                        new_title = change_title(event)
                        event[3] = new_title
                        events.append(event)
                        if date not in is_event:
                            is_event.append([date, 1])
                        else:
                            for event in is_event:
                                if is_event[0] == date:
                                    is_event[event] = [date, is_event[1] + 1]
                                    break 
                        break
                    else:
                        print(error_messenge)
                else:
                    print(error_messenge)
            print('\n' + '\n' + 'Το γεγονός ενημερώθηκε: <['+ new_title +'] -> Date: ' + new_date + ', Time: ' + new_time + ', Duration: ' + new_duration)
    opt_managment()


def opt0():
    """Υλοποιεί την επιλογή 0, δηλαδή επιστρέφει στο κυρίως μενού της εφαρμογής, με προβολή του μήνα που
    εμφανιζόταν πριν την ενεργοποίηση της επιλογής (+) για διαχείριση γεγονότων."""
    main()


def main():
    current_year = month.year  # Τρέχον χρόνος.
    current_month = month.month  # Τρέχον μήνας.
    calendar_(current_year, current_month)
    main_menu(current_year, current_month)


month = Month()
# Λεξικό το οποίο μετατρέπει το νούμερο του
# μήνα στα πρώτα τρία-τέσσερα γράμματά του.
months = {
    1: "ΙΑΝ",
    2: "ΦΕΒ",
    3: "ΜΑΡ",
    4: "ΑΠΡ",
    5: "ΜΑΪ",
    6: "ΙΟΥΝ",
    7: "ΙΟΥΛ",
    8: "ΑΥΓ",
    9: "ΣΕΠ",
    10: "ΟΚΤ",
    11: "ΝΟΕ",
    12: "ΔΕΚ"
}

if __name__ == "__main__":
    main()
