import numpy as np
%mathplotlib inline
ts = pd.DataFrame(np.random.randn(50,4)) # can add index = something, column = [a,b,c,d]
ts = ts.cumsum()
ts.plot()
