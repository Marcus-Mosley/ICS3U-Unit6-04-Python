#!/usr/bin/env python3
#
# Created by Marcus A. Mosley
# Created on November 2020
# This program finds the average of a 2D array

import random


def array_average(passed_number_array):
    # This program finds the average of a 2D array

    sum = 0
    num_items = 0

    for row_value in passed_number_array:
        for single_element in row_value:
            sum += single_element
            num_items += 1
    average = sum / num_items

    return average


def main():
    # This function receives input

    number_array = []

    # Input
    rows = int(input("How many rows would you like?: "))
    columns = int(input("How many columns would you like?: "))
    print(" ")

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            number = random.randint(0, 50)
            temp_column.append(number)
            print("The random number is {} ".format(number))
        number_array.append(temp_column)
    print(" ")

    # Call Functions
    average = array_average(number_array)

    print("The average is {0:.2f}".format(average))


if __name__ == "__main__":
    main()
