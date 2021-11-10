# Importing modules (requests bs4)
import requests
# enables searching from taken html
from bs4 import BeautifulSoup 

# Getting url
url1="https://www.trendyol.com/trendyolmilla/siyah-cicek-desenli-elbise-tclaw19lj0076-p-3371132"

# For preventing be detected as a bot
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

# Getting page
page = requests.get(url1, headers=headers)

# Getting html page
htmlPage = BeautifulSoup(page.content, 'html.parser')

# Getting the name of the product
product_title = htmlPage.find("h1", class_="pr-new-br").getText()

# Getting the price of the product
price = htmlPage.find("span", class_="prc-slg prc-slg-w-dsc").getText()

# price should be an integer or a float
converted_price = float(price.replace(",",".").replace(" TL",""))

# if the price has droped, the message occurs
if converted_price <= 150:
    print("\nThe price of the product has droped!")
print(converted_price)