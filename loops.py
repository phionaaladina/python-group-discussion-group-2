
'''
PYTHON DISCUSSION QUESTIONS


Loops
Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.
Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
'''

'''
Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.

'''

def even_numbers():
    for i in range(1,21):
        if i %2 == 0:
            print(i)

even_numbers()

'''
Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
'''
'''
The while True: loop is a common pattern when you want to repeat a block of code until a specific condition occurs.
The break statement provides a way to exit the loop based on a condition.
'''
while True:
    number = int(input('Please enter a number: '))
    if number > 10:
        print('Thank you. You have reached your limit.')
        break


'''
Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers 
from 1 to 5 using nested for loops.

'''


for i in range(1,6):
    print(f'Multiplication of {i}')
    for j in range(1,11):
        print(f'{i} x {j} = {i * j}')
        print()  #space



'''
Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program
 using a for loop to find the sum of all odd numbers and print the result.

'''  

numbers = [4, 7, 2, 9, 12, 15]

sum_odd_num = 0

for number in numbers:
 if number  % 2 != 0:
    sum_odd_num += number
print(f'Sum of Odd numbers: {sum_odd_num}')