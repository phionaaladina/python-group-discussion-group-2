'''
Lists
Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function.

'''


'''
Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.

'''

fruits = ['apple', 'pear', 'banana', 'berry' , 'melon']

for fruit in fruits:
    print(fruit)



'''
Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared.
 Example: [1, 2, 3] should become [1, 4, 9].

'''

def squared(list):
    return [x**2 for x in list]

list = [1,2,3]
new_list = squared(list)
print(new_list)



'''
Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6],
 and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

'''

list1 = [1, 2, 3] 
list2 = [4, 5, 6]

combined = []

for a, b in zip(list1, list2):  # The zip function takes two (or more) iterables (like lists) and combines them into pairs of corresponding elements.
    combined.append(a)          # Append an element from list1
    combined.append(b)          # Append the corresponding element from list2

print(combined)


'''
Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], 
write a program to find and print the two largest numbers in the list without using the max() function.

'''
def large_num(list):
    list.sort(reverse=True)
    print(f'The two largest numbers are {list[0]} and  {list[1]}, ')

num_list = [3, 1, 4, 1, 5, 9, 2]
lst = [10, 89, 100, 20, 25]
large_num(num_list)
large_num(lst)
