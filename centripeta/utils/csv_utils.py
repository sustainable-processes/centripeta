"""
JSON Wrappers

.. moduleauthor:: Graham Keenan <https://github.com/ShinRa26>
"""

import csv

def read_csv(filename, delimiter=","):
    """Reads a CSV file, returning the column names and data

    Arguments:
        filename {str} -- Name of the csv file to read

    Keyword Arguments:
        delimiter {str} -- Default delimiter for csv format (default: {","})

    Returns:
        list -- Column names as a list
        list -- Data rows as a list of lists
    """
    with open(filename) as f:
        reader = csv.reader(f, delimiter=delimiter)
        data = [row for row in reader]
        header = data.pop(0)

    return header, data


def write_csv(header, data, filename, delimiter=","):
    """Writes data out in CSV format

    Arguments:
        header {list} -- Column names as a list
        data {list} -- Data rows as a list of lists
        filename {str} -- Name of the file

    Keyword Arguments:
        delimiter {str} -- Default delimiter for csv format (default: {","})
    """
    with open(filename, "w") as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerow(header)
        writer.writerows(data)
