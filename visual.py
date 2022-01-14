"""
This module is responsible for visualising the data using Matplotlib.
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import process
import tui

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
    ax.pie(num_confirmed, labels=countries, autopct='%1.1f%%')
    ax.set_title("Covid-19 Confirmed cases per Country/Region")
    plt.legend(loc="upper right")
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    ax.axis('equal')
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
    plt.ylabel("Number of Deaths", fontsize=18)
    plt.xlabel("Countries", fontsize=18)
    plt.tight_layout()
    plt.show()


def animated_summary(records):
    option = tui.menu(3)
    values = []
    data = ""
    if option == 1:
        values = process.retrieve_data_animation(records)

    elif option == 2:
        data = tui.country_region()
        values = process.retrieve_data_animation(records, data)

    x_date, y_confirmed, y_death, y_recovered = [], [], [], []
    for index in values[0].keys():
        x_date.append(index)
        y_confirmed.append(values[0][index][0])
        y_death.append(values[0][index][1])
        y_recovered.append(values[0][index][2])
    x, y1, y2, y3 = [], [], [], []

    global fig, ax

    def animate(frame):
        x.append(x_date[frame])
        y1.append(y_confirmed[frame])
        y2.append(y_death[frame])
        y3.append(y_recovered[frame])
        ax.plot(x, y1, color='red', marker='o', label="Confirmed")
        ax.plot(x, y2, color='black', marker='o', label="Deaths")
        ax.plot(x, y3, color='green', marker='o', label="Recovered")
        if len(x) == 1:
            ax.legend(loc="upper left")

    simple_animation = animation.FuncAnimation(fig, animate, frames=len(x_date), repeat=False, interval=1000)
    if option == 1:
        plt.title("Correlation of Covid-19 cases in the World")
    elif option == 2:
        plt.title(f"Correlation of Covid-19 cases in {str.upper(data)}")

    plt.ylabel("Number of Covid-19 Cases", fontsize=18)
    plt.xlabel("Date", fontsize=18)
    plt.style.use("seaborn")
    plt.tight_layout()
    plt.show()

