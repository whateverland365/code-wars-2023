#F-Strings
# guess = 8
# print(f"your guess of {guess} was wrong!")

#.format method
# x=10
# formatted = "I've told you {} times already!".format(10)

# fruit = 'banana'
# ripeness = 'unripe'
# print("The {} is {}".format(fruit, ripeness))

# The old way => % operator (deprecated)
# x = 10
# formatted = "I've told you %d times already" % (x)


# Formatting Strings
# Set the variable called first  to your first name.

# Set the variable called last  to your last name.

# Then set the variable called formatted  that interpolates both using the .format()  method.  Make sure you follow this pattern:

# "First Name: Colt, Last Name: Steele"
# Remember, Udemy doesn't support f-strings yet, so you have to use format()  

first = 'Rene'
last = 'FloorCruise'

#Using .format() method
formatted = "First Name: {}, Last Name: {}".format(first, last)

#F-String Version
#formatted = f"First Name: {first}, Last Name: {last}"

print(formatted)


