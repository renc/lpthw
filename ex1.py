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

