import methods

# The user should make a list of five values

numbers = []
for num in range(0,5):
    num = int(input('Enter numbers of your choice please: '))
    numbers.append(num)

numbers.sort()
print('\nsorted list:', numbers)

sum = methods.sum_list(numbers)
print(f'\nThe sum of your values is: {sum}')

product = methods.product_list(numbers)
print(f'\nThe product of your values is: {product}')

average = methods.average(numbers)
print(f'\nThe mean of your values is:', round(average, 2))

print('\nThe median of your values is:', numbers[2])

mode = methods.mode(numbers)
print(f'\nThe mode of your values is: {methods.mode(numbers)}')

print(f'\nYour largest value is: {numbers[-1]}')

print(f'\nYour smallest value is: {numbers[0]}')

numbers = list(set(numbers))
print(f'\nThese are your values without duplicates: {numbers}')


print('\nThese are your values without odd numbers:')
methods.odd_list(numbers)

print('\nThese are your values without even numbers: ')
methods.even_list(numbers)

input('\nPRESS ENTER TO FINISH!')

