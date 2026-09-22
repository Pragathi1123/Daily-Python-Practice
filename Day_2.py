# VARIABLES
a=10
b=20
c=a*b
print(c)

x=y=z=10
print(x)
p, q, r= 100, 200, 300
print(r)

#DATA TYPES
age=10  #int
name = "Pragathi"  #string
rupee=1.45  #float
is_student = False  #bool
 
print(type(age))
print(type(is_student))  # changing datatype
is_student="true"
print(type(is_student))
age_float=float(age)
print(type(age_float))
print(age_float)


##TYPE CONVERSION
women="10"
men=20
print(int(women)+men)  #converting string to integer


##ARITHEMATIC OPERATIONS
s=10
t=3
print(s+t) #addition
print(s-t)  #subtraction
print(s*t)  #multiplication
print(s/t)  #division
print(s//t)  #floor division
print(s**t)   #exponent
print(s%t)    #modulus|remainder



####PRACTICE
#1)PERFORMING ARTITHEMATIC OPERATIONS
e=20
f=30
print(e+f)
print(e-f)
print(e*f)
print(e/f)
print(e//f)
print(e%f)
print(e**f)
print(e+f/e%f-e**f)

#2)SWAP TWO VARIABLES WITH AND WITHOUT USING THIRD VARIABLE
g=10
h=20
i=g
g=h
h=i
print(h,g)  # using third variable

j=40
k=50
j, k = k, j
print(j,k)     #without using third variable

##DAY2 OUTPUT
#200
#10
#300
#<class 'int'>
#<class 'bool'>
#<class 'str'>
#<class 'float'>
#10.0
#30
#13
#7
#30
#3.3333333333333335
#3
#1000
#1
#50
#-10
#600
#0.6666666666666666
#0
#20
#1073741824000000000000000000000000000000
#-1.073741824e+39
#10 20
#50 40