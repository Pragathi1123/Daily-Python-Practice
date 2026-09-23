items=["sugar", "bru","bru2"]
print(items)
l=[1,2,3,"sugar"]
print(l)
items.pop()
items.pop(1)
items.append("mom's magic")
print(items)
l[0]="5"
print(l)
items.insert(1,"tea")
print(items)
l.remove(2)
print(l)
print(items[0:1:2])
print(len(items))
a=[0,10,14]
print(sorted(a))
b=[1,2,3,4,5,6,7,8,9,10]
print(sum(b))
nump=[1,23,22,43,67]
sorted_nump= sorted(nump)
rev=sorted_nump.reverse()
print(sorted_nump)

#MATRIX
m=[[1 ,2 ],[3,4]]
print(m)
print(m[0][0]) #nesting
print(m[1][0])
print(type(m))

#OUTPUT
'''['sugar', 'bru', 'bru2']
[1, 2, 3, 'sugar']
['sugar', "mom's magic"]
['5', 2, 3, 'sugar']
['sugar', 'tea', "mom's magic"]
['5', 3, 'sugar']
['sugar']
3
[0, 10, 14]
55
[67, 43, 23, 22, 1]
[[1, 2], [3, 4]]
1
3
<class 'list'>
'''




