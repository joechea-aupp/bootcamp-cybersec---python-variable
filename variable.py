
# install python3
# https://www.python.org/downloads/

'''
Part 1: Introduction to Python

once installed python, you can start to write python code using REPL (Read-Eval-Print-Loop) session or create a python file.

to start REPL session, open terminal and type python3

'''

'''
Part 2: Variables
naming convention

snakecase: Words are delimited by an underscore.

variable_one
variable_two

pascalcase: Words are delimited by capital letters.

VariableOne
VariableTwo

Camelcase: Words are delimited by capital letters, except the initial word.

variableOne
variableTwo

'''

# to create variable, you can use the following syntax
# variable_name = value
apple = "iphone_15"

# variable is case-sensitive, the following code will raise an error
# print(Apple) 


'''
Part 3: String
String is a sequence of characters. In python, you can create string using single quote or double quote.

'''

pro = "_pro"
plus = "_plus"

# the apple_plus variable name is following snake_case naming convention
# the process of having 2 strings combined is called concatenation
apple_plus = apple + plus

print(apple + pro)
print(apple_plus)


fake_number = "123" + "456"
print(fake_number)

# access string via it index position
alphabet = "abcdefghijklmnopqrstuvwxyz"

a = alphabet[0]
print(a)

# access string using range of index
# starting_index:ending_index
print(alphabet[0:3])

# starting_index:ending_index:step
print(alphabet[0:3:2])

# access string using negative index
print(alphabet[-1])

# reverse string
print(alphabet[::-1])


# string method
# string method is away to manipulate string
# to see what method available for string, you can use dir method
print(dir(str))

name = "john doe"

print(name.capitalize())

print(name.find("doe"))
print(name.find("joe"))

print(name.index("doe"))
# print(name.index("joe"))

print(name.upper())
print(name.lower())

greeting = "                        hello world!                        "
print(greeting.strip())
print(greeting.strip() + "!!!")

formal_greeting = "Hello, how are you?"
print(formal_greeting.split())


# count all character in string
print(len(formal_greeting))


'''
Part 4: Number

python follow operation order (PEMDAS)
- Parentheses
- Exponents
- Multiplication and Division (from left to right)
- Addition and Subtraction (from left to right)

math operation support 
+ Add
- Subtract
/ Divide
* Multiply
% Modulus = Remainder
** Exponential
'''

print(1 + 1)
print(2 - 1)
print(2 * 2)
print(4 / 2)
print(5 % 2)
print(2 ** 3)


# exponential
print(2 ** 3)

# float number
print(2.5 + 2.5)

print(type(2/3))


# type casting
'''
int(value)
float(value)
str(value)
'''

a = 1
b = "2"

# print(a + b)
print(a + int(b))


c = 2.5
print(int(c))


'''
Part 5: List
'''
lst = []
print(type(lst))


name = ["john", "doe", "jane", "dew"]
print(name[1])


# list method
print(dir(list))

print(len(name))

# add item to the end of the list 
name.append("jack")

# add item to specific location in list
name.insert(1, "jimmy")

# remove specific item from the list 
name.remove("jane")

# remove last item from the list 
name.pop()

# sort item in a list
random_number_1 = [3, 1, 5, 2, 4]
random_number_1.sort()
print(random_number_1)

# random_number_2 = ["3", 1, "5", 2, 4]
# random_number_2.sort()
# print(random_number_2)

# reverse item in a list
short_aplhabet = ["a", "b", "c", "d", "e"]
short_aplhabet.reverse()
print(short_aplhabet)


'''
Part 6: Dictionary
Normal Dictinary (word):(Meaning) 

Key-Value Pair

- Dictionaries are collections of key-value pairs.
- They allow you to associate values (values) with unique identifiers (keys).
- Dictionaries are useful for storing structured data.

Key — fixed and unique, cannot be changed

Value — tied to the key, can be changed
'''

book = {}
print(type(book))


services = {
    'ssh': 22,
    'http': 80,
    'https': 443
}

print(services)
print(services['ssh'])

remote_service_port = 'ssh'

print(services.get(remote_service_port))

print(services.keys())
print(services.values())

# add new key-value pair
services['ftp'] = 21
print(services)

# remove key-value pair
# print(services.pop('ftp'))
# del services['ftp']


'''
Part 7: Boolean
- Booleans represent true or false values.
- They are used for decision-making and logical operations.
- Logical operators (and, or, not) allow you to combine and negate conditions.

== equals to
!= (≠) not equal to
> Greater Than
< Less Than
>= (≥) Greater than or equals to 
<= (≤) Less than or equals to
in used to check if an item can be found in another item
not in check if something is not in another item

'''
print(10 == 9)
print(10 != 9)
print(10 > 9)
print(10 < 9)

full_name = "john doe"
print("john" in full_name)
print("jane" in full_name)
print("jane" not in full_name)


