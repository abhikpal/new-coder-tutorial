import csv

DATA_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, _delimiter):
    """
    Parses a raw csv data file to a JSON like object.

    input:
        * raw_file: the raw csv file
        * delimiter: <self explnatory>
    """

    # open CSV file
    opened_file = open(raw_file)

    # read CSV file
    csv_data = csv.reader(opened_file, delimiter=_delimiter)

    # build required data structure to return parsed data
    parsed_data = []

    fields = csv_data.next()  # the first line is headers

    for row in csv_data:
        # fields: [f1, f2, f3, ...]
        # row: [v1, v2, v3, ...]
        # this line converts it to a dict:
        # {f1:v1, f2:v2, f3:v3, ...}
        # and adds it to the parsed_data list
        parsed_data.append(dict(zip(fields, row)))

    # close CSV file
    opened_file.close()

    return parsed_data


def main():
    # call the parrser function
    data = parse(DATA_FILE, ',')

    # print all of the data
    # (like, why would you do that!?)
    print data

if __name__ == '__main__':
    main()