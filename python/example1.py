#!/usr/bin/python
""" Write a program to read and total all numbers in a file. """

__author__ = 'Jason Consiglio'
__date__ = '10/13/2023'


import sys
import pathlib


def read_file(file_name):
    """ Function to read in a file based on user input.
    Args:
        file_name (str): Name of file to read in.
    Returns:
        list_of_lines (list): List of lines from file.
    """
    list_of_lines = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                list_of_lines.append(line)
    except FileNotFoundError:
        print()
        print('Could not open file - exiting')
        sys.exit()
    except OSError:
        print()
        print('Could not open file - exiting')
        sys.exit()
    return list_of_lines


def main():
    """ Main function to ask user for filename to read and calculates total.
    Args:
        None
    Returns:
        None
    """
    list_of_lines = read_file(input('File? '))
    print()
    grand_total = 0.0
    for line in list_of_lines:
        try:
            new_line = float(line.strip())
        except ValueError:
            print(f'Invalid number: {line.strip()}')  
            continue
        grand_total += new_line
    print(f'Grand total: {grand_total:.1f}')

     
if __name__ == '__main__':
    main()
