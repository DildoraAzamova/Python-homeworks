# Task 1
from datetime import datetime
a=input('Enter your name:')
b=int(input('Enter your year of birth:'))
current_year = datetime.now().year
c=current_year-b
print(f"Hello, {a}! Your are {c} years old.")

# Task 2
txt='LMaasleitbtui'
Car1=txt[1::2]
Car2=txt[0::2]
print(Car1)
print(Car2)

# Task 3
txt='MsaatmiazD'
Car1=txt[1::2]
Car2=txt[0::2]
print(Car1[::-1])
print(Car2)

# Task 4
txt = "I'am John. I am from London"
# Extract part after 'from'
residence = txt.split('from')[-1].strip()
print("Residence area:", residence)

# Task 5
a=input("Enter text:")
print(a[::-1])

# Task 6
vowels="Hello World"
o=vowels.count('o')
e=vowels.count('e')
i=vowels.count('i')
a=vowels.count('a')
u=vowels.count('u')
print(a+e+i+o+u)

# Task 7
Number=input("Enter numbers :")
num= list(Number.split())
m=max(num)
print(m)

# Task 8
a=input("Enter a word")
if a==a[::-1]:
    print("The word is palindrome")
else: print("The word is not palindrome")

# Task 9
e=input("Enter email:")
a= e.index('.')
print(e[a+1::])

# Task 10
import random
import string
password_length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))
print("Generated password:", password)
