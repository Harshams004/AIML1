a=[1,1,1,1]
b=[1,2,3,4]
c=[1,1,1,1]
d=list(map(lambda x,y,z:x+y+z,a,b,c))
print(d)

fruitss=["Mango","Apple","Orange","Kiwi"]
e=list(filter(lambda x :'g' in x ,fruitss))
print(e)
