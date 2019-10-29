# Program to compute the volume and surface area of a sphere
# given the radius as input

from math import *

def sphereArea(radius):

    surfaceArea = 4 * pi * radius ** 2
    return surfaceArea

def sphereVolume(radius):

    volume = (4.0/3.0) * pi * radius ** 3
    return volume

def main():

    print("This program computes the volume and surface area")
    print("of a sphere of a particular radius.\n")

    r = float(input("What is the radius of the sphere?: "))

    s = sphereArea(r)
    v = sphereVolume(r)

    print("The Surface Area and the Volume of a sphere with radius, {2}, is {0:0.3f} and {1:0.3f}, respectively.".format(s,v,r))


main()