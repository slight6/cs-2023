#!/usr/bin/python

""" Write a program.

__author__ = 'Jason Consiglio'
__date__ = '10/04/2023'

"""

import math
import locale as lc
from decimal import Decimal, ROUND_HALF_UP


def calc_and_print(balance, apr, payment):
    """ Function to write data to file based on user input.
    Args:
        balance (float)
        apr (float)
        payment (float)
    Returns:
        None
    """
    dec_balance = Decimal(balance).quantize(Decimal('.01'), ROUND_HALF_UP)
    dec_apr = Decimal(apr / 100).quantize(Decimal('.01'), ROUND_HALF_UP)
    dec_payment = Decimal(payment).quantize(Decimal('.01'), ROUND_HALF_UP)


    dec_interest = Decimal(dec_balance * (dec_apr / 12))
    new_balance = dec_balance + dec_interest - dec_payment

    try:
        lc.setlocale(lc.LC_ALL, '')
    except lc.Error:
        print('unable to set locale')
        

    print(f'Interest Paid: {lc.currency(dec_interest, grouping = True):>15}', )
    print(f'Balance:       {lc.currency(new_balance, grouping = True):>15}')

def main():
    """ Main function to do something
    Args:
        None
    Returns:
        None
    """
    balance = float(input('Balance? '))
    print()
    apr = float(input('APR? '))
    print()
    payment = float(input('Payment? '))
    print()
    calc_and_print(balance, apr, payment)
    

if __name__ == '__main__':
    main()

