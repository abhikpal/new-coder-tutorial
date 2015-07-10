from collections import Counter
import matplotlib.pyplot as plt
import numpy as numpy

import parse


def visualize_days(parsed_data):
    """
    Visualizes parsed_data by day of the week.
    """

    # prepare list that will be used later fow counting.
    # counter = Counter(item["DayOfWeek"] for item in parsed_data)

    counter = {}

    for item in parsed_data:
        try:
            counter[item["DayOfWeek"]] += 1
        except KeyError:
            counter[item["DayOfWeek"]] = 0

    # seperate out the counter
    data_counts = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
    ]

    # tuple of shorrt days names to be used for labelling the axis
    day_tuple = tuple(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

    plt.rcParams['toolbar'] = 'None'
    plt.figure(facecolor='white')
    # plt.xkcd()

    ## plot the data
    plt.plot(data_counts)

    ## change the x-ticks
    plt.xticks(range(len(day_tuple)), day_tuple)

    plt.show()

def main():
    visualize_days(parse.parse(parse.DATA_FILE, ","))

if __name__ == '__main__':
    main()
