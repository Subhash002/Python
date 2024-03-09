from math import sqrt, ceil

name = input("Enter your name: ")
print(f"Hello, {name}!")

num1=input("Number")
num2=input("Number2")
sum=num1+num2
diffs=num1-num2
product=num1*num2
quotient=num1/num2
print(f"{product}")

for i in range(5):
    print(i)

count=0
while count<10:
    print(count)
    count+=1

fruits = ["apple", "banana", "cherry"]
fruits.append("pineapple")

for fruit in fruits:
    print(fruit)


cordinates =(1.2.3.4)
x,y=cordinates
print(f"X: {x} y: {y}")

person={"name": "John", "age":20, "gender": "M"}
print(person["name"])

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(full_name)

age = 30
name = "Alice"
message = "Hello,{}! you are {} years old".format(name, age)
print(message)


text = "Hello, World!"
substring = text[7:12]  # From index 7 (inclusive) to 12 (exclusive)

print(substring)



text=" This is a string "
trimmed_text=text.strip()

text_word_check="Python is amazing tool to play with but less than Javascript"
isPresent="tool" in text_word_check.strip().lower()
print(isPresent)

text = "Hello, World!"
new_text = text.replace("World", "Python")

print(new_text)


text = "apple,banana,cherry"
fruits = text.split(",")

print(fruits)


text = "Python is a powerful language"
index = text.find("powerful")

print(index)  # -1 if not found

greeting = "Hello" * 3

print(greeting)


for i in range(100):
    if i%2 == 0:
        continue
    print(i)

if True:
    pass

numbers= [x in range(100) if x%2==0]

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an element
fruits.insert(3, "burberry")
fruits.remove("orange") # Remove an element
del fruits[0]

person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:
    print(key, person[key])  # Looping through keys and values

for value in person.values():
    print(value)  # Looping through values only

for key, value in person.items():
    print(key, value)  # Looping through key-value pairs


my_set = {1, 2, 3}
my_set.add(4)  # Add an element
my_set.remove(2)  # Remove an element (raises KeyError if not found)
my_set.discard(5)  # Remove an element if present (no error if not found)

print(my_set)
my_frozen_set = frozenset({1, 2, 3})
# my_frozen_set.add(4)  # Error: cannot modify frozen set

print(my_frozen_set)


my_set = {1, 2, 3}
is_present = 4 in my_set

print(is_present)


with open("data.txt", 'w') as file:
    file.write("Behanchod sala kya backchodi ho raha han ye sab maa choid denge tumhari hum maza aa raha na ish keyboard me loude ye jo maza han hum sabko dena chahte han samjhe Papu sala madarchod han loude ka baal hain")
with open("data.txt", 'r') as file:
    contents=file.read()
    print(contents)

try:
    with open("data.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("The 'finally' block always executes.")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, {self.name}!")
person1=Person("Subhash", "24")
person.gret()

# Encapsulation hiding the object atrributes
class Point:
    def __init__(self, x, y):
        self.__x = x  #


class Product:
    def __init__(self, name, price):
        if len(name) < 3:
            raise ValueError("Product name must be at least 3 characters long.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        self.name = name
        self.price = price

try:
    product1 = Product("Pen", 1.50)
    print(product1.name, product1.price)
except ValueError as e:
    print(e)

today = datetime.date.today()  # Get the current date
print(today.strftime("%B %d, %Y"))  # Format the date (e.g., October 27, 2023)

current_time = datetime.datetime.now()  # Get the current date and time
print(current_time.strftime("%H:%M:%S"))  # Format the time (e.g., 16:10:32)

#  Other operations: adding/subtracting days, comparing dates, etc.
current_time2=datetime.datetime.now()
print(current_time2.strftime("%H:%M:%S"))