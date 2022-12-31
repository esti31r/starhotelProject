import requests
import pandas as pd
from bs4 import BeautifulSoup



branch_names = []
branch_rating = []

opset = 25
for i in range(7):

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    target_url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGqIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4AuCYnZ0GwAIB0gIkODY5NmI3MWUtMTcxNy00ZjFmLTk0ZTktNjQ4MGU3Y2I2NGRl2AIF4AIB&sid=df045411fb6cd87fd8af2d35cf08251b&aid=304142&dest_id=&ss=france&checkin_month=&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaGqIAQGYATG4ARfIAQ_YAQHoAQH4AQKIAgGoAgO4AuCYnZ0GwAIB0gIkODY5NmI3MWUtMTcxNy00ZjFmLTk0ZTktNjQ4MGU3Y2I2NGRl2AIF4AIB%26sid%3Ddf045411fb6cd87fd8af2d35cf08251b%26sb_price_type%3Dtotal%26%26&sb_lp=1&sb=1&src_elem=sb&checkin_year=&dest_type=&src=index&b_h4u_keep_filters=&search_selected=false&group_children=0&no_rooms=1&checkout_year=&is_ski_area=0&ss_raw=fg&checkout_month=&from_sf=1&group_adults=2&auth_success=1&search_pageview_id=205485b04d900109&offset="+str(opset)
    opset = opset + 25
    print(opset)
    resp = requests.get(target_url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    branches = soup.find_all("div", {"class": "a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"})
    for branch in branches:
         name = branch.find("div", {"class": "fcab3ed991 a23c043802"}).get_text()
         branch_names.append(name)
         rating = branch.find("div", {"class": "b5cd09854e d10a6220b4"}).get_text()
         branch_rating.append(rating)





df = pd.DataFrame({'Name':branch_names, 'rating':branch_rating})
df.to_excel("output.xlsx")
