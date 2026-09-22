#ASSIGNMENT OPERATOR
x=10
x+=10  #x=x+10 (short form)
print(x)  #20 (output)

x*=10
print(x)  # 200(output)


#COMPARISION OPERATOR
a=10
b=12
print(a==b)
print(a<=b)
print( a!=b)
print(a>=b)

'''output
20
200
False
True
True
False
'''

#LOGICAL OPERATOR
print(1>2 and 2>1)
print(0 and 1)
print(0 or 1)
print(not(1))

#OUTPUT
'''False
0
1
False
'''

#MEMBERSHIP OPERATOR
numbers=[1,2,3,4,5]
string="Pragathi"
print("p" in string)
print("z" not in string)
print(3 in numbers)
print(7 not in numbers)
print("a" not in string)
print("p" not in string) or (3 in numbers)
print("p" in string) and (3 in numbers)

# outputs
'''False
True
True
True
False
True
False
'''

#BITWISE OPRATORS
p=5
q=3
print(p&q) #BITWISE AND
print(p|q) #BITWISE OR
print(~p)  #NEGATION
print(~q)  #NEGATION
print(p^q)   #BITWISE XOR
print(p<<1) #LEFT SHIFT
print(q>>1)  #RIGHT SHIFT

#OUTPUTS
'''
1
7
-6
-4
6
10
1
'''

#HOMEWORK
#1)
s = input("Enter the number 1: ")
r = input("Enter the num2: ")
print((int(s) > 10) and (int(r) > 10))
print((int(s) < 5) or (int(r) < 5))
print(not (int(s) < int(r)))

#OUTPUT
'''Enter the number 1: 10 
Enter the num2: 3
False
True
True
'''
#2)







