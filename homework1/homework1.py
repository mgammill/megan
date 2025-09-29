# File: homework1. py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a))
# a is an integer, a whole number with no decimals
b = 1.5
print(b)
print(type(b))
# b is a 'float,' a number with a decimal or fraction
c = 3j
print(c)
print(type(c))
# c is a 'complex,' a complex number with real and imaginary parts. 
# In python, j represents i (j^2=-1), so the c is 3i.
d = "hello"
print(d)
print(type(d))
# d is a string, a data type that holds text
e = [1, 2, 3]
print(e)
print(type(e))
# e is a list of objects. 
# In this case our list contains integrers.
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a 'dict,' or dictionary, 
# which is an unordered collection of items that can be used / referred to later.
g = (1, 2)
print(g)
print(type(g))
# g is a 'tuple,' which is an ordered collection of items.
# once a tuple has been created, you cannot change it later on.
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list of items
# in this case, our list contains string of text.
i = True
print(i)
print(type(i))
# i is a 'bool', or booleneanBoolean
# this data type holds values true or false.
j = None
print(j)
print(type(j))
# j is a 'NoneType'.
# this data type represents an absence of value.
k = [True, "blue", 12]
print(k)
print(type(k))
# k is a list.
# in this case, the list contains a bool, string, and integer.
l = str(14)
print(l)
print(type(l))
# l is a 'str', or string. This data type holds text.
# in this case, our string holds a number, but we want to treat it
# just like we would a text, rather than an integer.
m = 1e4
print(m)
print(type(m))
# m is a 'float' or a number with a decimal or fraction.
# 1e4 prints out as 10^4, or 10000.0

# --- Questions ---
# 1) How many different data types did you find?
# There were 9 different data types.
# 2) List all the data types you found.
# I found: integer, float, complex, string, 
# list, dict, tuple, bool, and NoneType.
# 3)What variables have the same data types?
# b and m are both floats.
# d and l are strings.
# e, h, and k are lists
# 4) What was the data type of 1? Why is it not an integer? What does str() do?
# The data type of l was string, because we defined l (using the specification str() )
# as the string of text containing the number 1, not the integer value 1.
# 5) Look up one more data type not given above. Repeat the same procedure.
n = range(3)
print(n)
print(type(n))
# The data type of n is 'range.'
# This data type represents a sequence of numbers from 0 to one less than
# the inputted stop value, incrementing by 1. 
# In this case range(3) represents the numbers 0, 1, and 2.

# --- Booleans ---
# a boolean is a data type in Python which returns True or False depending 
# on your code. Run each line. Next to the line, write a comment if it was 
# True or False. Describe the result.
print(10 > 9) # True, 10 is greater than 9.
print (10 == 9) # False, 10 is not equal to 9.
print(10 <= 9) # False, 10 is not less than or equal to 9.
print(bool("abc")) # True, because "abc" is a nonempty string.
print(bool(123)) # True, because 123 is a nonsero integer.
print(bool(["apple", "cherry", "banana"])) # True, beacuse the given list is nonempty.
print(bool(True)) # True, because the truth value is true:)
print(bool(False)) # False, because the true value is false.
print(bool(0)) # False, because 0 is a zero integer; it corresponds to "no" or "empty" or "false"
print(bool("")) # False, because the given string is empty.
print(bool(" ")) # True, because the given string is nonempty; it contains a space.
print(bool(())) # False, because the given tuple is empty.
print(bool([])) # False, because the given list is empty.
print(bool({})) # False, because the given dictionary is empty.
print(bool(True and False)) # False, because the bool operator only returns True if
# both operands are True.
print(bool(True and True)) # True, because both operands are True.
print(bool(False and False)) # False, because at least one operand is False.
print(bool(True or False)) # True, because at lest one of the operands is True.
print(bool(True or True)) # True, because at least one of the operands is True.
print(bool(False or False)) # False, because neither of the operands is True.
print(bool(not(False))) # True, because the truth value of not(False) is True.
print(bool(not(True))) # False, because the truth value of not(True) is False.

