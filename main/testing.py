import pandas as pd
from board_transform import Move

x = [1, 2, 3, 4]
y = ['a', 'b', 'c', 'd']

zipped = zip(x, y)
print(list(zipped))
print(dict(zipped))


#y = {"c": [4, 2], "d": [8, 5]}

df = pd.DataFrame(index=y, columns=Move)
print(df)

#df_new = df.append(pd.DataFrame(y))

#print(df_new)