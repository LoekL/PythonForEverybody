[Programming for Everybody (Python)]

You cannot use reserved words as variable names/identifiers. 

x = 2
x = x + 2 
print x 

x == variable
= == operator
2 == constant
print == reserved word

[Command Line]
# cat                   --> show file
# ls 				  	--> list all files
# cd 				  	--> change directory
# pwd 				  	--> print working directory
# ls -l 			  	--> get more info of the files
# python firstprog.py 	--> run the prog using python

Tips
# Write part of the command and press tab to pull up closest match
# Press up or down arrow to go through previous commands

[Programming Paragraphs]

# Interactive --> you type directly to Python one line at a time and it responds
# Script --> you enter a sequence of statements (lines) into a file using a text editor and tell Python to execute the statements in the file

[Program Steps / Program Flow]

# Like a recipe or installation instructions, a program is a sequence of steps to be done in order
# Some steps are conditional - they may be skipped
# Sometimes a step or group of steps are to be repeated
# Sometimes we store a set of steps to be used over and over as needed several places throughout the program

-- Conditional Steps

if x < 10 # if true we do the indented bit
   print 'Smaller'

-- Repeated Steps

n = 5
while n > 0:
	print n
	n = n - 1
print 'Blastoff!'

[Expressions]

# Constants
- Fixed values such as numbers, letters and strings are called "constants", because their value does not change
- Numeric constants are as you expect
- String constants use single-quotes '' or double quotes ""

# Variables
- A variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable "name"
- Programmers get to choose the name of the variable
- You can change the contents of a variable in a later statement
- Name rules
+ Must start with a letter or underscore _
+ Must consist of letters and numbers and underscores
+ Case Sensitive
- You can not use reserved words as variable names/identifiers

Operator Precedence rules
- Highest precedence rule to lowest precedence rule
+ Paranthesis are always respected
+ Exponentiation (raise to a power)
+ Multiplication & Division & Remainder (%)
+ Addition & Subtraction
+ Left to right (all else equal)

Python Integer Division
print 10/2
#=> 5
print 9/2
#=>  4
print 99/100
#=> 0
print 10.0/2.0
#=> 5.0
print 99.0 / 100.0
#=> 0.99 

--> mixing float & integer == float

[Types]

What does 'Type' mean?
- In Python variables, literals, and constants have a 'type'
- Python knows the difference between an integer number and a string
- For example '+' means 'addition' if something is a number and 'concatenate' if something is a string

type() # checks the type
int() --> to integer
str() --> to string
float() --> to float

# User Input
- We can instruct Python to pause and read data from the user using the raw_input function
- The raw_input function returns a string
 nam = raw_input('Who are you?')
 print 'Welcome', nam

String Operations
- Some operators apply to strings:
+ '+' implies concatenation
+ '*' implies multiple concatenation
- Python knows when it is dealing with a string or a number and behaves appropriately

Variable names
- mnemonic --> choose names so that they remind you of what they are

[Conditional Statements]

- Python cares a lot about how far a line is indented. If you mix tabs and spaces, you may get 'indentation errors', even if everything looks fine. 
- Multi-Way if --> using elif. Order matters --> it stops execution whenever it hits true. 

[Try / Except Structure]

- You surround a dangerous section of code with try and except 
- If the code in the try works - the except is skipped
- If the code in the try fails - it jumps to the except statement

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print 'First', istr

--> stopping your program: quit()

[Functions]

- Are reusable pieces of code. 
- Stored and reused steps.

- There are two kinds of functions in python
A - Built-in functions that are provided as part of Python
B - User-defined functions that we define and use ourselves
- We treat the names of built-in functions as additional reserved words

- In Python a function is some reusable code that takes arguments() as input, does some computation, and then returns result(s)
- We define a function using the def reserved word
- We call/invoke the function by using the function name, paranthesis and arguments in an expression

big = max('Hello world')

- A function is some stored code that we use. A function takes some input and produces an output. 

Building our Own Functions

- We create a new function using the def keyword followed by optional parameters in parenthesis.
- We indent the body of the function.
- This defines the function but does not execute the body of the function.

def print_lyrics():
	print "I'm a lumberjack and I'm okay."
	print "I sleep all night and I work all day."

Arguments

- An argument is a value we pass into the function as its input when we call the function.
- We use arguments so we can direct the function to different kinds of work when we call it at different times. 
- We put the arguments in parenthesis after the name of the function.

Parameters

- A parameter is a variable which we use in the function definition that is a 'handle' that allows the code in the function to access the arguments for a particular function invocation.

def greet(lang):
	if lang == 'es':
		return 'Hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'

>>> print greet('en'),'Glenn'
#=> Hello Glenn

lang == parameter
'en' == argument

Return values

- Often a function will take its arguments, do some computation and return a value to be used as the value of the function call in the calling expression. The return keyword is used for this.
- A 'fruitful' function is one that produces a result (or return value) -- the opposite is called 'void'.
- The return statement ends the function execution and 'sends back' the result of the function.

