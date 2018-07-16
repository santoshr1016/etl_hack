"""
Author: R Santosh Kumar
Description: ETL assignment
Date: 16th July, 2018
"""
import collections
import os

from ETL_package.etl_conversion import type_dict

FILE = os.getcwd() + "/Challenge_me.txt"


def load(file_name=FILE):
    """ Function to load the file

    :param file_name: The file to processed
    :return: list of valid rows of the file data
    """
    title_row = True
    elements = []
    for line in get_file_data(file_name):
        if title_row:
            line = [col.replace('-','_')for col in line if col]
            vehicle = collections.namedtuple('vehicle', line)
            title_row = False
            continue
        line.pop(0)
        row = vehicle._make(line)
        elements.append(row)

    return elements


def get_file_data(file_name):
    """ Function to read the file data line by line

    :param file_name: (string) Name of the file
    :return: returns a valid line(row of data)
    """
    try:
        with open(file_name) as file:
            for line in file:
                if line_is_valid(line):
                    yield line.strip().split(";")
    except IOError as error:
        print(error)

def line_is_valid(line):
    """ Function to check the validity of line(row of data)
    :param line: each line of the file
    :return: boolean, True for valid line
    """
    if '-' in map(lambda item: item.strip(), line.strip().split(";")):
        return False
    else:
        return True


def transform(filtered_list):
    """ Transformation function to get correct col and data
    :param filtered_list: list of the valid lines from the load file
    :return: list of col names and list of row data
    """
    out_put = {}
    out_list = []
    # loop to get the required columns, random ordered
    for item in filtered_list:
        for val in item._fields:
            if val in type_dict:
                out_put[val] = type_dict.get(val)(getattr(item, val))
        out_list.append(out_put)
        out_put = {}

    # loop to the ordered columns data as per output
    all_rows = []
    for item in out_list:
        tmp_row = []
        for key in type_dict.keys():
            out_put[key] = item[key]
            tmp_row.append(item[key])
        all_rows.append(tmp_row)

    col_row = [col.replace('_', '-') for col in type_dict.keys()]
    all_rows.insert(0, col_row)
    return all_rows

# if __name__ == '__main__':
#     filtered_list = load("../Challenge_me.txt")
#     out_put = transform(filtered_list)
#
#     for item in out_put:
#         print(item)
