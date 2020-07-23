# UltraQuickPythonRefresher

# Basic_python: (Ultra quick Tutorial )


print(1 + 1)     # addition(+)
print(2 - 1)     # subtraction(-)
print(6 * 3)     # multiplication(*)
print(4 / 2)     # division(/)
print(3 ** 2)    # exponential(**)  /  power
print(5 % 2)     # modulus(%)
print(3 // 2)     # Floor division operator(//)


# Data Types:
# Numeric Data-Types

print(type(2))  # Int
print(type(3.1415926535))  # float


# Sequence Types

print(type("yolo"))  # String
print(type([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # list
print(type())  # Tuples


# Dictionary
print(type({‘name’: ‘your-name’}))  # Dictionary
print(type())     #


# Variables:

first_name = "Tom"  # declaring string to variable name "first_name"
last_name = "Cr00se"  # declaring string to variable name "last_name"
Full_name = first_name + last_name  # String concatenation
Age = 9  # declaring integer to variable name "Age"
employed_status = True  # declaring boolean value to variable name "employed_status"
Programming_knowledge = [‘Python’, ’Java’, ’c  # ’,’c’,’Javascript’] #assigning list to variable.                                                                                                      name "Programming_knowledge"
Description = {  # assigning dictionary to variable name Description
‘First_name(Key) ’: ’Tom’(value),  # dictionaries have key value pairs
‘last_name ’: ’Cr00se’,
‘Age ’: 9,
}


# Printing the values stored in the variables:

print("My First name is ", First_name)  # Prints: My First name is Tom
print("My last name is ", last_name)  # Prints: My last name is Cr00se
print("My Full name is ", Full_name)  # Prints: My Full name is TomCr00se
# Prints length of full name: 9
print("My length of full name is ", len(Full_name))
print("Age is ", Age)  # Prints: Age is 9
print("Employed Status", employed_status)  # Prints: Employed Status True


# Arithmetic Operation in python

# Integer Operation

print("Addition in python ", 1+1)
print("Subtraction in python ", 1-1)
print("Multiplication in python ", 1*1)
# while dividing two integer it gives float as output
print("Division in python ", 1/1)
print("Addition in python ", 1+1)


# Float Operation

print('Value of PI', 3.1415926535897)

# Complex numbers

print('Complex number : ', 1+1j)
print('Multiplying complex number: ', (1+1j) * (1-1j))


# Playing with variables

a = 3  # declaring integer to variable name "a"
b = 2  # declaring integer to variable name "b"
sum = a + b                                          # declaring result to the variables
difference = a - b
multiplication = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b  # squares,cubes…

print('a + b = ', sum)
print('a - b = ', difference)
print('a * b = ', multiplication)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)



# Calculate Area of circle:
 	#	pseudo code
   # Assign the value of  radius
  #  areaOfCircle is pi * radius ^ 2
  #  Print it
# Code

Radius = 20
Pi = 3.14
AreaOfCircle = Pi * Radius ** 2
print("The area of Circle is: ", AreaOfCircle)


# Calculate Area of rectangle:
 	#	pseudo code
  #  Assign the length
 #   Assign the width
 #   areaOfRectangle is length * width
 #   Print it
# Code

length = 20
Width = 40
AreaOfRectangle = length * width
print("The area of Rectangle is: ", AreaOfRectangle)


# Boolean Operation

print(1 > 2)  # False
print(1 < 2)  # True
print(1 == 2)  # False      "==" is an comparison operator (it compares)
print(1 != 2)  # True        "!="  is not equal to
# False #compares the length of both string
print(len("tomCroose") == len("DonaldDuck"))
print(len("python") < len("potatoHeadYolo"))  # True


# Boolean comparison

print('5 is 5', 5 is 5)                  		 # True
print('5 is not 6', 5 is not 6)          		 # True
print('P in Pramit', 'P' in 'Pramit')    	 # True
print('L in Pramit', 'L' in 'Pramit') 		# False
print('started' in 'lets get started') 		# True
print('9 is 3 ** 2:', 9 is 3 ** 2)   		# True
print(not False)     				# True
print(not not True)  				# True
print(not not False) 				# False
print('True and True: ', True and True)  # True
print('True or False:', True or False)  # True



# MultiLine String:

# This_is_multiline_string= ‘’’This ia multiline string
# And i can write where ever I
# Want’’’

# Unpacking Character:

	Name = "TomCroose"
	a, b, c, d, e, f, g, h, i = Name
	print(a)  # It print "T"
    print(b)  # It print "o"
	print(c)  # It print "m"
	print(d)  # It print "C"
    print(e)  # It print "r"
    print(f)  # It print "o"
    print(g)  # It print "o"
	print(h)  # It print "s"
	print(i)  # It print "e"


# Accessing by Index:

name = "TomCroose"
First_character = name[0]
print(First_character)            	 # print out "T"

Second_character = name[1]
print(Second_character)             	# print out "o"

Third_character = name[2]
print(Third_character)             	# print out "m"

fourth_character = name[3]
print(fourth_character)             	# print out "C"

Fifth_character = name[4]
print(Fifth_character)            	 # print out "r"
………..

# Slicing the string:

name = "TomCroose"
Four_slice = name[0:4]  # Slice character upto fourth but it doesn't include fourth one
print(Four_slice) 		  # prints out "TomC"

last_slice = name[3:7]  # Slice character from third index to seventh one but not seventh
print(last_slice)                  # prints out "Croo"




# Escaping the string (Escape character):

print("I am bond \n james \n bond")  # break lines

# Prints: I am bond
	    james
	    bond
print(" I am bond \t james \t bond")  # create tab spaces
# Prints: I am bond		james		bond


# Capitalize first character of string by using .capitalize() :

character = "i am not a james bond "
print(character.capitalize())       		# " I am not james bond"


# Count the character of string by using .count() :

character = "i am not a james bond "
print(character.count(‘a’))       		# There are "3" "a" in character



# Replacing tabs character with spaces by using .expandtabs() :

character = "i \t am \t not \t a \t james \t bond "
							# output

# i 		am 	   not 	    a 	   james 	  bond
print(character.expandtabs(5))

# i 		am 	    not 	  	  a 	   james            bond
print(character.expandtabs(10))



# Find the index position of the string by using .find() :

character = "i am not a james bond "

# prints out " 5 "  (spaces are also being counted)
print(character.find("n"))


# Using .format() to format the output in meaningful way:

length = 20
Width = 40
AreaOfRectangle = length * width
print("{} is the area of Rectangle: " .format(str(AreaOfRectangle)))

first_name = "tom"
last_name = "croose"
print("{} is the very good bouy and he likes to {}: " .format(first_name, last_name))



# check whether given string is alphabet or not by using isalpha():

first_name = "tom"
print(first_name.isalpha())     # True

first_name = 69
print(first_name.isalpha())     # False


# check whether given string is digit or not by using isdigit():

first_name = "tom"
print(first_name.isdigit())     # False

first_name = 69
print(first_name.isdigit())     # True

# check whether given string is uppercase or not by using isupper():

first_name = "TOM"
print(first_name.isupper())     # True

first_name = "tom"
print(first_name.isupper())     # False



# Replacing the substring by using replace():

Coding_practice = "I have no idea what I am doing"
print(Coding_practice.replace("no", "yes")  # replaces no with yes



# Splitting the substring by using split():

Coding_practice="I have no idea what I am doing"
# ['I', 'have', 'no', 'idea', 'what', 'I', 'am', 'doing']
print(Coding_practice.split())



# Check whether given string start with certain string by using startswith():

Coding_practice="The world is in Complete chaos"

print(Coding_practice.startswith("The"))			# True

# Creating an empty list:

empty_list=list()
or
empty_list=[]

print(len(empty_list))  # Its length is "0" cause list is empty


# Creating a list called programming languages:

programming_languages=["Python", "Java", "C", "C  # "]

print("List of Programming languages: ", programming_languages)
print("Number of programming languages: ", len(programming_languages))


# Accessing the items from the list called programming languages:

programming_languages=["Python", "Java", "C", "C  # "]

Java_language=programming_languages[1]
print(Java_language)  # prints: "Java"

C_language=programming_languages[2]
print(C_language)  # prints: "C"

Last_items_from_list=programming_languages[-1]
print(Last_items_from_list)  # prints: "C#"

SecondLast_items_from_list=programming_language[-2]
print(SecondLast_items_from_list)  # prints: "C"




# Slicing the list items from the list called programming language:

programming_language=["Python", "Java", "C", "C  # "]

All_language=programming_language[0:4]
print(All_language)  # prints out all the list



# Manipulating the list:

programming_language=["Python", "Java", "C", "C  # "]

Programming_language[1]="Kotlin"
print(programming_language)  # Prints out ["Python","Java","Kotlin","C#" ]



# checking the items whether its in list or not:

programming_language=["Python", "Java", "C", "C  # "]

Existence_check="Python" in programming_language

print(Existence_check)  # True


# Appending the items in the list using append():

programming_language=["Python", "Java", "C", "C  # "]

programming_language.append("matlab")

print(programming_language)  # Prints out ["Python","Java","C#","matlab" ]


# Inserting the items in the list using insert():

programming_language=["Python", "Java", "C", "C  # "]

# inserts "matlab" between python and java
programming_language.insert(1, "matlab")

print(programming_language)  # Prints out ["Python","matlab","Java","C","C#"]



# Removing the items in the list using remove():

programming_language=["Python", "Java", "C", "C  # "]

programming_language.remove("Java")

print(programming_language)  # Removes the "java" from the list


# using del to remove:

programming_language=["Python", "Java", "C", "C  # "]

del programming_language[1]

print(programming_language)  # prints output as "["Python","C","C#" ]"



# using copy() to copy the entire list:

programming_language=["Python", "Java", "C", "C  # "]

copyOf_programming_language=programming_language.copy()

print(copyOf_programming_language)


# clearing the entire list by using clear():

programming_language=["Python", "Java", "C", "C  # "]

programming_language.clear()

print(programming_language)  # Prints empty list


# Joining with extend():

number1=[1, 2, 3, 4, 5, 6, 7]

number2=[8, 9, 10]

number1.extend(number2)

print("Total Numbers: ", number1)  # Prints: [1,2,3,4,5,6,7,8,9,10]



# counting in list using count():

number1=[11, 21, 11, 4, 11, 6, 11]

print(number1.count(11))  # prints out "4"


# Using index() to find the index position:

number1=[11, 21, 14, 4, 16, 7, 199]

print(number1.index(14))  # prints out "2"

# Using reverse() to reverse the list:

programming_language=["Python", "Java", "C", "C  # "]

programming_language.reverse()

print(programming_language)  # prints out the reverse of the list



# Using sort() to sort the list:

programming_language=["Python", "Java", "C", "C  # "]

programming_language.sort()

print(programming_language)  # prints out list in sorted order



# Using sort(reverse=True) to reverse sort the list:

programming_language=["Python", "Java", "C", "C  # "]

programming_language.sort(reverse=True)

print(programming_language)



# Creating an empty tuple:

empty_tuple=tuple()
or
empty_tuple=()

print(len(empty_list))  # Its length is "0" cause its an empty tuple


# Accessing the items in the tuple:

progarmming_tuple=("python", "Java", "C’, "C  # ")

First_tuple=progarmming_tuple[0]

Second_tuple=progarmming_tuple[1]

Third_tuple=progarmming_tuple[2]

Fourth_tuple=progarmming_tuple[3]


# Accessing the last items in the tuple:

progarmming_tuple=("python", "Java", "C’, "C  # ")

Tuple_last=progarmming_tuple[-1]

or
progarmming_tuple=("python", "Java", "C’, "C  # ")

Last_tuple_index=len(progarmming_tuple) - 1

Last_tuple=progarmming_tuple[Last_tuple_index]

print(Last_tuple)


# Slicing the tuple :

progarmming_tuple=("python", "Java", "C’, "C  # ")

All_tuple=progarmming_tuple[0:4]  # prints out all the items

or

All_tuple=progarmming_tuple[0:]  # prints out all the items


# Slicing the range of negative index in tuple:

progarmming_tuple=("python", "Java", "C’, "C  # ")

All_tuple=progarmming_tuple[-4:]
print(All_tuple)  # prints out all the items

Middle_tuple=progarmming_tuple[-3:-1]
print(Middle_tuple)  # print out the middle ones


# Converting tuple to list:

progarmming_tuple=("python", "Java", "C’, "C  # ")

Convert_to_list=list(progarmming_tuple)

print(Convert_to_list)  # convert tuple into list




# Joining two tuple :

tuple1=("python", "Java", "C’, "C  # ")

tuple2=("javascript", "kotlin", "coq’, "matlab")

combine_tuple=tuple1 + tuple2

print(combine_tuple)

# Checking an item in tuple whether it exist or not:

programming_tuple=("python", "Java", "C’, "C  # ")

# Prints "True" cause python exist in programming_tuple
"python" in programming_tuple

"GoLang" in programming_tuple  # Prints "False" cause it dose not exist

# Deleting the entire tuple using del :


tuple1=("python", "Java", "C’, "C  # ")

del tuple1  # deletes tuple1

tuple2=("javascript", "kotlin", "coq’, "matlab")

del tuple2  # deletes tuple2


# Creating an empty set:

empty_set=set()
or
empty_set={}

print(len(empty_set))  # Its length is "0" cause its an empty set


# Creating and adding items in set:

programming_set={"python", "java", "C", "C  # "}

print(programming_set)  # prints out "{"python","java","C","C#" }

programming_set.add("coq")

print(programming_set)  # prints out "{"python","java","C","C#","coq" }


# Adding multiple items in set using update():

programming_set={"python", "java", "C", "C  # "}

# Insert entire items
Programming_set.update(["matlab", "javascript", "go", "ruby"])

# prints out {'matlab', 'python', 'ruby', 'javascript', 'java', 'C#', 'C', 'go'}
print(programming_set)


# Removing from set using remove() or discard():

programming_set={"python", "java", "C", "C  # "}

programming_set.remove("java")
or
programming_set.discard("java")

print(programming_set)  # Removes java from the items list

# Removing last item using pop():

programming_set={"python", "java", "C", "C  # "}

programming_set.pop()

print(programming_set)  # removes the last item and print the rest of the set


# Deleting the entire set using del:

programming_set={"python", "java", "C", "C  # "}

del programming_set 			# deletes the entire set


# Merging or Joining the entire set using union() or update():

programming_set={"python", "java", "C", "C  # "}

programming_set_2={"matlab", "javascript", "go", "ruby"}

Merge_set=programming_set .union(programming_set_2)

print(Merge_set)  # Joins two set into one



# Finding the common items in the set using intersection:

programming_set={"python", "java", "C", "C  # "}

programming_set_2={"python", "java"}

Common_items=intersection(programming_set_2)

print(Common_items)  # prints out  { "python","java" }



# Checking the subset and super set using issubset() and issuperset():

programming_set={"python", "java", "C", "C  # "}

programming_set_2={"python", "java"}

programming_set_2.issubset(programming_set)  # True

programming_set.issuperset(programming_set_2)  # True

# Finding out the difference between two sets using difference():

programming_set={"python", "java", "C", "C  # "}

programming_set_2={"python", "java"}

programming_set_2.difference(programming_set)  # Prints out "{"C","C#"}


# Finding out the symmetric_difference() between two sets:

programming_set={"python", "java", "C", "C  # "}

programming_set_2={"python", "java"}

programming_set_2.symmetric_difference(
    programming_set)  # Prints out "{"C","C#"}

Or(simple example)

Name={"t", "o", "m"}

Last_name={"c", "r", "o", "o", "s", "e"}

Name.symmetric_difference(Last_name)

print(Last_name)  # prints out {'c', 'r', 's', 'o', 'e'}
