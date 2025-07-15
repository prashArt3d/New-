#----------------Concatenation -------------------
first_name = "joe"
second_name= "doe"

full_name = first_name + second_name 
print(full_name)

result = "hello"*3
print(result)

character ="*"
pattern = (character + "")*4
print (pattern)

word = "Go"
time = 8 
cheer =(word+"")*time
print(cheer)

#-------------Comma (, )-----------

word1="new"
word2= "Thing"
print(word1,word2)

print("apple", "bannanas", "cherrys")



#------------------------String Operations---------------------------------------------#
#omparison Operators
#ASCII TABLE
#Membership Operators

result = "apple" < "bannana"
print(result)

result = "cherry" > "grape"
print (result)

result = "kiwi"!= "apple"
print(result)

#------------------------Membership Operators---------------

text ="hello friends"
result = "friends" in text
print(result)

text ="my mistake "
result = "my" not in text
print(result)

#---------------------------String Escape Characters-----------------------------------------------------------#

print("i am new in \"india\".")


text= "hello \nworld"
print(text)

text = 'it\'s sunny day '
print(text)

text = "it's sunny day "
print(text)

text = """actor says : never say,\n\n never !"""
print(text) 

file_path =  "C:\\Users\\prash\\Downloads"
print(file_path)


#---------------------------------------String Formatting-------------------------------------------------------------#

name = "Alice"
fomatted_string ="Hello,%s!"%name
print(fomatted_string)

age= 30
formated_string ="i am %d years old "%age
print(formated_string)


temp = 25.5
formated_string = "the temperature is % .2f"%temp
print(formated_string)


#------------------------------Multiple Values in One String________-----------------------------------#

name = "joe"
age = 25
height = 175.5
formatted_string = "Name: %s, Age: %d, Height: %.1f cm" % (name, age, height)
print (formatted_string)

charcter_code= 85
formated_string= "the character is %c"%charcter_code
print(formated_string)

name = "prash"
age = 35
message = "My name is {} and I'm {} years old.".format(name, age)
print (message)



text = "{0} is {1} years old.".format("prash", 35)
print(text)


text = "The price of {0} is {1:.2f}.".format("a book", 12.49, 12.49 )
print(text)

first_name = "joe"
second_name= "doe"

full_name = first_name + second_name 
print(full_name)

