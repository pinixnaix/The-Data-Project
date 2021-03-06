"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""
import tui


"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries


"""


def records_loaded(records):
    return len(records)


def retrieve_record_serial_number(records):
    serial = tui.serial_number()
    record = None
    for rec in records:
        if serial == rec[0]:
            record = rec
    return record


def retrieve_records_obs_dates(records, obs_dates):
    total_records = []
    for date in obs_dates:
        for record in records:
            if date == record[1]:
                total_records.append(record)
    return total_records


def retrieve_records_country_region(records):
    records_per_country = []
    records_dict = {}
    for record in records:
        if record[3] not in records_dict:
            records_dict[record[3]] = []
        records_dict[record[3]].append(record)
    records_per_country.append(records_dict)
    return records_per_country


def retrieve_records_summary(records):
    records_per_country = []
    records_dict = {}
    for record in records:
        if record[3] not in records_dict:
            records_dict[record[3]] = []
        records_dict[record[3]].append(record[5:])

    for keys, values in records_dict.items():
        num_conf = 0
        num_death = 0
        num_recover = 0
        for value in values:
            num_conf += value[0]
            num_death += value[1]
            num_recover += value[2]
        stats = [{"confirmed": num_conf}, {"deaths": num_death}, {"recovered": num_recover}]
        records_dict.update({keys: stats})
    records_per_country.append(records_dict)
    return records_per_country


def retrieve_data_animation(records, data=None):
    records_animation = []
    records_dict = {}
    for record in records:
        if str.lower(record[3]) == data:
            if record[1] not in records_dict:
                records_dict[record[1]] = []
            records_dict[record[1]].append(record[5:])
        elif data is None:
            if record[1] not in records_dict:
                records_dict[record[1]] = []
            records_dict[record[1]].append(record[5:])
    for keys, values in records_dict.items():
        num_conf = 0
        num_death = 0
        num_recover = 0
        for value in values:
            num_conf += value[0]
            num_death += value[1]
            num_recover += value[2]
        stats = [num_conf, num_death, num_recover]
        records_dict.update({keys: stats})

    records_animation.append(records_dict)
    return records_animation
