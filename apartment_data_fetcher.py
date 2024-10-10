import requests
from bs4 import BeautifulSoup
import re
import statistics
from datetime import datetime 
import huf_to_eur
from config import SCRAPING_TARGET

class ApartmentDataFetcher:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        self.prices = []
        self.areas = []

    def fetch_apartment_price(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            all_prices = soup.find_all("h3", class_="item-price")
            self.prices = [price.find("span", class_="price-value").text.strip().replace(" ","") 
                           for price in all_prices if price.find("span", class_="price-value")]
            if not self.prices:
                print("Nem található árinformáció.")
        else:
            print(response.status_code)

    def fetch_apartment_area(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            all_areas = soup.find_all("section", class_="reLiSection sizeRooms")
            self.areas = [re.sub(r'm²','',area.find("div", class_="size").get_text(strip=True)) 
                          for area in all_areas if area.find("div", class_="size")]
            if not self.areas:
                print("Nem található alapterület információ.")  
        else:
            print(response.status_code) 

    def price_per_sqm(self):
        if len(self.prices) != len(self.areas):
            print("Hiba: Az árak és területek listáinak hossza nem egyezik meg.")
            return None
        huf_per_sqm = list(set([float(x) / float(y) for x, y in zip(self.prices, self.areas)]))
        return huf_per_sqm

    def get_apartment_data(self):
        self.fetch_apartment_price()
        self.fetch_apartment_area()
        prices_per_sqm = self.price_per_sqm()
        if prices_per_sqm:
            universal_sqm_price_huf = round(statistics.mean(prices_per_sqm))
            exchange_rate = huf_to_eur.get_huf_to_eur_rate()
            universal_sqm_price_eur = round(universal_sqm_price_huf * exchange_rate)
            one_million_huf_to_eur = exchange_rate * 1000000
            date = datetime.now().date()
            return date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur
        else:
            return None

def main():
    url = SCRAPING_TARGET 
    fetcher = ApartmentDataFetcher(url)
    apartment_data = fetcher.get_apartment_data()
    if apartment_data:
        date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur = apartment_data
        print(date)
        print("Universal Square Meter Price (HUF):", universal_sqm_price_huf)
        print("Universal Square Meter Price (EUR):", universal_sqm_price_eur)
        print("One million HUF to EUR:", one_million_huf_to_eur)

if __name__ == "__main__":
    main()