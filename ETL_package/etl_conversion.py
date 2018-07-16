"""
Author: R Santosh Kumar
Description: ETL assignment
Date: 16th July, 2018
"""

from collections import OrderedDict

ASPIRATION_TYPE = "std"
ENGINE_LOCATION = "front"
num_cylinders = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}

"""
Conversion functions for the specific column type
"""
def convert_engine_location(val):
    return 1 if val.lower() == ENGINE_LOCATION else 0


def convert_num_of_cylinders(val):
    return num_cylinders.get(val.lower())


def convert_engine_size(val):
    return int(val)


def convert_weight(val):
    return int(val)


def convert_horsepower(val):
    return float(val.replace(',', '.'))


def convert_aspiration(val):
    return 1 if val.lower() == ASPIRATION_TYPE else 0


def convert_price(val):
    return float(val)/100


def convert_make(val):
    return str(val)

type_dict = OrderedDict()
type_dict["engine_location"] = convert_engine_location
type_dict["num_of_cylinders"] = convert_num_of_cylinders
type_dict["engine_size"] = convert_engine_size
type_dict["weight"] = convert_weight
type_dict["horsepower"] = convert_horsepower
type_dict["aspiration"] = convert_aspiration
type_dict["price"] = convert_price
type_dict["make"] = convert_make
