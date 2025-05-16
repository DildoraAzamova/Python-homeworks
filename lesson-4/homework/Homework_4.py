# Dictionary Exercises Task 1
import operator

# Sample dictionary
my_dict = {'apple': 10, 'banana': 5, 'cherry': 7, 'date': 3}

# Sort dictionary by value (ascending)
ascending = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))

# Sort dictionary by value (descending)
descending = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))

# Print results
print("Ascending order by value:", ascending)
print("Descending order by value:", descending)

# Dictionary Exercises Task 2
my_dic1 = {0: 10, 1: 20}
my_dic1[2]=30
print(f'Updated dictionary:',my_dic1)

# Dictionary Exercises Task 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dic = {**dic1, **dic2, **dic3}
print(f'Merged dictionary:', merged_dic)

# Dictionary Exercises Task 4
n = int(input('Enter number:'))
square_dic = {x: x*x for x in range(1,n+1)}
print(square_dic)

# Dictionary Exercises Task 5
x=15
n=1
square_dic1 = {x: x**2 for x in range(1,16)}
print(square_dic1)

# Set Exercises Task 1
my_set = {'Sara', 'Lusy', 'Elis'}

# Set Exercises Task 2
my_set = {'Sara', 'Lusy', 'Elis'}
for a in my_set:
    print(a)

# Set Exercises Task 3
my_set = {'Sara', 'Lusy', 'Elis'}
my_set.add(10)
print(my_set)

# Set Exercises Task 4
my_set3 = {'Sara', 'Lusy', 'Elis', 'Anna'}
removed_item=my_set3.remove('Sara')
print(my_set3)

# Set Exercises Task 5
my_set2 = {"apple", "banana", "cherry"}
item_to_remove = "banana"

if item_to_remove in my_set2:
    my_set2.remove(item_to_remove)
    print(f'"{item_to_remove}" was removed.')
else:
    print(f'"{item_to_remove}" not found in the set.')

print("Updated set:", my_set2)
