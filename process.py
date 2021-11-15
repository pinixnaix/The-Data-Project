"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

import tui


def records_loaded(records):
    return len(records)


def retrieve_record_serial_number(records):
    serial = tui.serial_number()
    record = None
    for rec in records:
        if serial == rec[0]:
            record = rec
    return record


def retrieve_records_obs_dates(records):
    total_records = []
    obs_dates = tui.observation_dates()
    for date in obs_dates:
        for record in records:
            if date == record[1]:
                total_records.append(record)
    print(len(total_records))
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
