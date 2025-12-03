# Pandas 

# import pandas 

# df = pandas.read


import pandas as pd
#df = pd.read_csv("test.csv")
#df.head() first 5 rows of dataframe

#df.tail()

#df.info()

songs = {
    "Album": ["Album 1", "Album 2", "Album 3"],
    "Songs": ["Song 1", "Song 2", "Song 3"],
    "Duration": [3.5, 4.2, 3.1]
}

df = pd.DataFrame(songs)

print(df)

print(df.iloc[0, 0])
