#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 15th, 2023
# This program generates 10 random numbers
# then finds and displays the max of those numbers
import constants
import random


def calc_max(random_numbers):
    # Set maximum to first value
    maximum = random_numbers[0]

    # Initialize counter
    counter = 0

    # Use a while loop to find the max number
    while counter < constants.ARRAY_SIZE - 1:
        counter = counter + 1
        if random_numbers[counter] > maximum:
            maximum = random_numbers[counter]

    # Return the max number
    return maximum


def main():
    # Create empty list
    list_of_int = []

    # Use a for loop to generate all of the random numbers and populate the array
    for counter in range(0, constants.ARRAY_SIZE):
        list_of_int.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        print(
            "{} added to the list at position {}.".format(list_of_int[counter], counter)
        )

    # Function call
    maximum = calc_max(list_of_int)

    # Display the max
    print("")
    print("The max number is {}.".format(maximum))


if __name__ == "__main__":
    main()
