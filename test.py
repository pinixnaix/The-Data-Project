import csv
import tui

covid_records = []
path = "data/covid_1_data.csv"

while True:
    try:
        with open(path) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for line in csv_reader:
                covid_records.append(line)
        break
    except FileNotFoundError:
        tui.error("File not Found!!")
        path = input("Please enter the correct path for the file")
    except StopIteration:
        tui.error("File is empty!!")
        path = input("Please enter the correct path for the file")

tui.total_records(len(covid_records))
tui.progress('Data loading', 100)