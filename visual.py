"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""
import matplotlib.pyplot as plt


def country_region_pie_chart(records):
    countries = []
    num_confirmed = []
    for country in records[0].keys():
        countries.append(country)
        conf = records[0][country]
        num_confirmed.append(conf[0].get("confirmed"))
    plt.pie(num_confirmed, labels=countries)
    plt.legend(title="Covid-19 Confirmed cases per Country/Region")
    plt.show()


def observation_chart(records):
    countries = []
    num_death = []
    for country in records[0].keys():
        countries.append(country)
        conf = records[0][country]
        num_death.append(conf[1].get("deaths"))

    plt.bar(countries, num_death)
    plt.show()


def animated_summary(records):
    pass
