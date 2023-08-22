import pandas as pd

data={'days':[1,2,3,4,5,6,7,8,9,10],
      'Steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
df=pd.DataFrame(data)
df['Steps']=df['Steps'] +1000

print(df)

w=df[df['Steps'] > 7000]['days']
print("days walks more than 7000 steps")

h=pd.Series(w)
print(h)



