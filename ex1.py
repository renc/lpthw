#-*- coding: utf-8 -*- 

# Exercise 1. 
# learn saving a .py file, and use cmd python ex1.py to run this file.
# learn the string '' and ""

print "Hello World!"
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "can # be print out?"
print "what about \' and \" ?"
print "what about ' and "

# Exercise 3. Numbers and Math 
print "what is 7/4?", 7/4
print "what is 7.0/4?", 7.0/4

# Exercise 4. Variables and Name 
cars = 100
print "There are", cars, "cars available." 

# using %s wiht a list of variables to create string 
my_name = 'CJ.REN'
my_age = 32 # not a lie 
print "my name is %s, and age %d." % (my_name, my_age) 

# Exercise 6. String 
x = "There are %d types of people." % 10   #using %d and % to add string 
binary = "binary" 
do_not = "don't" 
y = "Those who know %s and those who %s" % (binary, do_not) #using %s and % to add string 

print x 
print y 

print "I said: %r." % x 
print "I also said:'%s'." % y 

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side." 

print w + e # using + to add string 

# This %r is best for debugging, since it display the "raw" data of the variable, 
# but we use other formats (%d, %s) for displaying to users. 

# Exercise 7. More printing  

print "Mary ahd a little lamb."
print "Its fleese was white as %s." % 'snow' 
print "And everywhere that Mary went."
print "." * 10

e1="C"
e2="h"
e3="e"
e4=e3
e5="s"
e6="e"
e7="B"
e8="u"
e9="r"
e10="g"
e11="e"
e12="r"

# watch that comma at the end, try removing it to see what happens
print e1 + e2 + e3 + e4 + e5 + e6, 
print e7 + e8 + e9 + e10 + e11 + e12 
# we have see above that , is used in print to connect two strings.

# Exercise 8, more printing 
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) 
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) 
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.", 
	"That you could type up right.", 
	"But id didn't sing.",
	"So I said goodnight."
) 
print "中文"
# we need to put coding: utf-8 at the top of file, or it complain the non-ascii

# multi lines string 
print "a\nb"
print """ 
line1
line2
""" 

# Exercise 10
# we saw that ' and " is used for sttring. if we want to print ' or ", 
# we need to use \' and \", these are Escape Sequences, 
# other Escape Sequences include \n \t \\ etc.

# Exercise 11. Asking question. 
print "How much do you weight?", 
weight = raw_input()  
# pay attention to the , 
 
print "So, you are %r heavy." % weight

height = raw_input("How tall are you?")
print "So, you are %r tall." % height 

# to learn raw_input() function, you can use:
# python -m pydoc raw_input 
# it will print some help information. 