# --- Questions ---
# 1) What pattern do you notice about the expressions returning True or False?
# bool(X and Y) returns True only if both X and Y are True.
# bool(X or Y) returns True if at least one of X and Y are True.
# bool(notX) returns the opposite truth value of X.
# 2) Which expression surprised you about its result?
# I was surprised that bool(True and False) was false at first, because
# I expected the bool(X and Y) to return True if at least one of X and Y were
# True, not both. 
# 3) Create an expression, not given above, that will return True. Why is it True?
print(bool(not(not(True))))
# The above expression returns True because the opposite of the opposite of True
# is the opposite of False, is True.
# 4) Create an expression, not given above, that will return False. Why is it False?
print(bool(None))
# The above expression returns False because "None" is a 'false' or 'no' value.

# --- Operators ---
# An operator is a special symbol or keyword that performs operations. 
# --- Below are Arithmetic Operators ---
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division
print(5 % 2) # 1, % performs modulo division, returning the remainder of 5 upon division by 2
print(3 ** 2) # 9, ** returns exponentiation
print(15 // 2) # 7, // performs integer (or 'floor') division. This means python will
# divide 15 by 2 then get rid of the decimal part. 15 / 2 = 7.5, so 15 // 2 = 7.
# -- Below are Comparison Operators ---
print(5 == 2) # False, == compares equality
print(10 != 10) # False, != compares whether two inputs are not equal
print(2<5) # True, x<y compares whether x is less than y
print(12>5) # True, x>y compares whether x is greater than y
print(5<=6) # True, x<=y compares whether x is less than or equal to y
print(1>=10) # False, x>=y compares whter x is greater than or equal to y
# --- Below are Assignment Operators ---
x = 5
x += 5 # This updates the value of x from x to x + 5.
x -= 4 # This updates the value of x from x to x - 4
x *= 3 # This updates the value of x from x to x * 3
# ---  Logical Operator Questions ---
# 1) What does the operator 'and' do? Write an expression that results in True. 
# Write an expression that results in False. 
# The operator 'and' requires that both operands are 'truthy' in order to return True.
print(bool(1 and 2)) # This expression is True because both operands are nonzero.
print(bool(5 and 0)) # This expression is False because at least one of the operands is zero.
# 2)What does the operator 'or' do? Write an expression that results in True. 
# Write an expression that results in False.
# The operator 'or' returns True if at least one of the operands are 'truthy.'
print(bool(1 or 0)) # This expression is True because at least one of the operands is nonzero
print(bool(0 or "")) # This expression is False because neither of the operands are 'truthy'
# 3) What does the operator not do? Write an expression that resultsin True. 
# Write an expression that results in False.
# The 'not' operator returns the opposite true value of the given input.
print(not(0)) # This expression is True because the opposite of zero is a nonzero value
print(not(1)) # This expression is False because the opposite of a nonzero value is zero
# --- More Questions ---
# 1) What is the difference between / and //?
# / performs division. // performs floor division, meaning the result ommits any fractional 
# parts of the result of normal division /.
# 2) What is the difference between % and //?
# % performs modulo division, returning the remainder. // returns the quotient, as define in 1).
# 3) What operator would you use to calculate the remainder when dividing two numbers.
# Give an example.
print(7 % 3) 
# The % returns the remainder when dividing two numbers. 
# In the case above, print(7 % 3) returns the remainder when 7 is divided by 3,
# That is, the above expression prints 1, since 7 = 3(2) + 1
# 4) How do assignment operators work?
# Assignment operators change or assign a new value to a given variable according
# to the operator given.
# x *= 3 for example assigns a new value to x, one that is 3 times more than the 
# initial value of x.

# --- Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints first character: h
print(my_string[1]) # Prints second character: e
print(my_string[2]) # Prints third character: l
print(my_string[3]) # Prints fourth character: l
print(my_string[4]) # Prints fifth character: o
print(my_string[-1]) # Prints last character: o
print(my_string[1:3]) # Prints seconds and fourth character: el
print(my_string[0:5:2]) # Prints every seconds character, starting at the 
# first character and stopping up to and including the sixth character.
# That is, prints: hlo
print(len(my_string)) # Prints the length of my_string: 5
print(my_string + "goodbye") # Prints hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello
# --- Questions ---
# 1) Define the term slicing. For which of the manipulations did you slice your string?
# Slicing allows you to extract a part of sub-sequence of your string. 
# I used slicing in the manipulation: "my_string[0:5:2]", where I extracted the substring
# of my_string consisting of only every second character.
# 2) Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name) # Prints: Hello, my name is Oski
# 3) Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski
# 4) What is the difference between the two last print statments?
# The first print statment allows you to add an expression to a string,
# using a touple where you list the first string you want to print, then then next.
# The second print statement (utilizing an f-string) allows you to embed an expression, 
# in this case name = "Oski" directly into a string using curly brackets {}.

# --- Terminal Commands ---
# cd
# Change directories. Use it to move from one folder to another
# Example: cd python_decal_fa25
# ls
# List Contents. Use it to list the contents of a folder or directory
# Example: ls lecture_notes
# ls -a
# List Contents. Use it to list all contents of a folder or directory, including
# hidden ones. The -a refers to 'all'.
# Exampele: ls -a python_decal_fa25
# mkdir
# Make Directory. Use it to make a new folder or directory
# Example: mkdir homework1testfolder
# cat
# Concatenate. Use it to tell your computer to print all contents of a file.
# Example: cat functions.py
# pwd
# Print Working Directory. Use this to sould the file path to your current directory.
# Example: pwd
# cd ..
# Change Directories. Use this to move up to a parent directory
# Example: cd ..
# cd .
# Change Directories. Use this to change directories to your current directory 
# (Useful to reference your current directory explicitly)
# Example: cd .
# cd ~
# Change Directory. Use this to move into your home directory.
# Example: cd ~
# cp
# Copy. Use this to copy a file or directory
# Example: cp homework1testfolder
# mv
# Move. Use this command to move a file or directory
# Example:  mv ~/python_decal_fa25/megan/homework1/homework1testfolder ~/python_decal_fa25/lecture_notes
# rm
# Remove. This command permanently deletes a file or folder
# Example: rmdir homework1testfolder
# clear
# Clear. Use this command to erase the previous outputs on your screen and reset your curser to the top lest of the screen.
# Example: clear
# grep
# Global Regular Expression Print. Use this to print all lines of a file that contain the given expression or string.
# Example: grep "def" functions.py

# --- Questions ---
# 1) Look up 3 other commands cont present. Define and explain how to use them on the commmand line.
# touch
# Touch. Use this command to create a new file.
# Example: touch hwtestfile
# head
# Head. Use this command to print the beginning contents of a file.
# Example: head functions.py
# history
# History. Use this command to print a list of all the commands you have recently executed in your terminal
# Example. history
# 2) What is the difference between ls and ls -a?
# ls prints all contents of a file or directory. 
# ls -a prints all contents of a file or directory, including hidden ones.
# 3) What is a hidden file?
# a hidden file is a file whose name sates with a (.) By default, these files are not displated when you call ls.
# 4) Look up 3 other flags. Define and explain how to use them on the command line.
# mkdir -p: This makes a new directory and parent directories as specified.
# For example, if you wanted to create a new directory test_child inside a new directory test_parent,
# you would call mkdir -p test_parent/test_child
# rm -r: To remove a directory and all the files an subdirectories inside it, you can use the rm command with a -r flag.
# For example, to delete the previously created parent and child directories, you can call
# rm -r test_parent
# grep -n: This prints all lines of a file that contain the given expression or string,
# and includes their corresponding line numbers.