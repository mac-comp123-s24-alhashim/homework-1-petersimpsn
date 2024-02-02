"""
Determines the number of circles of radius 5 meters that should be done to cover a rectangular search area.

@author: Peter J. Simpson (psimpson@macalester.edu)
"""

import math

rectHeight = int(input("Please input the height of the desired rectangular search area:"))
rectWidth = int(input("Please input the width of the desired rectangular search area:"))
searchDiameter = math.sqrt(rectHeight*rectHeight + rectWidth*rectWidth)
searchRadius = searchDiameter/2

numCircles1 = searchRadius / 5

print("The search radius is: ", searchRadius, " meters.")
print("Therefore, we would do ", math.ceil(numCircles1), " circles, with each expanding by 5 meters.")