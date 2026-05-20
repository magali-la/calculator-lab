# This script prints info about Cruella de Vil and calculates how many acres her estate is.
# profile variables
name = "Cruella de Vil"
age = 40
height = 1.85

# print the person
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")

# calculate age in 5 years
print("In 5 years " + f"I will be {age + 5} years old.")

# calculate age in dog years and limit to 1 decimal place
dogAge = age / 7 # full number is 5.714285714285714
print(f"If I were a Dalmatian, I would be about {dogAge:.1f} years old.")

# calculate area of a rectangle
width = 5.5
height = 2
print(f"The area of a rectangle a {width} x {height} rectangle is {width * height}.")

# calculates the amount of land Cruella has - format sqMiles to two decimal places and round up to nearest integer for acres
estateWidth = 1.25
estateLength = 2.20
estateSqMiles = estateWidth * estateLength
print(f"My estate is {estateWidth} miles wide and {estateLength} miles long. This is a total of {estateSqMiles:.2f} square miles. I have {round(estateSqMiles * 640)} acres of land.")