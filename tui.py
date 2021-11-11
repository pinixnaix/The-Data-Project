"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def welcome():
    message = "COVID-19 (January) Data"
    print('*' * len(message))
    print(message)
    print('*' * len(message))


def error(msg):
    print(f"Error! {msg}")


def progress(operation, value):
    if value == 0:
        print(f"{operation} has started")
    elif 0 < value < 100:
        print(f"{operation} is in progress {value}% completed")
    elif value == 100:
        print(f"{operation} has completed")


def menu(variant):
    print("Please choose one of the available options:\n")

    if variant is None or variant == 0:
        choices = [1, 2, 3, 4]
        print("[1] Process Data")
        print("[2] Visualise Data")
        print("[3] Export Data")
        print("[4] Exit")
        option = int(input())
        if option in choices:
            return option
        else:
            error("Wrong Option!!!!!")
            return None

    elif variant == 1:
        choices = [1, 2, 3, 4]
        print("[1] Record by Serial Number")
        print("[2] Records by Observation Date")
        print("[3] Group Records by Country/Region")
        print("[4] Summarise Records")
        option = int(input())
        if option in choices:
            return option
        else:
            error("Wrong Option!!!!!")
            return None

    elif variant == 2:
        choices = [1, 2, 3]
        print("[1] Country/Region Pie Chart")
        print("[2] Observations Chart")
        print("[3] Animated Summary")
        option = int(input())
        if option in choices:
            return option
        else:
            error("Wrong Option!!!!!")
            return None

    elif variant == 3:
        choices = [1, 2]
        print("[1] All Data")
        print("[2] Data for Specific Country/Region")
        option = int(input())
        if option in choices:
            return option
        else:
            error("Wrong Option!!!!!")
            return None


def total_records(num_records):
    print(f"There are {num_records} records in the data set.")


def serial_number():
    print("Please enter a serial number for a record")
    return int(input())


def observation_dates():
    """
    Task 7: Read in and return a list of observation dates.

    The function should ask the user to enter some observation dates
    This should be entered in the format dd/mm/yyyy where dd is two-digit day, mm is two digit month and yyyy is
    a four digit year e.g. 01/22/2020
    The function should return a list containing the specified observation dates.

    :return: a list of observation dates
    """
    print("Please enter some observations dates")
    print("This should be entered in the format dd/mm/yyyy")
    return [input()]


def display_record(record, cols=None):
    if len(cols) == 0 or cols is None:
        print(record)

    elif len(cols) > 0:
        value = []

        for index in cols:
            value.append(record[index])

        print(value)


def display_records(records, cols):
    if len(cols) == 0 or cols is None:
        for index in records:
            print(records[index])

    elif len(cols) > 0:
        for index in records:
            display_record(records[index], cols)
