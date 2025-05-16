# Task 1
fruit = ['apple','banana', 'lemon', 'orange', 'melon']
fruit[2]

  # Task 2
lst1 = [1,34,6,7,32]
lst2 = [4,12,43,10,8]
lst1.extend(lst2)
print(lst1)

# Task 3
lst=[1, 4, 5, 2, 8]
first = lst[0]
middle = lst[len(lst)//2]
last = lst[-1]
result = [first, middle, last]
print( result)

  # Task 4
Movie = ["Inception", "The Dark Knight", "Parasite", "Interstellar", "Get Out"]
Movies_Tuple = tuple(Movie)
print(Movies_Tuple)

# Task 5
City = ['London', 'Rim', 'Paris']
if 'Paris' in City:
    print('Paris is in the list')
else:
    print('Paris is not in the list')

  # Task 6
numbers = [1,2,3,4,5]
num = numbers*2
print(num)

  # Task 7
number = [1,2,3,4,5]
number[0], number[-1] = number[-1], number[0]
print('numbers after swapping:', number)

# Task 8
my_tuple = tuple(range(1,11))
slice_part = my_tuple[3:7]
print('Full tuple:', my_tuple)
print('Sliced tuple:', slice_part)

  # Task 9
colors = ['red', 'orange', 'blue', 'white', 'blue']
count_blue = colors.count('blue')
print('The color blue appears', count_blue, 'times')

  # Task 10
Animals = ('cat', 'lion', 'tiger', 'puma')
lion=Animals.index('lion')
print('Indeks of lion:', lion)

  # Task 11
tuple1 = (1,2,3,4,5,6)
tuple2 = (9,8,7,6,5,4)
merged_tuple = tuple1+tuple2
print(merged_tuple)

  # Task 12
list3 = [1,3,5,7,9]
tuple3 = (3,5,7,3)
list3_length = len(list3)
tuple3_length = len(tuple3)
print(f'Length of the list:', list3_length)
print(f'Length of the tuple:', tuple3_length)

  # Task 13
tuplee = (2,3,7,5,4,8)
list_to_tuple = list(tuplee)
print(f'Tuple:', tuplee)
print(f'Converted list:', list_to_tuple)

  # Task 14
tuple0 = (1,2,3,4,5)
tuple_min = min(tuple0)
tuple_max = max(tuple0)
print(f'Max value:', tuple_max)
print(f'Min value:', tuple_min)

  # Task 15
words = ("apple", "banana", "cherry", "date", "elderberry")
reversed_words = words[::-1]
print("Original tuple:", words)
print("Reversed tuple:", reversed_words)
