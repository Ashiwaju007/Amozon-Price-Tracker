import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B084F4KQYN/ref=sbl_dpx_B08GC6PL3D_0"
product = "Cuisinart GR-M3 STACK5 Multifunctional Grill"
my_email = "Email Goes Here"
password = "Password Goes Here"
response=requests.get(URL,
                      headers={
                          "Accept-Language":"en-US,en;q=0.9",
                          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
price = soup.find(name="span", id="mbc-price-1").getText()
f_price = price.split("$")[1]
float_price = float(f_price)
print(float_price)


if float_price < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ik.umez@yahoo.com",
            msg=f"Subject:Amazon Bot\n\n {product}\nPrice:{price}\nLink:{URL}")

