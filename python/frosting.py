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
"""

import math
import locale

# Set locale to user's default locale
locale.setlocale(locale.LC_ALL, '')

