#file name quiz_app.py 
name = input("What is your name? ")
print ("Hello! ", name )

age = input("How old are you? ")
print ("Great to know that you are" , age , "years old!!")

total_point = 0
question = input("2 + 2? ")

if question == "4": 
    total_point = total_point + 1   
    print('Correct')
else: 
    print('Incorrect')

question = input("4 + 2? ")

if question == "6": 
    total_point = total_point + 1   
    print('Correct')
else: 
    print('Incorrect')

question = input("5 + 5? ")

if question == "10": 
    total_point = total_point + 1   
    print('Correct')
else: 
    print('Incorrect')

question = input("6 + 2? ")

if question == "8": 
    total_point = total_point + 1   
    print('Correct')
else: 
    print('Incorrect')

question = input("3 + 2? ")

if question == "5": 
    total_point = total_point + 1   
    print('Correct')
else: 
    print('Incorrect')

question = input("What is my favorite color? ")

#This is the way to fix all the upper and lowercase problem 
if question.lower() == "blue": 

    total_point = total_point + 1   
    print('Correct')
else: 
    print('Incorrect')

print (total_point)
#floating number
point1 = (total_point/6*100)

#full number
point = (int(total_point/6*100))

print (f"You total point is {point}%") 

