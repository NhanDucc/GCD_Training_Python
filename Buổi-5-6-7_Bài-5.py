# a
def input_fraction():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    while denominator == 0:
        print("The denominator cannot be 0!")
        denominator = int(input("Re-enter the denominator: "))
    return {'numerator': numerator, 'denominator': denominator}

def format_fraction(fraction):
    return f"{fraction['numerator']}/{fraction['denominator']}"

# b
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduce_fraction(fraction):
    gcd = find_gcd(fraction['numerator'], fraction['denominator'])
    reduced_numerator = fraction['numerator'] // gcd
    reduced_denominator = fraction['denominator'] // gcd
    return {'numerator': reduced_numerator, 'denominator': reduced_denominator}

# c
def compare_fraction(fraction_1, fraction_2):
    result_1 = fraction_1['numerator'] * fraction_2['denominator']
    result_2 = fraction_2['numerator'] * fraction_1['denominator']
    if result_1 > result_2:
        return "The first fraction is greater than the second fraction!"
    elif result_1 < result_2:
        return "The first fraction is less than the second fraction!"
    else:
        return "Two equal fractions!"

# d
def add_fraction(fraction_1, fraction_2):
    add_numerator = fraction_1['numerator'] * fraction_2['denominator'] + fraction_2['numerator'] * fraction_1['denominator']
    add_denominator = fraction_1['denominator'] * fraction_2['denominator']
    return {'numerator': add_numerator, 'denominator': add_denominator}

# e, f
def input_list():
    n = int(input("Enter the number of fractions of the list: "))
    fraction_list = []
    for i in range (n):
        print(f"Enter the information for fraction {i+1}")
        fraction = input_fraction()
        print()
        fraction_list.append(fraction)
    return fraction_list

# g
def find_max_fraction(fraction_list):
    max_fraction = fraction_list[0]
    for fraction in fraction_list:
        if compare_fraction(fraction, max_fraction) == "The first fraction is greater than the second fraction!":
            max_fraction = fraction
    return max_fraction


# a
print("Enter the first fraction information: ")
fraction_1 = input_fraction()
print("Enter the second fraction information: ")
fraction_2 = input_fraction()
print(f"The first fraction: {format_fraction(fraction_1)}")
print(f"The second fraction: {format_fraction(fraction_2)}")
print()

# b
print(f"The first fraction after reduction: {format_fraction(reduce_fraction(fraction_1))}")
print(f"The second fraction after reduction: {format_fraction(reduce_fraction(fraction_2))}")
print()

# c
compare_result = compare_fraction(fraction_1, fraction_2)
print(f"The result: {compare_result}")
print()

# d
sum = add_fraction(fraction_1, fraction_2)
print(f"Sum of two fractions: {format_fraction(reduce_fraction(sum))}")
print()

# e, f
fraction_list = input_list()
format_list = []
for fraction in fraction_list:
    format_fractions = format_fraction(fraction)
    format_list.append(format_fractions)
format_str = ', '.join(format_list)
print(f"The list of fractions just entered: [{format_str}]")
print()

# g
max = find_max_fraction(fraction_list)
print(f"The maximum fraction of the list: {format_fraction(max)}")
print()

# h
sum_fraction = {'numerator': 0, 'denominator': 1}
for fraction in fraction_list:
    sum_fraction = add_fraction(sum_fraction, fraction)
print(sum_fraction)