def greet():
	return 'Hello'

print greet(), 'Glenn'
#=> Hello Glenn

Multiple Paramaters / Arguments

- We can define more than one parameter in the function definition.
- We simply add more arguments when we call the function.
- We match the number and order of arguments and parameters.

Void (non-fruitful) Functions

- When a function does not return a value, we call it a 'void' function
- Functions that return values are 'fruitful' functions
- Void functions are not fruitful

To function or not to function

- Organize your code into 'paragraphs' - capture a complete thought and 'name it'
- Do not repeat yourself - make it work once and then reuse it
- If something gets too long or complex, break up logical chunks and put those chunks in functions.
- Make a library of common stuff that you do over and over - perhaps share this with your friends. 

Which line of the following Python program is useless?

def stuff():
    print 'Hello'
    return
    print 'World'

stuff()

--> The print 'World' will never execute because it is after the return statement.

[Loops and Iteration]

- Loops (repeated steps) have iteration variables that change each time through a loop. 
- Often these iteration variables go through a sequence of numbers.

n = 5
while n > 0:
	print n
	n = n - 1
print 'Blastoff!'
print n 
#=> 5, 4, 3, 2, 1, Blastoff!, 0

- Infinite loop (avoid):

n = 5
while n > 0:
	print 'Lather'
	print 'Rinse'
print 'Dry off!'

- Breaking out of a Loop
+ The break statement ends the current loop and jumps to the statement immediately following the loop
+ It is like a loop test that can happen anywhere in the body of the loop

while True:
	line = raw_input('>')
	if line == 'done':
		break
	print line
print 'Done!'

- Finishing an Iteration with continue
+ The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

while True:
	line = raw_input('>')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print line
print 'Done!'

> hello there 
hello there
> # don't print this
> print this!
print this!
> done
Done!

A - Indefinite Loops --> while
+ While loops are called "indefinite loops" becaue they keep going until a logical condition becomes False
+ The loops we have seen so far are pretty easy to examine to see if they will terminate or if they will be "infinite loops"
+ Sometimes it is a little harder to be sure if a loop will terminate

B - Definite Loops --> for
+ Quite often we have a list of items of the lines in a file - effectively a finite set of things
+ We can write a loop to run the loop once for each of the items in a set using the Python for construct
+ These loops are called "definite loops" because they execute an exact number of times
+ We say that "definite loops iterate through the members of a set"

for i in [5,4,3,2,1]:
	print i
print 'Blastoff!'

#=> 5 4 3 2 1 Blastoff!

friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
	print 'Happy New Year:', friend

print 'Done!'

- Definite loops (for loops) have explicit iteration variables that change each time through a loop. These iteration variables move through the sequence or set.

- Looking at in 
+ The iteration variable (i) 'iterates' through the sequence (ordered set)
+ The block (body) of code is executed once for each value in the sequence
+ The iteration variable moves through all of the values in the sequence (list)

[Loop Idioms]

- Loop Idioms What We Do in Loops
- Making 'smart' loops
+ The trick is 'knowing' something about the whole loop when you are stuck writing code that only sees one entry at a time

- Finding the largest value

largest_so_far = -1
print 'Before', largest_so_far
for the_num in [9,41,12,3,74,15]:
	if the_num > largest_so_far
	largest_so_far = the_num
print largest_so_far, the_num

print 'After', largest_so_far

+ We make a variable that contains the largest value we have seen so far. If the current number we are looking at is larger, it is the new largest value we have seen so far. 

- Counting in a Loop

zork = 0 
print 'Before',zork
for thing in [9,41,12,3,74,15]:
	zork = zork + 1
    print zork, thing
print 'After',zork

+ To count how many times we execute a loop we introduce a counter variable that starts at 0 and we add one to it each time through the loop.

- Summing in a Loop

zork = 0 # running total
print 'Before',zork
for thing in [9,41,12,3,74,15]:
	zork = zork + thing
    print zork, thing
print 'After',zork

+ To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop.

- Finding the Average in a Loop
count = 0 
sum = 0 
print 'Before',count,sum
for value in [9,41,12,3,74,15]:
	count = count + 1
	sum = sum + value
	print count, sum, value
print 'After',count,sum,sum/count

+ An average just combines the counting and sum patterns and divides when the loop is done.

print 'Before'
for value in [9,41,12,3,74,15]:
	if value > 20:
		print 'Large number', value
print 'After'

+ We use an if statement in the loop to catch / filter the values we are looking for.

- Search Using a Boolean Variable

found = False
print 'Before', found
for value in [9,41,12,3,74,15]:
	if value == 3:
		found = True
	print found, value

print 'After', found

+ If we just want to search and know if a value was found - we use a vraibale that starts at False and is set to True as soon as we find what we are looking for. 

[Largest and Smallest]

