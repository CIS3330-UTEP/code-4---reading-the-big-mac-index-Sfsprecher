import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

bm = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3,date)"

def get_big_mac_price_by_country(country_code):
    cc = country_code.upper()
    # Creates logic for our country code told by tutor I should use .upper() as it will work with github grade better 
    bm_by_country = bm[bm["iso_a3"] == country_code] 
    # 
    return round (bm_by_country["dollar_price"].mean(),2)

def get_the_cheapest_big_mac_price_by_year(year):

    query_text = f"((date >= '{year}-01-01' and date <= '{year}-12-31'))"
    min_bm = bm.query(query_text)
    min_idx= min_bm["dollar_price"].idxmin()
    return round (query_text["dollar_price"])

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
   
   get_the_cheapest_big_mac_price_by_year(2010)