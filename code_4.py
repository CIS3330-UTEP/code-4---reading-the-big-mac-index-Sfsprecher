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
    # this creates are query for the year that is entered using the dates within each year
    min_idx= min_bm["dollar_price"].idxmin()
    # Identifies the row with the lowest minimum for that row
    price_min = min_bm.loc[min_idx, "dollar_price"]
    # Finds the dollar price for that specific row using the loc 
    # I did ask CHAT gpt "How am I setting this line up wrong?" with my orignal line here without the loc.
    price_min_rounded = round (price_min,2)
    # uses for rounding the price to 2 decimals
    country_name = min_bm.loc[min_idx, "name"]
    # finds the country name for that row
    country_3 = min_bm.loc[min_idx, "iso_a3"]
    # finds the 3 letter 
    print(f"{country_name}({country_3}): ${price_min_rounded}'")
    # I know this is a very ugly long code but I was have trouble doing it the way I think it should be done so I improvised
def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"((date >= '{year}-01-01' and date <= '{year}-12-31'))"
    max_bm = bm.query(query_text)
    max_idx= max_bm["dollar_price"].idxmax()
    price_max = max_bm.loc[max_idx, "dollar_price"]
    price_max_rounded = round (price_max,2)
    country_name = max_bm.loc[max_idx, "name"]
    country_3 = max_bm.loc[max_idx, "iso_a3"]
    print(f"{country_name}({country_3}): ${price_max_rounded}'")
if __name__ == "__main__":
   year = 2003
   
   get_the_most_expensive_big_mac_price_by_year(year)

   