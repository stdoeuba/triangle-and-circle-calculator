

# function for calculating the area of a triangle
def area (h, b):
    return (h*b) / 2

import math

#function that defines an area of a circle
def area_of_circle(r):
    return  r**2 * math.pi
    
#print to console 
print("this application calculates the area of a triangle: ")

#user input for height and side length
h =  float(input('enter height of the triangle in cm: '))
b =  float(input('enter base side of the triangle in cm: '))

#calculating area of the triangle
trianglearea = area(h,b)

#print solution to the console
print("the triangle has an area of: " , round(trianglearea,2), "cm^2")

#next step calculating circle area
print("in the next step this application calculates the area of a circle: ")

#user input for the radius
r =  float(input('enter radius of the circle in cm: '))

#calculating area of the circle
circlearea = area_of_circle(r)

#print solution to the console
print("the circle has an area of: " , round(circlearea,2), "cm^2")

