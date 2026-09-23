#TUPLES
gender=("male", "female","others")
print(gender)   # ('male', 'female', 'others')
print(gender.count("male"))
print(gender.index("male"))
print(type(gender))
print(len(gender))
print(gender[1])

#OUTPUT
'''
('male', 'female', 'others')
1
0
<class 'tuple'>
3
female
'''


#insertion to tuples
a=('1','2','3','4','5')
b=('6')
l=list(a)
l.append(b)
print(tuple(l))

#OUTPUT 
#('1', '2', '3', '4', '5', '6')


#CONCATENATION Of tuples

t1=(1,2,3,4)
t2=(5,6,7,8)
t=t1+t2
print(t)   #(1, 2, 3, 4, 5, 6, 7, 8)


#REPETATION OF TUPLES
t3=(1,2)*5
print(t3)   # (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)

#checking membership

fruits=("apple","banana","kiwi")
print("apple" in fruits)         #true




#SETS
s={20,3, 134}  # set is unordered
print(type(s))  #<class 'set'>
print(s)  #{3, 20, 134}
# print(s[0])   #un indexed

p=set()
print(p)

s1={1,2,3}
s2={3,4,5}
s3=s1|s2  #union
s4=s1&s2  #intersection
s5=s1-s2   #difference
print( s3, s4, s5)

# {1, 2, 3, 4, 5} {3} {1, 2}


s1.add(4)
print(s1)
s2.remove(5)  #{1, 2, 3, 4}
print(s2)     #{3, 4}
t=s2.pop()
print(t)


#Home work
#1)

z=(1,2,3,4,5)
 # cannot add the elements
z1=6
l=list(z)
l.append(z1)
tuple(l)
print(l)
print(z[1:3])
y=(6,7,8,9)
w=z+y
print(w)

#[1, 2, 3, 4, 5, 6] 
# #(2, 3)
#(1, 2, 3, 4, 5, 6, 7, 8, 9)

#2)
mf={"orange","kiwi","banana"}
ff={"apple","stra","pineapple","banana"}
d=mf|ff
e=mf&ff
f=mf-ff
print(d)
print(e)
print(f)

(mf.add("straw"))
print(mf)
mf.remove("kiwi")
print(mf)
mf.discard("pineapple")
print(mf)

#OUTPUTS
'''{'stra', 'banana', 'kiwi', 'apple', 'orange', 'pineapple'}
{'banana'}
{'orange', 'kiwi'}
{'orange', 'banana', 'kiwi', 'straw'}
{'orange', 'banana', 'straw'}
{'orange', 'banana', 'straw'}
'''

#3)
r=[1,2,3,4,5]
q=tuple(r)
s=set(r)
print(q)
print(s)
#q.append(20)  not possible in tuple to change the values
s.add(40)

print(s)

# OUTPUT
'''(1, 2, 3, 4, 5)
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 40}
'''












