import sys
from CheckAttendanceEligibilty import AttendClass

if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
    except IndexError:
        print("Please pass 'no. of days' argument in command line. Hint: `python3 main.py 5`")
    except ValueError:
        print("Could not pass the argument for to integer. Please ensure the argument 'no. of days' is a number")
    else:
        university = AttendClass()
        print(university.ways_to_attend_classes(days))
        print(f"{university.ways_miss_graduation(days)}/{university.ways_to_attend_classes(days)}")
