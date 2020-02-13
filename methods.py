# Joe Degere
# 2/11/2020
# Assignment 2 - List Operations


# This will sort the integers that you have chosen
def sort_numbers(numbers):
    sorted(numbers)

# The sum of your values will be calculated


def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# The product of your values


def product_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# The Mean of your values


def average(numbers):
    return sum(numbers) / len(numbers)

# The mode of the values


def mode(numbers):
    if numbers == []:
        return None
    else:
        return max(set(numbers), key=numbers.count)

# This function prints the largest number in the list


def largest(numbers):
    return numbers(-1)

# This function prints the smallest number in the list


def smallest(numbers):
    return numbers(0)

# This function prints the even numbers chosen


def even_list(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num, end=' ')

# This function prints the odd numbers chosen


def odd_list(numbers):
    for num in numbers:
        if num % 2 != 0:
            print(num, end=' ')

