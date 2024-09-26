import pandas as py

filename = "./big-mac-full-index.csv"
bm = py.read_csv(filename)

print(bm.columns)

print(bm.index)

for i in bm.index:

    #print(bm["name"][i])

    for index, row in bm.iterrows():
        print(bm['name'][index])