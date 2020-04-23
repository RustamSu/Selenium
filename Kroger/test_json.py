import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

url = "https://www.google.co.in"
#url = "https://www.kroger.com/d/beverages"
# r = requests.get(current_link)
# print(r.status_code)

r = requests.request("GET", url)
print(r.status_code)

# session = requests.Session()
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)
# session.mount('https://', adapter)
#
# r = session.get(current_link)
# print(r.status_code)

# a = \
#     [{'Pantry':{'items':[{"nameItem":"Beverages","href":"https://www.kroger.com/d/beverages","result":"Ok"},{"nameItem":"Breakfast","href":"https://www.kroger.com/d/breakfast","result":"Ok"},{"nameItem":"Snacks","href":"https://www.kroger.com/pl/snacks/01020","result":"Ok"},{"nameItem":"Packaged Breads","href":"https://www.kroger.com/pl/packaged-bread/01016","result":"Ok"},{"nameItem":"Canned Foods","href":"https://www.kroger.com/pl/canned-foods/01006","result":"Ok"},{"nameItem":"Baking and Cooking","href":"https://www.kroger.com/pl/baking-cooking/01012","result":"Ok"},{"nameItem":"Condiments and Sauces","href":"https://www.kroger.com/pl/condiments-sauces/01008","result":"Ok"},{"nameItem":"Pasta and Pasta Sauce","href":"https://www.kroger.com/pl/pasta-pasta-sauces/01010?searchType=curated","result":"Ok"},{"nameItem":"Grains, Beans and Rice","href":"https://www.kroger.com/pl/grains-beans-rice/01007","result":"Ok"},{"nameItem":"Packaged Meals and Sides","href":"https://www.kroger.com/pl/packaged-meals-sides/01011","result":"Ok"},{"nameItem":"Spreads, Jelly and Honey","href":"https://www.kroger.com/pl/spreads-jelly-honey/01014","result":"Ok"},{"nameItem":"Spices & Seasonings","href":"https://www.kroger.com/pl/spices-seasonings/01015","result":"Ok"},{"nameItem":"Shop All","href":"https://www.kroger.com/d/grocery","result":"Ok"}]}},{'Meat and Seafood':{'items':[{"nameItem":"Beef","href":"https://www.kroger.com/pl/beef/05001","result":"Ok"},{"nameItem":"Pork and Ham","href":"https://www.kroger.com/pl/pork-ham/05006","result":"Ok"},{"nameItem":"Bacon and Breakfast Sausage","href":"https://www.kroger.com/pl/bacon-breakfast-sausage/05017","result":"Ok"},{"nameItem":"Fish","href":"https://www.kroger.com/pl/fish/05004","result":"Ok"},{"nameItem":"Shrimp and Shellfish","href":"https://www.kroger.com/pl/shrimp-shellfish/05010","result":"Ok"},{"nameItem":"Turkey","href":"https://www.kroger.com/pl/turkey/05012","result":"Ok"},{"nameItem":"Lamb, Veal and Bison","href":"https://www.kroger.com/pl/lamb-veal-bison/05014","result":"Ok"},{"nameItem":"Hot Dogs and Franks","href":"https://www.kroger.com/pl/hot-dogs-franks/05005","result":"Ok"},{"nameItem":"Dinner Sausage","href":"https://www.kroger.com/pl/dinner-sausage/05003","result":"Ok"},{"nameItem":"Pepperoni, Salami and Summer Sausage","href":"https://www.kroger.com/pl/pepperoni-salami-summer-sausage/05015","result":"Ok"},{"nameItem":"Heat & Serve Meals and Sides","href":"https://www.kroger.com/pl/heat-serve-meals-and-sides/05016","result":"Ok"},{"nameItem":"Lunch & Snack Kits","href":"https://www.kroger.com/pl/lunch-snack-kits/05018","result":"Ok"},{"nameItem":"Packaged Deli Meats","href":"https://www.kroger.com/pl/packaged-deli-meat/05013","result":"Ok"},{"nameItem":"Shop All","href":"https://www.kroger.com/d/meat-seafood","result":"Ok"}]}}]
# with open('output_test.json', 'w') as outfile:
#     json.dump(a, outfile)