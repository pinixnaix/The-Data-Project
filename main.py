"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""
# Task 10: Import required modules
import csv
import tui
import process
import visual

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
covid_records = []


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    tui.progress('Data loading', 0)
    path = "data/covid_19_data.csv"

    # Task 14: Using the appropriate function in the module 'tui', display a menu of options
    # for the different operations that can be performed on the data (menu variant 0).
    # Assign the selected option to a suitable local variable
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
            path = tui.path()
        except StopIteration:
            tui.error("File is empty!!")
            path = tui.path()

    tui.total_records(process.records_loaded(covid_records))
    tui.progress('Data loading', 100)

    # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
    # - Use the appropriate function in the module tui to display a message to indicate that the data processing
    # operation has started.
    # - Process the data (see below).
    # - Use the appropriate function in the module tui to display a message to indicate that the data processing
    # operation has completed.
    #
    # To process the data, do the following:
    # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
    # (menu variant 1).
    # - Check what option has been selected
    #
    #   - If the user selected the option to retrieve an individual record by serial number then
    #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
    #       has started.
    #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
    #       display it.
    #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
    #       completed.
    #
    #   - If the user selected the option to retrieve (multiple) records by observation dates then
    #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
    #       process has started.
    #       - Use the appropriate function in the module 'process' to retrieve records with
    #       - Use the appropriate function in the module 'tui' to display the retrieved records.
    #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
    #       process has completed.
    #
    #   - If the user selected the option to group records by country/region then
    #       - Use the appropriate function in the module 'tui' to indicate that the grouping
    #       process has started.
    #       - Use the appropriate function in the module 'process' to group the records
    #       - Use the appropriate function in the module 'tui' to display the groupings.
    #       - Use the appropriate function in the module 'tui' to indicate that the grouping
    #       process has completed.
    #
    #   - If the user selected the option to summarise the records then
    #       - Use the appropriate function in the module 'tui' to indicate that the summary
    #       process has started.
    #       - Use the appropriate function in the module 'process' to summarise the records.
    #       - Use the appropriate function in the module 'tui' to display the summary
    #       - Use the appropriate function in the module 'tui' to indicate that the summary
    #       process has completed.
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
                records = process.retrieve_records_obs_dates(covid_records, tui.observation_dates())
                tui.display_records(records)
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

        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        elif option == 2:
            tui.progress("Visualisation operation", 0)
            variant2 = tui.menu(2)
            records = process.retrieve_records_summary(covid_records)
            if variant2 == 1:
                tui.progress("Visualisation pie chart", 0)
                visual.country_region_pie_chart(records)
                tui.progress("Visualisation pie chart", 100)
            if variant2 == 2:
                tui.progress("Visualisation bar chart", 0)
                visual.observation_chart(records)
                tui.progress("Visualisation bar chart", 100)
            if variant2 == 3:
                tui.progress("Animated visualisation ", 0)
                visual.animated_summary(covid_records)
                tui.progress("Visualisation operation", 100)
                tui.progress("Animated visualisation", 100)
            tui.progress("visualisation operation", 100)

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
        # You should use these to write the records (either all or only those for a specific country/region)
        # to a JSON file.

        elif option == 3:
            tui.progress("Export Data operation", 0)
            variant3 = tui.menu(3)
            if variant3 == 1:
                tui.progress("Exporting All Data to a JSON file", 0)

                tui.progress("Exporting All Data to a JSON file", 100)
            if variant3 == 2:
                country = tui.country_region()
                tui.progress(f"Exporting Data for {country} to a JSON file", 0)

                tui.progress(f"Exporting Data for {country} to a JSON file", 100)
            tui.progress("Export Data operation", 100)
        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        elif option == 4:
            break

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        else:
            tui.error(" Try again!!")


if __name__ == "__main__":
    run()
