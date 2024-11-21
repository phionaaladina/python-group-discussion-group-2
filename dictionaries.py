

'''
 Dictionaries
 1. Basic: Create a dictionary with three key-value pairs representing a student's
 information: name, age, and grade. Print each key-value pair on a new line.
2. Intermediate: Write a function that takes a dictionary of people's names and their ages,
 {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of
 people who are 21 or older.
 3. Advanced: Given a dictionary representing items in a store with their prices,
 {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes
 a list of items bought, ['apple', 'orange', 'banana', 'banana'], and
 calculates the total cost.
 4. Challenge: Write a program that counts the occurrences of each word in a given
 sentence. Example: for the sentence "hello world hello," the output should be
 {'hello': 2, 'world': 1}.

'''

'''
1. Basic: Create a dictionary with three key-value pairs representing a student's
 information: name, age, and grade. Print each key-value pair on a new line.
'''

students_info = {
    'Name': 'Keith',
    'Age': 24,
    'Grade': 7
}

for key, value in students_info.items():
    print(f'{key}: {value}')


'''
2. Intermediate: Write a function that takes a dictionary of people's names and their ages,
 {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of
 people who are 21 or older.
'''
def adults(db):
    return[name for name, age in db.items() if age >= 21]

db =  {'Alice': 24, 'Bob': 19, 'Charlie': 30}

print(adults(db))


'''
 3. Advanced: Given a dictionary representing items in a store with their prices,
 {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes
 a list of items bought, ['apple', 'orange', 'banana', 'banana'], and
 calculates the total cost.
'''

store =  {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}

items_bought = ['apple', 'orange', 'banana', 'banana']

total_cost = sum(store[items] for items in items_bought)

print(f'Total cost of items bought is {total_cost: .2f}')


'''
 4. Challenge: Write a program that counts the occurrences of each word in a given
 sentence. Example: for the sentence "hello world hello," the output should be
 {'hello': 2, 'world': 1}.
'''

sentence = 'hello world hello'

word_count = {}

for word in sentence.split(): # splitting the sentence into a list separated by commas ['hello', 'world', 'hello']
    word_count[word] = word_count.get(word, 0) +1  # This line updates the word count in the dictionary.
# Retrieves the current count of the word from the dictionary.
#If the word does not exist in the dictionary, get returns the default value of 0.

#+1 increments the word count

print(word_count)



def adults(ages):
    return[name for name, age in ages.items() if age >= 21]

people_db =  {'Alice': 24, 'Bob': 19, 'Charlie': 30}

print(adults(people_db))



def adults_age(db):
    return[name for name, age in db.items() if age > 21]
db =  {'Alice': 24, 'Bob': 19, 'Charlie': 30}

adults_age(db)