# Suggestion (especially helpful while solving the homework assignments): Python Cheat Sheet
# https://www.dataquest.io/blog/python-cheat-sheet/

# === Working with variables ===

# In general, Python scripts are just executed from top to bottom, an explicit main function is not
# necessary (it is possible and useful to have one, but we will take a loot at that later).

# Variables do not have type declarations:
x = 5
x += 3
y = 2*x
print(y)

# The usual operations work just as expected.
# Modulo:
print(y%3)

# Floor:
print(y//3)

# Exponents:
print(y**4)

# All operations can be combined with assignment:
y %= 3
print(y)

# Careful: Python uses strong typing -> Java-type concatenation does not work!
print("y="+y)

# Instead, types must be converted manually:
print("y="+str(y))

# Every variable in Python is an object:
print(x.bit_length())

# dir() is an extremely useful function: It shows all methods available for an object:
dir(x)

# That is, for instance, useful to find out how to do something with an object
# that one suspects should be possible (as a shortcut before digging into documentation,
# or if documentation is lacking).
# For instance, try to find out how to convert a string object into uppercase:
dir("   test")

# This shows, among other things, a method called "upper()". Let's see what it does:
print("   test".upper())

# Caution: Methods starting with "__" are "magic methods", they are meant for internal use and
# are not supposed to be called manually (Python does not have access modifiers, so this is its
# way of saying "please don't, if we had access modifiers this would be private").

# For data management, there's lists:
x = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
print(x)

# Careful: Due to dynamic typisation x=[1,2,3] is possible: x used to be an integer, now it is a list.
# Addressing elements of a list works as expected:
print(x[0])

# In Python, you can do lots of fun and useful things with lists:
# slicing
print(x[2:5])
print(x[5:])
print(x[:5])

# addressing relative to the list's end
print(x[-3])

# chaining and mixing data types (including putting lists into lists)
print(x + ["a", 2, ["b", "blub"]])

# repeating
zerolist = 4*[0]
print(zerolist)

# removing elements
print(x)
x.pop(3) # 3 is the index
print(x)
x.remove(5) # 5 is the element's value, the first occurence is removed
print(x)

# The operator "in" allows to check whether an element occurs in a list:
mylist = [0, 5, 7]
if 7 in mylist:
    print("7 is in the list!")
else:
    print("7 is not in the list!")

# Performance hint: Under the hood, lists are pre-allocated pointer arrays. Once the capacity is reached,
# a larger array is allocated and the old array's values are copied.
# pop last, get are O(1), append is amortised O(1), but pop by index and remove are O(n)!

# --- Task 1: Lists (see aufgaben.py) ---


# Tuples are a slimmer version of lists:
tup = (1, 3, 4)
print(tup)

# Tuples are immutable, so you can't do much more than initialize them and access the values. This allows
# lots of optimizations, so for performance reasons one should use tuples wherever possible (and future-proof)

# Then, there's dictionaries (like HashMaps in Java):
mydict = {"key": "value", "a": 5, "stuff": "great", 7: "seven"}
print(mydict)
print(mydict["stuff"])
mydict["stuff"] = "eh, not so great"
print(mydict["stuff"])

# As with lists, in allows to check whether a key exists in a dictionary:
print("stuff" in mydict)
print("newkey" in mydict)
mydict["newkey"] = "newvalue"
print("newkey" in mydict)
print(mydict["newkey"])

# A dictionary can also be initialized directly from a tuple of tuples:
mydict2 = dict((("7", "seven"), ("eight", 8)))
print(mydict2)

# --- Task 2: Dictionaries (see aufgaben.py) ---

# A set is a, well, set and can only contain each value once:

myset = set()
myset.add(15)
myset.add("blub")
print(myset)
myset.add(14)
myset.add(15)
print(myset)

# === Strings ===
# Python has some very useful string manipulation methods, so it is often used to perform simple (or not-so-simple)
# string/text file manipulation tasks (which, as we'll see, is very useful in bioinformatics)

# Possible string delimiters are ", ', or (for multiline strings) """:
print('That is useful to avoid having to escape " characters')

dat="""Or in order
to directly
initialize a string with
multiple lines"""
print(dat)

# There are lots of convenience methods for strings, for instance:

dat2 = dat.replace("\n", " ")
print(dat2)
print(dat2.split(" "))

# There is also regular expression support via the re module, but we're not going to look at that in detail here.

# Strings have a very useful method to concatenate tuples and lists:

toprint = ["Those", "are", "words"]
print(" ".join(toprint))
print("--!--".join(toprint))

# --- Task 3: Strings ---

# There is a specification language for formatting strings.
# {} are used as placeholders for variables:
x = 12
y = 4
print("the value of y: {} minus the value of x: {} is: {}".format(y, x, y-x))

# The positions of the values in the argument list of format() that are to be used can be
# specified within {}:
print("y: {1}, x: {0}".format(x, y))

# The nice thing about that: Positions can be repeated:
print("{0}{1}{0}".format("abra", "cad"))

# Number formats can be defined:
print("723 in binary: {0:b} and hex: {0:X}".format(723))

# Side note: That can be used to show the results of binary operations:
print("1: {:b}, 1<<2: {:b}, 60: {:b}, ~60: {:b} (dezimal: {}), 13: {:b}, 60&13: {:b}, 60|13: {:b} etc...".format(1, 1<<2, 60, ~60, ~60, 13, 60&13, 60|13))
# Question: Can anyone explain why ~60==-61?

# Alignment and padding characters can be specified:
print("y with 10 places and right aligned: {0:>10}, left aligned: {0:<10}, centered: {0:^10} and right aligned, padded with 0: {0:0>10}".format(y))


# === Flow control ===

# flow control structures work as expected.
# New:
#  * the beginning of a block is shown by a : after the control structure
#  * indentation is syntactically relevant (shows the length of a block) and must be consistent throughout the code (sometimes 3, sometimes 4 spaces does not work)
y = 12
if y > 10:
    y -= 3
elif y <= 10:
    y += 10
else:
    print("This is impossible!")
print(y)

# This would not work due to missing indentation:
#if y > 10:
#print("y immer noch groesser 10")

# While just does what while usually does:
y=10
while y > 5:
    print(y)
    y -= 1

# for, however, is used specifically for iteration (as the ":" version of for in Java):
letters = ["a", "b", "c"]
for letter in letters:
    if letter == "a":
        print("AAAAAAAAA")
    print(letter)

# One can iterate over everything that is an iterable (strings among other things):
print(range(2,7))
for x in range(2,7):
    print(x)

for x in range(0,10,3):
    print(x)

for key in mydict:
    print(str(key) + ": " + str(mydict[key]))

for item in mydict.items():
    print(item)

# --- Task 4: combining it all ---
