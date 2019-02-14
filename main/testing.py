import pandas as pd

x = [1, 2, 3, 4]
y = ['a', 'b', 'c', 'd']

zipped = zip(x, y)
print(list(zipped))
print(dict(zipped))


#y = {"c": [4, 2], "d": [8, 5]}

df = pd.DataFrame.from_dict(dict(zipped))
print(df.head(2))

#df_new = df.append(pd.DataFrame(y))

#print(df_new)