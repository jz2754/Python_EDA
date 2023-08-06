<<<<<<< HEAD
=======

>>>>>>> origin/main
# print statement

print("*")
print("**")
print("***")
print("****")
print("****")
print("***")
print("**")
print("*")
<<<<<<< HEAD
print("******************")

# variables


=======



# variables

>>>>>>> origin/main
character_name = "John"
character_age = "35"

print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
<<<<<<< HEAD

# change line
print("zhou \njingwei")

# use function
print(character_name.upper())
print(len(character_name))

# list : add, delete, remove, find

friends = ["kevin", "karen", "jim"]
lucky_numbers = [3, 4, 7]
print(friends)

print(friends[0].upper())

# tuple : can not change

coordinates = (4, 5)


# function

def sayhi():
    print("Hello User")


sayhi()


def say_hi(name):
    print("Hello " + name)


say_hi("jingwei")


# get information back from the function

def cube(num):
    return num * num * num


print(cube(3))

#  nested loop >> translation

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2]
]

for row in number_grid:
    for col in row:
        print(col)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

# comments

'''
this is a test file
try some basic python syntax

'''

# try and exception (ONLY use except would be too broad)


try:
    value = 10 / 0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError:
    print("Invalid")
except ValueError:
    print("invalid")

# file system


'''
open

set read, read + , write etc...

close
'''

# import  self-made modules

import useful_tools_test1
print(useful_tools_test1.roll_dice(99))


# import external modules













=======
>>>>>>> origin/main
