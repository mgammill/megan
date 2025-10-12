def say_goodbye(name):
    print(f"Goodbye, {name}. It was nice to see you!")
# say_goodbye("Katie")

def area_of_circle(radius):
    area = 3.14*radius**2
    print(area)
# area_of_circle(4)

def subtract(a, b):
    return(a - b)
def multiply(a, b):
    return(a * b)
def divide(a, b):
    return(a / b)
# print(subtract(5, 1))
# print(multiply(2, 7))
# print(divide(9, 2))

weather_report = [59, 62, 75, 74, 60, 54]

def todays_min_and_max_temperatures(weather_report):
    min_temp = min(weather_report)
    max_temp = max(weather_report)
    return(min_temp, max_temp)

# print(todays_min_and_max_temperatures(weather_report))

def is_weekend(day):
    if day == 6 or day == 7:
        return("It's the weekend! Let's party!")
    else:
        return("It's not the weekend:(")

# print(is_weekend(3))

def fuel_efficiency(miles, gallons):
    miles_per_gallon = (miles / gallons)
    return(miles_per_gallon)

# print(fuel_efficiency(80, 3))
    
def encrypt(number):
    string = str(number)
    length = len(string)
    encryption = string[length - 1] # This holds the last digit (in 12345, this would be 5)
    for i in range(length - 1): 
        encryption = encryption + (string[i]) 
# This adds digits (pulled from left to right of the input) 
# to the right of the starting digit 
# (ie starting with 5, add 1 (51), then add 2 (512), etc etc)
    return(encryption)

# print(encrypt(1560))

def power(x, y):
    number = 1
    for i in range(y):
        number = number*x
    return(number)

# print(power(2, 3))

def min(list): # using a FOR loop
    tracker = list[0]
    for int in list:
        if tracker > int:
            tracker = int
    return((tracker))

def max(list): # using a FOR loop
    tracker = list[0]
    for int in list:
        if tracker < int:
            tracker = int
    return(tracker)

def minimum(list): # using a WHILE loop
    tracker = list[0]
    i = 0
    while i in range(len(list)):
        if tracker > list[i]:
            tracker = list[i]
        i += 1
    return(tracker)

def maximum(list): # using a WHILE loop
    tracker = list[0]
    i = 0
    while i in range(len(list)):
        if tracker < list[i]:
            tracker = list[i]
        i += 1
    return(tracker)

def sum_of_digits(number):
    string = str(number)
    counter = 0
    for i in range(len(string)):
        counter += int(string[i])
    return(counter)

# print(sum_of_digits(2468))

x = 1560
result = encrypt(x) # Encrypts x so that the last digit is first
print(f"The result of Secret Code (5.4) with x = {x} is {result}.")