smallest = None
print 'Before'
for value in [9,41,12,3,74,15]:
	if smallest is None:
		smallest = value # first iteration
	elif value < smallest:
		smallest = value
	print smallest, value

print 'After', smallest

+ We still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest.

- The 'is' and 'is not' Operators -- use it to check for special constants (True/False/None)
+ Python has an is operator that can be used in logcial Expressions
+ Implies 'is the same as' (in type and value)
+ Similar to, but stronger than == 
+ 'is not' also a logical operator

[Worked Exercise 5.1]

===

count = 0 
total = 0

while True:
	inp = raw_input('Enter a number: ')

	# Handle edge cases
	if inp == 'done':
		break
	if len(inp) < 1 :
		break

	# Do the work

	try: 
		num = float(inp)
	except:
		print "Invalid input"
		continue
	count = count + 1
	total = total + num
	print num, total, count

print 'Average:', total / count

====

largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    if len(inp) < 1: break
    
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
     
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
        
    if smallest is None:
        smallest = num
    elif num < smallest:
         smallest = num

print "Maximum is", int(largest)
print "Minimum is", int(smallest)

[String Data Type]

- A string is a sequence of characters
- A string literal uses quotes 'Hello' or "Hello"
- For strings, + means 'concatenate' 
- When a string contains numbers it is still a string
- We can convert numbers in a string into a number using int()

Reading and Converting

- We prefer to read data in using strings and then parse and convert the data as we need
- This gives us more control over error situations and/or bad user input
- Raw input numbers must be converted from strings

Looking Inside Strings

- We can get at any single character in a string using an index specified in square brackets
- The index value must be an integer and starts at zero
- The index value can be an expression that is computed
- Element assignment however does NOT work (use loops)

A Character Too Far

- You will get a python error if you attempt to index beyond the end of a string
- So be careful when constructing index values and slices
- There is a built-in function len that gives us the lenght of a string

Looping Through Strings

- Using a while statement and an iteration variable, and the len function, we can construct a loop to look at each of the letters in a string individually.

fruit = 'banana'
index = 0 
while index < len(fruit):
	letter = fruit[index]
	print index, letter
	index = index + 1

- A definite loop using a for statement is much more elegant
- The iteration variable is completely taken care of by the for loop

fruit = 'banana'
for letter in fruit:
	print letter

Looping and Counting

- This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters the 'a' character.

word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count = count + 1
print count

Looking Deeper into in

- The iteration variable 'iterates' through the sequence (ordered set)
- The block (body) of code is executed once for each value in the sequence
- The iteration variable moves through all of the values in the sequence

Slicing Strings

- We can also look at any continuous section of a string using a colon operator
- The second number is one beyond the end of the slice - 'up to but not including'
- If the second number is beyond the end of the string, it stops at the end
- If we leave off the first or the last number of the slice, it is assumed to be the beginning or end of the string respectively

String Concatenation

- When the + operator is applied to strings, it means "concatenation" --> there is no space in between

Using in as an Operator

- The in keyword can also be used to check to see if one string is 'in' another string
- The in expression is a logical expression and returns True or False and can be used in an if statement

fruit = 'banana'
'n' in fruit 
#=> True

String Comparison

if word == 'banana':
	print 'All right, bananas.'

if word < 'banana':
	print 'Your word, ' + word + ', comes before banana (alphabetically).'
elif word > 'banana':
	print 'Your word, ' + word + ', comes after banana.'
else:
	print 'All right, bananas.'

String Library

- Python has a number of string functions which are in the string library
- These functions are already built into every string - we invoke them by appending the function to the string variable
- These functions do not modify the original string, instead they return a new string that has been altered

import string
greet = 'Hello Bob'
zap = greet.lower()
print zap
#=> hello bob

stuff = 'Hello world'
type(stuff)
#=> <type 'str'>
dir(stuff) --> what are all the things built into this that I can make use of?
- http://docs.python.org/lib/string-methods.html

Searching a String

- We use the find() function to search for a substring within another string
- find() finds the first occurance of the substring
- If the subsring is not found find() returns -1
- Remember that string positions starts at zero

fruit = 'banana'
pos = fruit.find('na')
print pos
#=> 2

aa = fruit.find('z')
print aa
#=> -1

Making everything UPPER CASE

- You can make a copy of a string in lower case or upper case
- Often when we are searching for a string using find() - we first convert the string the lower case so we can search a string regardless of case

Search and Replace

- The replace() function is like a "search and replace" operation in a word processor
- It replaces all occurrences of the search string with the replacement string

greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print nstr
#=> Hello Jane

greet = 'Hello Bob'
nstr = greet.replace('o','X')
print nstr
#=> HellX BXb

Stripping Whitespace

- Sometimes we want to take a string and remove whitespace at the beginning and/or end
- lstrip() and rstrip() to the left and right only
- strip() removes both begin and ending whitespace

