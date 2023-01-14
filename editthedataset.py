import openpyxl
import pandas as pd
import numpy as np

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def load_csv(file_name):
    return pd.read_excel(file_name)


def check_facility_exists(df, facility):
  df[facility] = df['facilities'].apply(lambda x: facility in x)
  return df



def facilities_list_without_duplicates(lst_of_lst):
    facilities_list = []
    for sub_list in lst_of_lst:
        for val in eval(sub_list):
            if val not in facilities_list:
                facilities_list.append(val)
    return facilities_list


def extract_unique_values(df, col):
    all_values = [val.lower() for sublist in df[col] for val in sublist if isinstance(sublist, list) and all(isinstance(i, str) for i in sublist)]
    print(all_values)
    #remove the duplicates
    unique_values = list(dict.fromkeys(all_values))
    return unique_values


df_star_hotel = load_csv("FINAL.xlsx" )

print(df_star_hotel)
listObj = df_star_hotel['facilities'].tolist()

testedFacilitiesAndServices=facilities_list_without_duplicates(listObj)
#testedFacilitiesAndServices=extract_unique_values(df_star_hotel, 'facilities')
print(testedFacilitiesAndServices)
for facility in testedFacilitiesAndServices:
    print(facility)
    check_facility_exists(df_star_hotel, facility)
     


df_star_hotel.to_excel("FINALNEW.xlsx")