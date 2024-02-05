my_str = "this is my string"

#check the legnth of the string above
print (len(my_str))

#check the word is in my string
print ("is" in my_str) 

# Last letter in my string
print (my_str[-1])

# Multiple string line 
my_multiple_str = '''
dgagasdgasdgdsagds
asdgsdagasdg
'''

print (my_multiple_str)

my_str_1 = " Hello World! "

print (my_str_1)

# This is to delete the space 
print (my_str_1.strip())

# The first word in the quotation mark is the orinal and the next one is the new word to replace
print (my_str_1.replace("Hello","____"))

#Split the word by letter
print (my_str_1.split("l"))

# This is how to combine string word tgt
str_one = "Hiii"
str_two = "WORLDDDD"

print (str_one + str_two)

print (str_one + " " + str_two)

print ("hellloooo " + str_one + str_two)

#f stand for format
print (f"Hello, {str_one} {str_two}")

# my name is my name I'm here using ""
print ("My name is my name I'm here") 
# Using ''
print ('my name is my name I\'m here')