greet = '   Hello Bob '
greet.lstrip()
#=> 'Hello Bob '
greet.rstrip()
#=> '   Hello Bob'
greet.strip()
#=> 'Hello Bob'

Prefixes

line = 'Please have a nice day'
line.startswith('Please')
#=> True
line.startswith('p')
#=> False

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print atpos
#=> 21
sppos = dat.find(' ',atpos)
print sppos
#=> 31
host = data[atpos+1:sppos]
print host
#=> uct.ac.za 

- This is called parsing text --> finding a substring/part

text = "X-DSPAM-Confidence:    0.8475"
pos1 = text.find('0')
sub = float(text[pos1:])
print sub

[Files]

- Escape to secondary memory, read/write files
- A text file can be thought of as a sequence of lines

1 - Opening a File

- Before we can read the contents of the file we must tell Python which file we are going to work with and what we will be doing with the file
- This is done with the open() function
- open() returns a "file handle" - a variable used to perform operations on the file
- Kind of like "File -> Open" in a word processor

Using open()

- handle = open(filename,mode) -- fhand = open('mbox.txt','r')
+ returns a handle used to manipulate the file (establishes a connection between the primary memory and secondary memory)
+ filename is a string
+ mode is optional (default = 'r') and should be 'r' if we are planning reading the file and 'w' if we are going to write to the file

What is a Handle?

- Handle maintains the connection between the file and your program

fhand = open('mbox.txt')
print fhand
#=> <open file 'mbox.txt', mode 'r' at 0x1005088b0>

When Files are Missing

fhand = open('stuff.txt')
#=> Traceback (most recent call last):
#=> File "<stdin>", line I, in <module>
#=> IOError:[Errno 2] No such file or directory: 'stuff.txt'

The newline Character

- We use a special character to indicate when a line ends called the 'newline'
- We represent it as '\n' in strings
- Newline is still one character - not two

stuff = 'Hello\nWorld!'
stuff
#=> 'Hello\nWorld!'
print stuff
#=> Hello
#=> World!

stuff = 'X\nY'
print stuff
#=> X
#=> Y
len(stuff) #=> 3

File Processing

- A text file can be thought of as a sequence of lines

File Handle as a sequence

- A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
- We can use the for statement to iterate through a sequence
- Remember - a sequence is an ordered set

xfile = open('mbox.txt') # xfile --> handle, a way to read the data
for cheese in xfile:
	print cheese

Counting Lines in a File

- Open a file read-only
- Use a for loop to read each line
- Count the lines and print out the number of lines

fhand = open('mbox.txt') # default is read
count = 0
for line in fhand:
	count = count + 1 # or count += 1

print 'Line Count:', count

Reading the *Whole* File

- We can read the whole file (newlines and all) into a single string

fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)
print inp[:20]
#=> From stephan.marquar --> first 20 chars (0-19)

Searching Through a File

- We can put an if statement in our for loop to only print lines that meet some criteria

fhand = open('mbox-short.txt')
for line in fhand:
	if line.startswith('From'): #=> .startwith = string utility function
		print line

- This will result in blanklines in between 'hits' (From:)
+ The print statement adds a newline to each line.
+ Each line from the file also has a newline at the end. 

- We can strip the whitespace from the right hand side of the string using rstrip() from the string library
- The newline is considered 'white space' and is stripped

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip() # strip, rstrip (right), lstrip (left)
	if line.startswith('From'): # .startwith = string utility function
		print line

Skipping with continue

- We can conveniently skip a line by using the continue statement (skipping pattern)

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	# Skip 'uninteresting lines'
	if not line.startswith('From:'):
		continue
	# Process our 'interesting' line
	print line

Using in to select lines

- We can look for a string anywhere in a line as our selection criteria

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not '@uct.ac.za' in line:
		continue
	print line

Prompt for File Name

fname = raw_input('Enter the file name: ')
fhand = open(fname) # could use a try/except in case of bad file names
count = 0 
for line in fhand:
	if line.startswith('Subject'):
		count = count + 1
print 'There were', count, 'subject lines in',fname

Bad File Names

fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened:',fname
	exit()
count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print 'There were',count,'subject lines in',fname

=== Assignment 7.1

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print 'File cannot be opened: ',fname
    exit()
for line in fhandle:
    line = line.rstrip()
    line = line.upper()
    print line

=== Assignment 7.2

# Use the file name mbox-short.txt as the file name
sum = 0
count = 0
fname = raw_input("Enter file name: ")
fhandle = open(fname)
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos1 = line.find('0')
    sub = float(line[pos1:])
    sum = sum + sub 
    count = count + 1    

average = sum/count
print "Average spam confidence:",average

[Lists]

A List is a kind of Collection

- A collection allows us to put many values in a single "variable"
- A collection is nice because we can carry all many values around in one convenient package

friend = ['Joseph','Glenn','Sally']

What is not a 'Collection'

- Most of our variables have one value in them - when we put a new value in the variable, the old value is over written

