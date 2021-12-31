"""
This module is responsible for visualising the data using Matplotlib.
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from main import covid_records

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

fig, ax = plt.subplots()


def country_region_pie_chart(records):
    countries = []
    num_confirmed = []
    for country in records[0].keys():
        countries.append(country)
        conf = records[0][country]
        num_confirmed.append(conf[0].get("confirmed"))

    # To sort the two lists together
    index = list(range(len(num_confirmed)))
    index.sort(key=num_confirmed.__getitem__)
    index.reverse()
    num_confirmed[:] = [num_confirmed[i] for i in index]
    countries[:] = [countries[i] for i in index]

    global ax
    ax.pie(num_confirmed[:5], labels=countries[:5], explode=(0.5, 0, 0, 0, 0))
    ax.set_title("Covid-19 Confirmed cases per Country/Region")
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


def observation_chart(records):
    countries = []
    num_death = []
    for country in records[0].keys():
        countries.append(country)
        conf = records[0][country]
        num_death.append(conf[1].get("deaths"))

    # To sort the two lists together
    index = list(range(len(num_death)))
    index.sort(key=num_death.__getitem__)
    index.reverse()
    num_death[:] = [num_death[i] for i in index]
    countries[:] = [countries[i] for i in index]
    global ax
    ax.bar(countries[:5], num_death[:5])
    ax.set_title("Top 5 Countries for number of deaths with Covid-19")
    plt.tight_layout()
    plt.show()


def animate(frame):
    global ax
    ax.cla()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.plot(frame, frame, 'ro')


def animated_summary(records):
    global fig
    simple_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()
