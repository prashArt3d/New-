
##--------------Understanding - If Statement----------------
number =10
if number >0:
    print("The number id positive")

    
new_number = 100

if new_number == 100:
 print("number is 100")

greeting = "hello"
if greeting == "hello":
   print ("greeting is hello ")

tempreture = 10
if tempreture > 0 :
   print ("tempreture is above freezing." )

###-----------if-else Statement-----------

number= -5
if number > 0:
   print("number is positive")
else:
  print ("number is negative")

x = 5
if x > 0:
    print("Positive")
    print("x is greater than zero")
    ##---------------------Checking if a Number is Even or Odd---------------------

number = 8
if number %2 ==0:
   print("the number is even")
else:
   print("number is odd")

text = "i love python"
if "python" in text:
   print ("the text contain pythone")
else:
   print("python not in text")

person = 18
if person >=18:
   print("he can vote")
else:
   print("not eligible for vote")

 #  ----------if-elif-else_-------------------------

temperature = 22

if temperature<0:
   print("its freezzing")
elif temperature<10:
   print("cold")
elif temperature<20:
   print("normal") 
elif temperature<30:
   print("warm")
else:
   print("hot")

age =16

if age <10:
   print("child ticket id :10$")
elif age < 15:
   print("Teen ticket : 20$")
elif age < 20:
   print("Young adult ticket : 30 $")
else:
   print("senior Ticket : 40 $")
   
   age = 16



number=55
if number < 0:
  print("small")
elif number < 10 :
   print("mediam")
elif number < 50:
   print("mediam-large")
else:
   print("number is greter than 50 ")


#--------------Nested if Statements-------------------------#


age = 16

if age < 10:
    print("Child ticket")
elif age < 18:
   print("Teen ticket")
elif age < 60:
    print("Adult ticket")
else:
    print("Senior ticket")