List Constants

- List constants are surrounded by square brackets and the elements in the list are separated by commas
- A list element can be any Python object, even another list
- A list can be empty

print [1,[5,6],7]
#=> [1,[5,6],7] --> length outer list = 3, length inner list = 2

Looking Inside Lists

- Just like strings, we can get at any single element in a list using an index specified in square brackets

friends = ['Joseph','Glenn','Sally']
print friends[1]
#=> Glenn

Lists are Mutable

- Strings are 'immutable' - we cannot change the contents of a string, we must make a new string to make any change
- Lists are 'mutable' - we can change an element of a list using the index operator

fruit = 'Banana'
fruit[0] = 'b'
#=> Traceback error

x = fruit.lower()
print x
#=> banana

lotto = [2,14,26,41,63]
lotto[2] = 28
print lotto
#=> [2,14,28,41,63]

How Long is a List

- The len() function takes a list as a parameter and returns the number of elements in the list
- Actually len() tells us the number of elements of any set or sequene (i.e. such as a string)

Using the range function

- The range function returns a list of numbers that range from zero to one less than the parameter
- We can construct an index loop using for and an integer iterator

print range(4)
#=> [0,1,2,3]
friends = ['Joseph','Glenn','Sally']
print len(friends)
#=> 3
print range(len(friends))
#=> [0,1,2]

for i in range(len(friends)):
	friend = friends[i]
	print 'Happy New Year:',friend

Concatenating lists using +

- We can create a new list by adding two existing lists together
- Lists can be sliced like strings --> remember: second number is up to but not including

List Methods

x = list()
type(x)
#=> <type 'list'>
dir(x)
#=> ['append','count','extend','index','insert','pop','remove','reverse','sort']

Building a List from Scratch

- We can create an empty list and then add elements using the append method
- The list stays in order and new elements are added at the end of the list

stuff = list()
stuff.append('book')
stuff.append(99)
print stuff
['book',99]

Is Something in a List?

- Python provides two operators that let you check if an item is in a list
- These are logical operators that return True or False
- They do not modify the list

some = [1,9,21,10,16]
9 in some
#=> True
15 in some
#=> False
20 not in some
#=> True

A List is an Ordered Sequence

- A list can hold many items and keeps those items in the order until we do something to change the order
- A list can be sorted (i.e. change its order)
- The sort method (unlike in strings) means "sort yourself"

friends = ['Joseph','Glenn','Sally']
friends.sort() #=> alphabetical order
print friends
['Glenn','Joseph','Sally']

Built in Functions and Lists

- There are a number of functions built into Python that take lists as parameters
- Remember the loops we built? These are much simpler

nums = [3,41,12,9,74,15]
print len(nums)
#=> 6
print max(nums)
#=> 74
print min(nums)
#=> 3
print sum(nums)
#=> 154
print sum(nums)/len(nums) # average
#=> 25

numlist = list()

while True:
	inp = raw_input('Enter a number:')
	if inp == 'done': break
	value = float(inp)
	numlist.append(value)

average = sum(numlist)/len(numlist)
print 'Average:',average

Best Friends: Strings and Lists

- Split breaks a string into parts, produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.

abc = 'With three words'
stuff = abc.split()
print stuff
#=> ['With','three','words']
print len(stuff)
#=> 3
print stuff[0]
#=> With
for w in stuff:
	print w
#=> With
#=> three
#=> words

- When you do not specify a delimiter, multiple spaces are treated like 'one' delimiter

line = 'A lot              of spaces'
etc = line.split()
print etc
#=> ['A','lot','of','spaces']

- You can specify what delimiter character to used in the splitting

line = 'first;second;third'
thing = line.split(;)
print thing
#=> ['first','second','third']

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2009

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From '): continue
	words = line.split()
	print words[2]

The Double Split Pattern

- Sometimes we split a line one way and then grab one of the pieces of the line and split that piece again

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2009

words = line.split()
email = words[1]
pieces = email.split('@')
host = pieces[1]
print host
#=> uct.ac.za

=== Assignment 8.4

fname = raw_input("Enter file name: ")
fhandle = open(fname)
lst = list()
for line in fhandle:
    line.rstrip()
    words = line.split()
    for i in words:
        if i not in lst:
            lst.append(i)
    
lst.sort()
print lst

=== Assignment 8.5

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
count = 0

for line in fhandle:
    line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print words[1]
        count += 1
 
print "There were", count, "lines in the file with From as the first word"

[Dictionaries]

What is a collection?

- A collection is nice because we can put more than one value in them and carry them all around in one convenient package.
- We have a bunch of values in a singe 'variable'
- We do this by having more than one place 'in' the variable
- We have ways of finding the different places in the variable

What is not a a 'Collection'

- Most of our variables have one value in them - when we put a new value in the variable - the old value is overwritten

A Story of Two Collections..

