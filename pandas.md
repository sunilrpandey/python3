# Pandas

## Basic commands
```
pandas dataframe 
index
columns
values
df[1:3]
head(i)
tail(2)
isnull()
iloc() // column header similar to slice
loc() //row header
drop()
fillna() fill nan value with mean, 0 or any other values
copy
to_csv("filename.csv") //same for excel
df = pd.read_csv("filename")
```
### plot a series
```py
import numpy as np
%mathplotlib inline
ts = pd.Series(np.random.randn(50)) # can add index = something
ts = ts.cumsum()
ts.plot()
```

### Plot a dataframe
```py
import numpy as np
%mathplotlib inline
ts = pd.DataFrame(np.random.randn(50,4)) # can add index = something, column = [a,b,c,d]
ts = ts.cumsum()
ts.plot()
```