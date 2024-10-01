import pandas as py

filename = "./big-mac-full-index.csv"
bm = py.read_csv(filename)

# print(bm.columns)

# print(bm.index)

# for i in bm.index:
    #print(bm["name"][i])
# for i in bm.index:
    #print(bm.loc[i]['name'])
# for i in bm.index:

#    print(bm.iloc[i]['name'])

#for index, row in bm.iterrows():
    # print(bm.loc['name'][index])

# for index, row in bm.iterrows():
    # print(bm['name'][index])
# bm_arg = bm.query('iso_a3 == "ARG"')

# for i in range(len(df_arg)):

    # print(bm_arg.iloc[1])

#def get_new_country_name(row):
   # print(row)
   # new_country_name = f"{row['name']}({row['iso_a3']})"
   # print(new_country_name)
   # bm.apply(get_new_country_name,axis=1)
   # return new_country_name
# Was doing the apply function wrong somehow on this last section