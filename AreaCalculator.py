"""
Codecademy - Learn Python 2
Area Calculator
"""

print "Starting the calculator..."

option = raw_input("Enter C for Circle, T for Triangle, S for Square, and R for Rectangle: ")

if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius**2
  print "Area: %f" % area
elif option == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "Area: %f" % area
elif option == 'S':
  side1 = float(raw_input("Enter side 1: "))
  side2 = float(raw_input("Enter side 2: "))
  area = side1 * side2
  print "Area: %f" % area
elif option == 'R':
  length = float(raw_input("Enter length: "))
  width = float(raw_input("Enter width: "))
  area = length * width
  print "Area: %f" % area
else:
  print "Error! Invalid shape."

print "Exiting..."
