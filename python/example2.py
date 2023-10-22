#!/usr/bin/env python3

"""Module to calculate cost of a tank."""

__author__ = 'Karen Peterson'
__date__ = '7/20/2020'

import math
import locale as lc
from decimal import Decimal, ROUND_HALF_UP


def print_countdown():
    """Print a formattted countdown loop.

    Args:
        None

    Returns:
        None
    """
    print('Calculating...', end='')
    for i in range(10, 0, -1):
        print(f'{i:2d}...', end='')
    print()


def calc_cost(gallons, price_per_gallon):
    """Calculate the mpg and cost.

    Args:
        gallons (float): number of gallons purchased
        price_per_gallon (float): cost for one gallon

    Returns:
        orig_cost (Decimal): original amount due with no discount
        discount (Decimal): amount of discount
        cost (Decimal): cost after discount is applied
    """
    # orig_cost = gallons * price_per_gallon
    dec_price_per_gallon = Decimal(price_per_gallon).quantize(
        Decimal('.01'), ROUND_HALF_UP)
    dec_gallons = Decimal(gallons).quantize(
        Decimal('.01'), ROUND_HALF_UP)
    print(dec_price_per_gallon)
    print(dec_gallons)
    orig_cost = dec_gallons * dec_price_per_gallon
    discount = math.floor(math.sqrt(orig_cost))
    cost = orig_cost - discount
    return orig_cost, discount, cost


def main():
    """Calculate cost of tank and mpg.

    Args:
        None

    Returns:
        None
    """
    miles = float(input('Miles? '))
    print()
    gallons = float(input('Gallons? '))
    print()
    price_per_gallon = float(input('Price per gallon? '))
    print()
    print_countdown()
    mpg = miles / gallons
    orig_cost, discount, cost = calc_cost(gallons, price_per_gallon)

    print('Unformatted')
    print('MPG', 'Cost', '-Discount', 'Final')
    print(mpg, orig_cost, discount, cost)
    print()

    print('Formatted')
    # Can use format specifiers with format function to
    # -- display our numbers and strings nicely
    # -- now our data is all lined up
    print(f'{"MPG":>10} {"Cost":>10} {"-Discount":>10} {"Final":>10}')
    print(f'{mpg:10.2f} {orig_cost:10.2f} {discount:10.2f} {cost:10.2f}')
    print()

    # setting the locale to '' will try to set it to the
    # -- user's default locale
    # -- use LC_ALL to affect both NUMERIC and MONETARY VALUES
    # Returns 'C' is unable to set to default
    result = lc.setlocale(lc.LC_ALL, '')
    if result == 'C':
        print('Set locale on my own')
        lc.setlocale(lc.LC_ALL, 'en_US')

    print('Formatted with locale')
    print(f'{"MPG":>10} {"Cost":>10} {"-Discount":>10} {"Final":>10}')
    print(lc.format_string('%10.2f', mpg), end=' ')
    print(f'{lc.currency(orig_cost):>10}', end=' ')
    print(f'{lc.currency(discount):>10}', end=' ')
    print(f'{lc.currency(cost, grouping=True):>10}', end=' ')
    print()

    # try setting to de for Germany
    # -- be careful because setlocale can raise lc.Error
    # -- is the country code is bad
    try:
        lc.setlocale(lc.LC_ALL, 'de')  # try: 'de' or 'uk'
    except lc.Error:
        print('unable to set locale')

    print('Formatted with German locale')
    print(f'{"MPG":>10} {"Cost":>10} {"-Discount":>10} {"Final":>10}')
    print(lc.format_string('%10.2f', mpg), end=' ')
    print(f'{lc.currency(orig_cost):>10}', end=' ')
    print(f'{lc.currency(discount):>10}', end=' ')
    print(f'{lc.currency(cost, grouping=True):>10}', end=' ')
    print()

    num1 = 1.01
    print(num1)
    num1 += 1.01
    print(num1)
    num1 += 1.01
    print(num1)


if __name__ == '__main__':
    main()
