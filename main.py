import pandas as pd
import requests
from bs4 import BeautifulSoup


def check_facility_exists(df, facility):
  df[facility] = df['facilities'].apply(lambda x: facility in x)
  return df



def facilities_list_without_duplicates(lst_of_lst):
    facilities_list = []
    for sub_list in lst_of_lst:
        for val in sub_list:
            if val not in facilities_list:
                facilities_list.append(val)
    return facilities_list

#  create Lists
branch_names = []
branch_rating = []
branch_facilitiesAndServices = []
branch_numOfFacilitiesAndServices =[]
cities = [
      "Paris" "Marseille", "Lyon" , "Nice", "Nantes", "Strasbourg"
]
branch_city = []

for k in range(len(cities)):
        opset = 0
        for i in range(39):
            print(cities[k])
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            try:
             target_url = "https://www.booking.com/searchresults.en-us.html?aid=7965225&lang=en-us&sid=4dc310284f88d2a3f8b9c9061560a7ef&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-us.html%3Faid%3D7965225%26sid%3D4dc310284f88d2a3f8b9c9061560a7ef%26sb_price_type%3Dtotal%3Bsrpvid%3Dcc2f829be2810053%26%26&ss="+cities[k]+"&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=france&ac_position=0&ac_langcode=en&ac_click_type=b&ac_meta=GhA5YzVjODJhMGUyY2IwMjkxIAAoATICZW46BmZyYW5jZUAASgBQAA%3D%3D&dest_id=73&dest_type=country&place_id_lat=46.8664&place_id_lon=2.59596&search_pageview_id=9c5c82a0e2cb0291&search_selected=true&search_pageview_id=9c5c82a0e2cb0291&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&offset="+str(opset)
            except:
             print("ERORR")
            opset = opset + 25
            print(opset)
            try:
             resp = requests.get(target_url, headers=headers)
             soup = BeautifulSoup(resp.text, 'html.parser')
            except:
                print("ERORR2")
            branches = soup.find_all("div", {"class": "a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"})
            a_href = soup.find_all("a", {"class": "e13098a59f"})

            for branch in branches:
                try:
                    name = branch.find("div", {"class": "fcab3ed991 a23c043802"}).get_text()
                    rating = branch.find("div", {"class": "b5cd09854e d10a6220b4"}).get_text()
                    href = branch.find("a", {"class": "e13098a59f"}).get("href")
                    resp_herf = requests.get(href, headers=headers)
                    soup_herf = BeautifulSoup(resp_herf.text, 'html.parser')
                    facilitiesAndServices = soup_herf.find_all("div", {"class": "bui-list__description"})
                except:
                    print("An exception occurred")

                facilitiesAndServices_text = [i.get_text() for i in facilitiesAndServices]
                branch_names.append(name)
                branch_rating.append(rating)
                branch_numOfFacilitiesAndServices.append(len(facilitiesAndServices))
                branch_facilitiesAndServices.append(facilitiesAndServices_text)
                branch_city.append(cities[k])


        


 #delete the newline character \n at the beginning and end of each string in a list of lists
stripped_list_of_lists = [[val.strip() for val in sublist] for sublist in branch_facilitiesAndServices]

#create a list of all the facilities in all the hotels
testedFacilitiesAndServices = facilities_list_without_duplicates(branch_facilitiesAndServices)
#create the first basic df before split the facilities coloumn
df = pd.DataFrame({'Name':branch_names, 'rating':branch_rating , 'facilities':stripped_list_of_lists, 'numOfFacilitiesAndServices':branch_numOfFacilitiesAndServices  ,'City':branch_city})

#Create coloumn for each facility that we want to check (from the list above)
#and check if exists using function and set boolean value in the new column
for facility in testedFacilitiesAndServices:
     check_facility_exists(df, facility)

df.to_excel("FINAL.xlsx")
