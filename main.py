from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "testingjudahgggs1@gmail.com"
MY_PASSWORD = "Flashing5314"
TARGET_PRICE = float(70000)
URL = "https://www.amazon.in/dp/B08L5TTX14?ref=ods_ucc_kindle_B08L5TTX14_nrc_ucc"
parameters = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ta;q=0.7"
}

response = requests.get(url=URL, headers=parameters)
html = response.text
soup = BeautifulSoup(html, "lxml")
price_soup = soup.find(name="span", class_="priceBlockDealPriceString").text.replace(u'\xa0', '')
price_without_currency = price_soup.split("₹")[1].replace(',', '')
price_as_float = float(price_without_currency)
print(price_as_float)
if price_as_float < TARGET_PRICE:
    title = soup.find(name="span", class_="product-title-word-break").text
    current_price = soup.find(name="span", class_="priceBlockDealPriceString").text
    with smtplib.SMTP("smtp.gmail.com", port=587)as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="georgejudah5@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{title}\nnow for {current_price}\n{URL}".encode(
                                "utf-8"))
