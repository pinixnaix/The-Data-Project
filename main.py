"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

import csv
import tui
import process
import visual

covid_records = []


def run():
    tui.welcome()

    tui.progress('Data loading', 0)
    path = "data/covid_19_data.csv"
    while True:
        try:
            with open(path) as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for line in csv_reader:
                    covid_records.append(line)
                for line in covid_records:
                    line[0] = int(line[0])
                    line[5] = int(line[5])
                    line[6] = int(line[6])
                    line[7] = int(line[7])
            break

        except FileNotFoundError:
            tui.error("File not Found!!")
            path = input("Please enter the correct path for the file")
        except StopIteration:
            tui.error("File is empty!!")
            path = input("Please enter the correct path for the file")

    tui.total_records(process.records_loaded(covid_records))
    tui.progress('Data loading', 100)

    while True:

        option = tui.menu()

        if option == 1:
            tui.progress("Data processing", 0)
            variant1 = tui.menu(1)

            if variant1 == 1:
                tui.progress("Record retrieval", 0)
                record = process.retrieve_record_serial_number(covid_records)
                tui.display_record(record)
                tui.progress("Record retrieval", 100)

            elif variant1 == 2:
                tui.progress("Records retrieval", 0)
                records = process.retrieve_records_obs_dates(covid_records)
                tui.display_record(records)
                tui.progress("Records retrieval", 100)

            elif variant1 == 3:
                tui.progress("Grouping process", 0)
                records = process.retrieve_records_country_region(covid_records)
                tui.display_records(records)
                tui.progress("Grouping process", 100)

            elif variant1 == 4:
                tui.progress("Summary process", 0)
                records = process.retrieve_records_summary(covid_records)
                tui.display_records(records)
                tui.progress("summary process", 100)

            tui.progress("Data processing", 100)

        elif option == 2:
            tui.progress("Visualisation operation", 0)
            variant2 = tui.menu(2)
            if variant2 == 1:
                tui.progress("Visualisation pie chart", 0)
                visual.country_region_pie_chart(covid_records)
                tui.progress("Visualisation pie chart",100)
            if variant2 == 2:
                tui.progress("Visualisation bar chart", 0)
                visual.observation_chart(covid_records)
                tui.progress("Visualisation bar chart", 100)
            if variant2 == 3:
                tui.progress("Animated visualisation ", 0)
                visual.animated_summary(covid_records)
                tui.progress("Visualisation operation", 100)
            tui.progress("Animated visualisation", 100)

        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here

        # Task 25: Check if the user selected the option for exporting data.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve the type of data to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the data (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the records (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here

        elif option == 4:
            break

        else:
            tui.error(" Try again!!")


if __name__ == "__main__":
    run()
