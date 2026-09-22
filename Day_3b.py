first_name="PRAGATHI"
last_name="GOWDA"
print(first_name + " " + last_name)  # concatination(joining strings using +operator)
print("Pragathi " *3)  # Repatation (getting the same output many types like to reduce code)


#STRING METHODS
print(first_name.upper())  #UPPERCASE(CAPITAL LETTERS)
print(first_name.lower())  #SMALLCSE(SMALL LETTERS)
print(first_name.strip())  #REMOVE SPACE IN THE STRING
print(first_name.replace("PRAGATHI" , "CHANDHAN"))   #REPLACING EXISTING STRING NAME WITH NEW NAME
print(len(first_name))   #FINDING THE LENGHT OF STRING
print("hello "   'I am pragthi')  # STRING INSIDE THE STRING (2 STRINGS)
print("hello " 'I am Pragathi ' "Gowda " )   # STRING INSIDE THE STRING (3 STRINGS)
print("chan\tdhan \nsaid" "hello")

#INDEX
name = "CHANDHAN"
print(name[0])
print(name[3:6])
print(name[ :7])
print(name[0: ])
print(name[::3])


#DAY 3 HOME WORK
#1) 
name=input("Enter your name: ")

age=input("Enter the age: ")

print("Hello, " +name+ "! You are " + age + " years old")
print(f"Hello, {name} ! You are {age} yeasrs old.")

#2)
msg=input("Enter the msg:")
print(str(msg).upper())
print(msg.lower())
print(msg.replace(" ","_"))


#3)
user=input("Enter the word:")

length=len(user.replace( " ",""))
print(length)

#4)
print("Hello \n    world\n This is a backlash: \ ")

###PRACTICE OUTPUTS
#PRAGATHI GOWDA
#Pragathi Pragathi Pragathi 
#PRAGATHI
#pragathi
#PRAGATHI
#CHANDHAN
#8
#hello I am pragthi
#hello I am Pragathi Gowda 
#chan    dhan 
#saidhello
#C
#NDH
#CHANDHA
#CHANDHAN
#CNA

## HOME WORK OUTPUTS
#1)Enter your name: Chandhan
#Enter the age: 25
#Hello, Chandhan! You are 25 years old
#Hello, Chandhan ! You are 25 yeasrs old.
#2)Enter the msg:I am studying in bgscet
#I AM STUDYING IN BGSCET
#i am studying in bgscet
#I_am_studying_in_bgscet
#3)Enter the word:I am studying in bgscet
#19
#3)Hello 
#    world
# This is a backlash: \ 

