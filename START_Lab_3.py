
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in
    isCutoff = False
    if (number < cutoff):
        print(f'{number} is less than {cutoff}')
        isCutoff = True
    elif (number > cutoff):
        print(f'{number} is not less than {cutoff}')
        isCutoff = False
    else:
        print(f'{number} is equal less to {cutoff}')
        isCutoff = False
    return isCutoff

print(lab3Question1(5,10))
print(lab3Question1(15,10))
print(lab3Question1(0,10))
print('------------------')
def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    message = ''
    # if zero
    if decimal_number == 0:
        message = 'zero'
    # if positive
    elif decimal_number > 0:
        message = 'positive'
    # if negative
    elif decimal_number < 0:
        message = 'negative'
    else:
        # if anything else
        message = 'invalid'
    return message

print(lab3Question2(0))
print(lab3Question2(5.5))
print(lab3Question2(-10))
print('------------------')

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    message = ''
    if year >= 2001 and year <= 2100:
        message = '21st century'
    elif year >= 1901 and year <= 2000:
        message = '20th century'
    elif year >= 1801 and year <= 1900:
        message = '19th century'
    elif year <= 1800:
        message = 'ancient'
    else:
        message = 'invalid'
    return message

print(lab3Question3(2021))
print(lab3Question3(1950))
print(lab3Question3(1850))
print(lab3Question3(1500))
print(lab3Question3(1909))
print('------------------')

def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers
    numbers = [number_1, number_2, number_3]
    if not isinstance(numbers[0], (int, float)) or not isinstance(numbers[1], (int, float)) or not isinstance(numbers[2], (int, float)):
        return None
    else:
        return max(numbers)

print(lab3Question4(5,10,15))
print(lab3Question4(10,5,15))
print(lab3Question4(10,15,5))
print(lab3Question4('invalid',10,15))
print('------------------')

def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    message = ''
    if scale_used.upper() == 'C':
        if temperature <= 0:
            message = 'Solid'
        elif temperature > 0 and temperature <= 100:
            message = 'Liquid'
        elif temperature > 100:
            message = 'Gas'
        else:
            message = 'Invalid'
    elif scale_used.upper() == 'F':
        if temperature <= 32:
            message = 'Solid'
        elif temperature > 32 and temperature <= 212:
            message = 'Liquid'
        elif temperature > 212:
            message = 'Gas'
        else:
            message = 'Invalid'
    else:
        message = 'Invalid'
    return message

print(lab3Question5(25,'C'))
print(lab3Question5(-10,'C'))
print(lab3Question5(110,'C'))
print(lab3Question5(75,'F'))
print(lab3Question5(10,'F'))
print(lab3Question5(220,'F'))
print('------------------')
