import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

bm = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    

def get_big_mac_price_by_country(country_code):
    cc = country_code.upper()
    # Creates logic for our country code told by tutor I should use .upper() as it will work with github grade better 
    bm_by_country = bm[bm["iso_a3"] == country_code] 
    # 
    return round (bm_by_country["dollar_price"].mean(),2)

def get_the_cheapest_big_mac_price_by_year(year):
    
    

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
   