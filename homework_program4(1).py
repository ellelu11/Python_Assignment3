# Michelle Lugo
# CIS 135
# Homework Program 04
# For this assignment, I created a program that displays car data in rows and columns.
# I had the make and model data be displayed on the left side. Units sold and starting price data be displayed on the right.
# I also had to display a comma in the thousands position for the units sold.
# For the starting price, I had to display two values after the decimal, a comma and a dollar sign.

print("{0:15s}{1:15s}{2:15s}{3:17s}".format("Make", "Model", "Units Sold", "Starting Price"))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Chevrolet", "Silverado", 586675, 28595))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Chevrolet", "Equinox", 270994, 25000))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Ford", "F-Series", 787422, 30635))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("GMC", "Sierra", 253016, 29695))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Honda", "CR-V", 333502, 26525))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Honda", "Civic", 261225, 22000))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Lamborghini", "Huracan", 1095, 208571))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Toyota", "RAV4", 430387, 27325))

print("{0:15s}{1:<18s}{2:<15,d}${3:>10,.2f}".format("Toyota", "Camry", 294348, 25965))

