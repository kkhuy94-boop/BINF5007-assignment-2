import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    """
    Loads data from a file into a list. 
    Returns a tuple that contains the list of values 
    and the total number of values in the column.
    """
    total_count = 0
    numbers = []
    with open(filepath, "r") as infile:
        for line in infile:
            line_num = 1
            try:
                num = float(line.split("\t")[column])
                int(num) # Raises ValueError if num is 'NaN'
                numbers.append(num)
                line_num += 1
                total_count +=1
            except ValueError: 
                total_count +=1
                continue # Skips non-numeric number and 'NaN'
            except IndexError:
                print(f"Exiting: There is no valid 'list index' in column {column} in line {line_num} in file: {filepath}")
                exit()
    number_of_valid_values = len(numbers)
    if number_of_valid_values < 1:
        print(f"Error: There were no valid number(s) in column {column} in file: {filepath}")
        exit()
    return (numbers,total_count)


def calculate_average(numbers:list)->float:
    """ Returns the average of the list of numbers. """
    return (sum(numbers) / len(numbers))


def get_max_and_min(numbers:list)->tuple[float, float]:
    """ Returns a tuple with the maximum and minimum values in the list, in that order. """
    return (max(numbers), min(numbers))


def calculate_variance(numbers:list)->float:
    """ Returns the variance of the numbers in the list. """
    sample_size = len(numbers) 
    if sample_size < 2:
        print("Error: Variance requires more than 1 sample size.")
        return 0.0
    else:
        avg = calculate_average(numbers)
        list_squared_dev = []
        for x in numbers:
            sqr_dev = (x - avg) ** 2
            list_squared_dev.append(sqr_dev)
    return sum(list_squared_dev) / (sample_size - 1)
        
   

def calculate_std_dev(numbers:list)->float:
    """ Returns the standard deviation of the numbers in the list. """
    variance = calculate_variance(numbers)
    return math.sqrt(variance)

def calculate_median(number:list)->float:
    """ Returns the median of the numbers in the list. """
    count = len(number)
    sorted_numbers = sorted(number)
    if count % 2 == 0: 
        first_middle = sorted_numbers[count // 2 - 1]
        second_middle = sorted_numbers[count // 2]
        return (first_middle + second_middle) / 2
    else:
        return float(sorted_numbers[count // 2])