- List: A linear collection of values that stay in order
- Dictionary: A 'bag' of values, each with its own label

Dictionaries

- Dictionaries are Pythons most powerful data collection
- Dictionaries allow us to do fast database-like operations in Python
- Dictionaries have different names in different languages
+ Associative arrays - Perl / PHP
+ Properties or Map or HasMap - Java
+ Property Bag - C# / .Net

- Lists index their entires based on the position in the list
- Dictionaries are like bags: no order
- So we index the things we put in the dictionary with a 'lookup tag'

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse
#=> {'money':12,'tissues:75','candy':3}
print purse['Candy']
#=> 3
purse['candy'] = purse['candy'] + 2
print purse
#=> {'money':12,'tissues:75','candy':5}

Comparing Lists and Dictionaries

- Dictionaries are like Lists except that they use keys instead of numbers to look up values. 

lst = list() # maintain order, in lists keys are numbers
lst.append(21)
lst.append(183)
print lst
#=> [21,183]
lst[0] = 23
print lst
#=> [23,183]

ddd = dict() # order is not preserved in dictionaries, we use keys, makes it faster (hashing)
ddd['age'] = 21
ddd['course'] = 182
print ddd
#=> {'course':182,'age':21}
ddd['age'] = 23
print ddd
#=> ['course':182,'age':23]

Dictionary Literals (Constants)

- Dictionary literals use curly braces and have a list of key:value pairs
- You can make an empty dictionary using empty curly braces

jjj = {'chuck':1,'fred':42,'jan':100}
print jjj
#=> {'jan':100,'chuck':1,'fred':42} -- no order!
ooo = {}
print ooo
#=> {}

Many Counters with a Dictionary

- One common use of a dictionary is counting how often we "see" something 

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print ccc
#=> {'csev':1,'cwen':1}
ccc['cwen'] = ccc['cwen'] + 1
print ccc
#=> {'csev':1,'cwen':2}

Dictionary Tracebacks

- It is an error to reference a key which is not in the dictionary
- We can use the in operator to see if a key is in the dictionary 

ccc = dict()
print ccc['csev']
#=> Traceback KeyError: 'csev'
print 'csev' in  # is the string csev a current key in the dictionary ccc
#=> False

When we see a new name

- When we encounter a new name, we need to add a new entry in the dictionary and if this is the second or later time we have seen the name, we simply add one to the count in the dictionary under that name

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1
print counts
#=> {'csev':2,'zqian':1,'cwen':2}

The get method for dictionary

- This pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common, that there is a method called get() that does this for us

if name in counts:
	print counts[name]
else:
	print 0

print counts.get(name,0) -- get me the value if it exists, if not return 0 // name = key
#=> {'csev':2,'zqian':1,'cwen':2}

Simplified counting with get()

- We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	counts[name] = counts.get(name,0) + 1 # 0 = default value, either going to create key:value pair or update value
print counts
#=> {'csev':2,'zqian':1,'cwen':2}

Counting Pattern

- The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently

counts = dict()
print 'Enter a line of text:'
line = raw_input('')

words = line.split()
print 'Words:', words

print 'Counting..'
for word in words:
	counts[word] = counts.get(word,0) + 1

print 'Counts', counts

Definite Loops and Dictionaries

- Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values

counts = {'chuck':1,'fred':42,'jan':100}
for key in counts:
	print, key, counts[key]
#=> jan 100
#=> chuck 1
#=> fred 42

Retrieving lists of Keys and values

- You can get a list of keys, values or items (both) from a dictionary

jjj = {'chuck':1,'fred':42,'jan':100}
print list(jjj) # only returns the keys
#=> ['jan','chuck','fred']
print jjj.keys()
#=> ['jan','chuck','fred']
print jjj.values()
#=> [100,1,42] -- same order as one above
print jjj.items() # returns both, can use both as iteration variables in floops
#=> [('jan',100),('chuck',1),('fred',42)] -- tuples (immutable key/value pairs)

Bonus: Two Iteration Variables (using .items() -- because this one returns both the key and value [two])

- We loop through the key-value paris in a dictionary using *two* iteration variables
- Each iteration, the first variable is the key, and the second variable is the corresponding value for the key

jjj = {'chuck':1,'fred':42,'jan':100}
for aaa,bbb in jjj.items():
	print aaa,bbb
#=> jan 100
#=> chuck 1
#=> fred 42

===

name = raw_input("Enter file:")
handle = open(name,'r')
text = handle.read() # take everything as one string
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None

for word,count in counts.items():
	if bigcount is None or count > bigcount: # if bigcount is None takes care of the first entry
		bigword = word
		bigcount = count

print bigword,bigcount

===

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name,'r')

counts = dict()

for line in fhand:
	line = line.rstrip()
	if not line.startswith('From '): continue
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0) + 1

bigcount = 0
bigword = 0

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print bigword,bigcount

===

[Tuples]

Tuples are like lists (but non-changeable)

