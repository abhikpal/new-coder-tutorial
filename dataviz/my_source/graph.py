from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

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

    # plot the data
    plt.plot(data_counts)

    # change the x-ticks
    plt.xticks(range(len(day_tuple)), day_tuple)

    # plt.show()

    # save the figure
    plt.savefig("Days.png")

    # close the figure
    plt.clf()


def visualize_type(parsed_data):

    # classify counters by category
    counter = Counter([item["Category"] for item in parsed_data])

    # set labels for the incidents
    category_labels = tuple(counter.keys())

    # set starting x locations for the bars
    x_locations = np.arange(len(category_labels)) + 0.5

    # set width of each bar
    width = 0.5

    # assign the data to the plot
    plt.bar(x_locations, counter.values(), width=width)

    # put labels on the graph
    plt.xticks(x_locations + width/2.0, category_labels, rotation=90)

    # give more space at the bottom to prevent cutting the labels
    plt.subplots_adjust(bottom=0.4)

    # change figure size
    plt.rcParams['figure.figsize'] = 12, 8

    # plt.show()

    # save and close
    plt.savefig('Type.png')
    plt.clf()


def main():
    parsed_data = parse.parse(parse.DATA_FILE, ",")
    visualize_days(parsed_data)
    visualize_type(parsed_data)

if __name__ == '__main__':
    main()
