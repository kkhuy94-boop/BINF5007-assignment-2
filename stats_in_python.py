import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    """
    Loads data from a file into a list. 
    The function returns a tuple that contains the list of values 
    and the total number of values in the column
    """
    numbers = []
    with open(filepath, "r") as infile:
        for line in infile:
            line_num = 1
            try:
                num = float(line.split("\t")[column])
                int(num) # Raises ValueError if num is 'NaN'
                numbers.append(num)
                line_num += 1
            except ValueError: 
                continue # Skips non-numeric number and 'NaN'
            except IndexError:
                print(f"Exiting: There is no valid 'list index' in column {column} in line {line_num} in file: {filepath}")
                exit()
    number_of_values = len(numbers)
    if number_of_values < 1:
        print(f"Error: There were no valid number(s) in column {column} in file: {filepath}")
        exit()
    return (numbers,number_of_values)


def calculate_average(numbers:list)->float:
    """ Function that returns the average of the list of numbers"""
    return float(sum(numbers) / len(numbers))



def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    pass

def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    pass

def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    pass

def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    pass