- Tuples are another kind of sequence that function much like a list - they have elements which are indexed starting at 0

x = ('Glenn', 'Sally', 'Joseph')
print x[2]
#=> Joseph
y = (1, 9, 2)
print y
#=> (1, 9, 2)
print max(y)
#=> 9
for inter in y:
	print iter 
#=> 1
#=> 9 
#=> 2

..but.. Tuples are "immutable"

- Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string

x = [9, 8, 7]
x[2] = 6
print x
#=> [9, 8, 6]

y = 'ABC'
y[2] = 'D'
#=> Traceback: 'str' object does not support item assignment

z = (5, 4, 3)
z[2] = 0
#=> Traceback: 'tuple' does not support item assignment

x = (3, 2, 1)
x.sort()
#=> Traceback: AttributeError: 'tuple' object has no attribute 'sort'
x.append(5)
#=> Traceback: AttributeError: 'tuple' object has no attribute 'append'
x.reverse()
#=> Traceback: AttributeError: 'tuple' object has no attribute 'reverse'

A Tale of Two Sequences

l = list()
dir(l)
['append','count','extend','index','insert','pop','remove','reverse','sort']

t = tuple()
dir(t)
['count','index']

Tuples are more efficient
- Since Python does not have to build tuple structures to be modifiable,
the are simpler and more efficient in terms of memory use and performance than lists
- So in our program when we are making "temporary variables" we prefer tuples over lists

Tuples and Assignment

- We can also put a tuple on the left hand side of an assignment statement
- We can even omit the parenthesis

(x, y) = (4, 'fred')
print y
#=> fred
(a, b) = (99, 98) # a, b = (99, 98) --> for key, value in dict.items(): -- is the same!

print a
#=> 99

Tuples and Dictionaries

