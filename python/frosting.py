"""
Write a program to calculate how many tubs of frosting you need to buy to fill and frost a cake
Prompt the user for the diameter of the cake, the height of the cake, and the number of layers
You will need to calculate the total area that needs to be covered by frosting
For each layer, the area is that of a circle, πr2, where is r is the radius (half the diameter)
For the side of the cake, the area is basically a rectangle wrapped around the cake. The width is πd, where d is the diameter. The height is the height entered
The total area will be the area for each layer times the number of layers PLUS the area for the side of the cake
For example, a two-layer cake with 6-inch diameter cakes and an overall height of 3 inches would be:
Area for each layer: π32 is approximately 28.2743
Area for the side of the cake is (π6)(3) is approximately 56.5487
Total area is 28.2743 * 2 (layers) + 56.5487 which is approximately 113.0973
Each tub of frosting covers 60 square inches
Each tub costs $1.25
Remember that you cannot purchase part of a tub from the store. If you need 2.1 tubs to cover the cake, then you must buy 3 tubs.
Set the locale to the user’s default locale
If that is not available, then set the locale to ‘en-US’
Output the number of tubs and total price of the frosting
On one line output, ‘Num tubs: ‘, followed by the number of tubs right-justified in 5 spaces
On the next line, output ‘Price: ‘, followed by the total price printed as currency right justifies in 8 spaces
Diameter? 6

Height? 3

Layers? 2

Num tubs:     2
Price:    $2.50
"""

import math
import locale as lc
from decimal import Decimal, ROUND_HALF_UP


# Set locale to user's default locale
lc.setlocale(lc.LC_ALL, '')

print(math.pi)

def calculate(diameter, height, layers):
    """Calculate the total area and amount of frosting needed.
    
        Args:
            diameter (float): Diameter of the cake
            height (float): Height of the cake
            layers (int): Number of layers of the cake
        Returns:
            None

    """

    # Calculate the area of the top of the cake
    area_top = math.pi * (diameter / 2) ** 2

    # Calculate the area of the side of the cake
    area_side = math.pi * diameter * height

    # Calculate the total area of the cake
    total_area = area_top * layers + area_side

    # Calculate the number of tubs needed
    num_tubs = math.ceil(total_area / 60)

    # Calculate the total price of the frosting
    price = num_tubs * 1.25

    # Output the number of tubs and total price of the frosting
    print(f'Num tubs: {num_tubs:>5}')
    print(f'Price: {price:>8}')

def main():
    """Accept input for the calculate function

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
