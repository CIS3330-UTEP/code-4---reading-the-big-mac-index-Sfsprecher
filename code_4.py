import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

bm = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3,date)"

def get_big_mac_price_by_country(country_code):
    cc = country_code.upper()
    # Creates logic for our country code to all be in UPPER CASE told by tutor I should use .upper() as it will work with github grade better 
    bm_by_country = bm[bm["iso_a3"] == country_code] 
    # sets our iso_a3 equal to contry code in our big-mac-index
    return round (bm_by_country["dollar_price"].mean(),2)
    # returns the dollar price mean for the country_code that is entdfdc
def get_the_cheapest_big_mac_price_by_year(year):

    query_text = f"((date >= '{year}-01-01' and date <= '{year}-12-31'))"
    min_bm = bm.query(query_text)
    min_idx= min_bm["dollar_price"].idxmin()
    price_min = min_bm.loc[min_idx, "dollar_price"]
    price_min_rounded = round (price_min,2)
    country_name = min_bm.loc[min_idx, "name"]
    country_3 = min_bm.loc[min_idx, "iso_a3"]
    print(f"{country_name}({country_3}): ${price_min_rounded}")

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
   year = 2010
   
   get_the_cheapest_big_mac_price_by_year(year)

   