- The items() method in dictionaries returns a list (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
	print k, v
#=> 2
#=> 4
tups = d.items()
print tups
#=> [('csev', 2),('cwen', 4)]

Tuples are Comparable

- The comparison operators work with tuples and other sequences.
If the first item is equal, Python goes on to the next element, and so on,
until it finds elements that differ.

(0, 1, 2) < (5, 1, 2)
#=> True
(0, 1, 200000) < (0, 3 , 4)
#=> True
('Jones', 'Sally') < ('Jones', 'Fred')
#=> False
('Jones', 'Sally') > ('Adams', 'Sam')
#=> True

Sorting Lists of Tuples

- Things that can be compared, can also be sorted
- We can take advantage of the ability to sort a list of tuples to get a sorted version of a library
First we sort the dectionary by the ky us the .items() method

d = {'a':10, 'b':1, 'c':22}
t = d.items()
t
#=> [('a', 10),('c', 22),('b', 1)]
t.sort()
t
#=> [('a', 10),('b', 1),('c', 22)]

--> Sort by keys

Using sorted()

- We can do this even more directly using the built-in function sorted
that takes a sequence as a parameter and returns a sorted sequence

d = {'a':10, 'b':1, 'c':22}
d.items()
#=> [('a', 10),('c', 22),('b', 1)]
t = sorted(d.items())
t
#=> [('a', 10),('b', 1),('c', 22)]

for k,v in sorted(d.items()):
	print k, v
#=> a 10
#=> b 1
#=> c 22

Sort by values instead of key

- If we could construct a list of tuples of the form (value, key) we could sort by value
- We do this with a for loop that creates a list of tuples

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
	tmp.append( (v, k) )
print tmp
#=> [(10, 'a'),(22, 'c'),(1, 'b')]
tmp.sort(reverse=True)
print tmp
#=> [(22, 'c'),(10, 'a'),(1, 'b')] 

===

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
	lst.append( (val, key) )

lst.sort(reverse=True)

for val, key in lst[:10]:
	print key, val

-- The top 10 most common words!

===

Even Shorter version

c = {'a':10, 'b':1, 'c':22}
print sorted( [ (v, k) for k,v in c.items() ] )
#=> [(1, 'b'),(10, 'a'),(22, 'c')]

- List comprehension creates a dynamic list. In this case, we make a list of reverserd tuples and then sort it

===

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
	if line.startswith('From '):
         lst = line.split()
         time = lst[5].split(':')
         hour = time[0]
         counts[hour] = counts.get(hour, 0) + 1

for k, v in sorted( [ (k, v) for k,v in counts.items() ] ):
    print k, v

===

[RegEx]

- In computing, a regular expression, also referred to as "regex" or "regexp", provides 
a concise and flexible means for matching strings of text, such as particular characters, words or patterns
of characters. A regular expression is written in a formal language that can be interpreted 
by a regular expression processor.

- Really clever "wild card" expressions for matching and parsing strings.

Understanding Regular Expressions

- Very powerful and cryptic
- Fun once you understand them
- Regular expressions are a language unto themselves
- A language of "marker characters" - programming with characters
- It is kind of an "old school" language - compact

'^' 	 	 - Matches the beginning of a line
'$' 	 	 - Matches the end of the line
'.' 	 	 - Matches any character
'\s' 	 	 - Matches whitespace (drop the '')
'\S' 	 	 - Matches any non-whitespace character (drop the '')
'*' 	 	 - Repeats a character zero or more times
'*?' 	 	 - Repeats a character zero or more times (non-greedy)
'+' 	 	 - Repeats a character one or more times 
'+?' 	 	 - Repeats a character one or more times (non-greedy)
'[aeiou]'  	 - Matches a single character in the listed set
'[^XYZ]'   	 - Matches a single character not in the listed set
'[a-z0-9]' 	 - The set of characters can include a range
'(' 		 - Indicates where string extraction is to start
')' 		 - Indicates where string extraction is to end

The Regular Expression Module

- Before you can use regular expressions in your program, you must import the
library using "import re"
- You can use re.search() to see if a string matches a regular expression similar
to using the find() method for strings
- You can use re.findall() to extract portions of a string that match your 
regular expression similar to a combination of find() and slicing: var[5:10]

Using re.search() like find()

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From:') >0:
		print line

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:',line):
		print line

--> We fine tune what is matched by adding special characters to the string: '^From:'

Wild-Card Characters

- The dot character matches any character
- If you add the asterisk character, the character is "any number of times"

'^X.*:'

X-Sieve: CMU Sieve 2.3
X-DSPAM-Result: Innocent
X-DSPAM-Confidence: 0.8475
X-Content-Type-Message-Body: text/plain

Fine-Tuning Your Match

- Depending on how 'clean' your data is and the purpose of your
application, you may want to narrow your match down a bit: '^X-\S+:' # \S (any non-whitespace) & + (one or more times, not zero or more)

X Plane is behind schedule: two weeks --> will no longer match!

Matching and Extracting Data

- The re.search() returns a True/False depending on whether the string matches
the regular expression
- If we actually want the matching string to be extracted, we use re.findall()

'[0-9]+' # one or more digits

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print y
#=> ['2','19','42'] # returns a list of strings
z = re.findall('[AEIOU]+', x) # AA OU would have matched (not Aa Ou)
print z
#=> []

- When we use re.findall() it returns a list of zero or more sub-strings
that match the regular expression

Warning: Greedy Matching

- The repeat characters (* and +) push outward in both directions (greedy)
to match the largest possible string

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y
#=> ['From: Using the :']

--> Why not 'From:'? Trying to get the largest string possible. 
If you do not want this, append it with the '?'! '^F.+?:'

"stop at the first"

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print y
#=> ['From:']

Fine Tuning String Extraction

- You can refine the match for re.findall() and separately determine which 
portion of the match that is to be extracted using paranthesis

"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

y = re.findall('\S+@+\S',x) # \S = At least one non-whitespace character
print y
#=> ['stephen.marquard@uct.ac.za']

Greedy version:

y = re.findall('\S+?@+?\S',x) # \S = At least one non-whitespace character
print y
#=> ['d@u']

- Parenthesis are not part of the match - but 
they tell where to start and stop what string to extract:

"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

y = re.findall('^From (\S+@+\S)',x) # \S = At least one non-whitespace character
print y
#=> ['stephen.marquard@uct.ac.za']
-- much stricter search for e-mail adres

Finding Host Name

First Version: Using find and string slicing

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find('@')
print atpos
#=> 21
sppos = data.find('',atpos)
print sppos
#=> 31
host = data[atpos+1:sppos]
print host
#=> uct.ac.za

Second Version: The Double Split 

- Sometimes we split a line one way and then grab one of the pieces of the line
and split that piece again

words = line.split()		#=> ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
email = words[1] 			#=> 'stephen.marquard@uct.ac.za'
pieces = email.split('@')   #=> ['stephen.marquard', 'uct.ac.za']
print pieces[1] 			#=> 'uct.ac.za'

Third Version: The RegEx Version

import re
lin = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('@([^ ]*)', lin)
print y 
#=> ['uct.ac.za']

- starts with @ but not included (outside paranthesis) # () "start/stop extracting"
- [^ ] everything except whitespace
- * 0 or more --> could also use + (at least one non-blank)

Better version: '^From .*@([^ ]+)'

===

Spam Confidence

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) # character != digit
	if len(stuff) != 1 : continue # for when we do not have match --> stuff will be an empty list, hence we need to continue (or we'd append a bunch of empty lists)
	num = float(stuff[0])
	numlist.append(num)

print 'Maximum:', max(numlist)

Escape Character

- If you want a special regular expression character to just behave 
normally (most of the time) your prefix it with '\''

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print y
#=> ['$10.00'] -- thee . in the regex pulled out the '.' in 10.00!

Summary

- Regular expressions are a cryptic but powerful language for 
matching strings and extracting elements from those strings
- Regular expressions have special characters that indicate intent
- Better when working with noisy data
