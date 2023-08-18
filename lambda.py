a=lambda x:x+5
print(a(5))

b=lambda a,b:a+b
print(b(2,3))

c=lambda a,b: a if(a>b) else b
print(c(3,1,))

d=lambda a:a*a
print(d(5))

#map
lst=[1,2,3,4,5,6]
e=list(map(lambda x:x+5,lst))
print(e)

#filter
lst=[1,2,3,4,5,6,7,8,9]
f=list(filter(lambda x:x%2,lst))
print(f)

#reduce
lst=[1,2,3,4,5,6,7,8]
from functools import reduce
y=reduce(lambda x,y: x+y,lst) 
print(y)
