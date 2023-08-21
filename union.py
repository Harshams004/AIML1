import pandas as pd
import numpy as np
Series1=pd.Series([10,11,1,3])
Series2=pd.Series([1,2,1,5,8])
u=pd.Series(np.union1d(Series1,Series2))
i=pd.Series(np.intersect1d(Series1,Series2))
notcommon=u[~u.isin(i)]
print(u)
print(i)
print(notcommon)

