# Importing modules (requests bs4)
import requests
# enables searching from taken html
from bs4 import BeautifulSoup 
# importing email file
from send_email import send_mail
# importing time module
import time

# Getting url
input_url = input("Enter the product link: ")
input_price = input("Enter the price that your product falls below: ")

def check_price(url, para_price):
    # For preventing be detected as a bot
    headers={
        "User-Agent":""
    }

    # Getting page
    page = requests.get(url, headers=headers)

    # Getting html page
    htmlPage = BeautifulSoup(page.content, 'html.parser')

    # Getting the name of the product
    product_title = htmlPage.find("h1", class_="pr-new-br").getText()

    # Getting the image of the product
    images = htmlPage.findAll("img")
    get_image = images[7]
    image = get_image.attrs['src']

    # Getting the price of the product
    price = htmlPage.find("span", class_="prc-slg prc-slg-w-dsc").getText()

    # price should be an integer or a float
    converted_price = float(price.replace(",",".").replace(" TL",""))

    # if the price has dropped, the message occurs
    if converted_price <= para_price:
        print("\nThe price of the product has dropped!")
        html_email_content= """\
                <html>
                <head></head>
                <body>
                <h3>{0}</h3>
                <br/>
                {1}
                <br/>
                <p>Product link: {2}</p>
                </body>
                </html>
                """.format(product_title, image, url)
        send_mail("mail_reciever", "The price of the product has just dropped", html_email_content)
    else:
        print("The price of the product has not dropped")

    print(converted_price)
    
while True:          
    check_price(input_url, input_price)
    time.sleep(600)