import pandas as pd
import numpy as np

import matplotlib.pyplot as p
data=pd.read_csv("C:/Users/SPTINT-16/Desktop/dataset/tips.csv")
print(data)

#scatter plot
p.scatter(data['day'],data['tip'])
p.xlabel('day')
p.ylabel('tip')
p.title ("scatter plot")
p.show()

#line plot
p.plot(data['tip'])
p.title('line plot')
p.xlabel('day')
p.show()

#bar plot
p.bar(data['day'],data['tip'])
p.xlabel('day')
p.ylabel('tip')
p.show()

#histogram
p.hist(data['total_bill'])
p.title('histogram plot')
p.show()

