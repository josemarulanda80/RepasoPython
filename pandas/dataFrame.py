import pandas as pd
import numpy as np

myList=np.array([[0,1],[2,3],[4,5]])
myDataFrama = pd.DataFrame(myList,columns=["even","odd"])
print(myDataFrama)

