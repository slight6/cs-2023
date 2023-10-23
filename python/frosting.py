#!/usr/bin/python

__author__ = 'Jason Consiglio'
__date__ = '10/20/2023'

import math
import locale as lc
from decimal import Decimal, ROUND_HALF_UP


# Taking care of locale early
result = lc.setlocale(lc.LC_ALL, '')
if result == 'C':
    print('Set locale on my own')
    lc.setlocale(lc.LC_ALL, 'en_US')

def calculate(diameter, height, layers):
    """Calculate the total area and amount of frosting needed.
    
        Args:
            diameter (float): Diameter of the cake
            height (float): Height of the cake
            layers (int): Number of layers of the cake
        Returns:
            None

    """
    price = Decimal().quantize(Decimal('.01'), ROUND_HALF_UP)
    area_top = math.pi * (diameter / 2) ** 2
    area_side = math.pi * diameter * height
    total_area = area_top * layers + area_side
    num_tubs = math.ceil(total_area / 60)
    price = num_tubs * 1.25

    # Output the number of tubs and total price of the frosting
    
    print(f'Num tubs: {num_tubs:>5}')
    print(f'Price: {lc.currency(price, grouping = True):>8}')
    # Have to put a print statement here to pass the test. I don't know why.
    print()

def main():
    """Begin program and accept input for the calculate function

        Args:
            None
        Returns:
            None

    """
    diameter = float(input('Diameter? '))
    print()
    height = float(input('Height? '))
    print()
    layers = int(input('Layers? '))
    print()
    calculate(diameter, height, layers)

if __name__ == '__main__':
    main()
