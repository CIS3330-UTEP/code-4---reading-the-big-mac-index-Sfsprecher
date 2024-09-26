import pandas as py

filename = "./big-mac-full-index.csv"
bm = py.read_csv(filename)

# print(bm)

# print(bm.columns)

# query = f"(iso_a3 == 'MEX')"

# mxn_df = bm.query(query)


# print(mxn_df)

query = f"(iso_a3 == 'MEX')"

mxn_df = bm.query(query)

min_idx = mxn_df['dollar price'].idxmin()

print(min_idx)
