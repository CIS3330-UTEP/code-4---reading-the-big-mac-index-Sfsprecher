import pandas as pd
us_chronic_disease_file = './US_chronic_diseases.csv'
df = pd.read_csv(us_chronic_disease_file, low_memory=False)
#Use LocationAbbr to filter by state code

def get_melanoma_mortality_information_by_state(state_code):
    #Question = "Column Melanoma, mortality"
    query_text = f"LocationAbbr == '{state_code}' and Question == 'Melanoma, mortality' "
    #Filters for state code and Melaonoma, Mortalities
    df_d = df.query(query_text)
    mortality_mean = df_d["DataValueAlt"].mean()
    # Grabs the mean from the DataValueAlt column  
    morality_mean_rounded = round (mortality_mean,2)
    # Rounds to 2 decimals
    return morality_mean_rounded
    
def get_asthma_mortality_information_by_state(state_code):
    #Question = "Asthma mortality rate"
    query_text = f"LocationAbbr == '{state_code}' and Question == 'Asthma mortality rate'"
    df_d = df.query(query_text)
    Asthma_mean = df_d["DataValueAlt"].mean()
    Asthma_mean_rounded = round (Asthma_mean,2)
    return Asthma_mean_rounded
    # Same code from above just replaced with Asthma mortality rates instead

def get_chronic_liver_mortality_by_state(state_code):
    #Question = "Chronic liver disease mortality"
    #DataValueType = "Crude Rate"
    query_text = f"LocationAbbr == '{state_code}' and Question == 'Chronic liver disease mortality' and DataValueType == 'Crude Rate'"
    # Instead of being two queries like the following two functions this one needs another with the "Crude Rate"
    df_d = df.query(query_text)
    liver_mortality = df_d["DataValueAlt"].mean()
    liver_mortality_rounded = round (liver_mortality,2) 
    return liver_mortality_rounded
    # A little confusing to tell if I completed these right without autograder but the values look correct
    
def get_missing_values_count_by_state(state_code):
    #DataValueAlt
    #isnull().sum() functions to count all null values
    query_text = f"LocationAbbr == '{state_code}'"
    # we only need one query for this null function since we are only grabbing by state
    df_d = df.query(query_text)
    null_sum = df_d['DataValueAlt'].isnull().sum()
    print(null_sum)

if __name__ == "__main__":
   
   state_code = "GA"
   get_melanoma_mortality_information_by_state(state_code)
   get_asthma_mortality_information_by_state(state_code)
   get_chronic_liver_mortality_by_state(state_code)
   get_missing_values_count_by_state(state_code)