""" 
Next step will be to gather exchange rate from a good api, instead of a webpage scrape 

from forex_python.converter import CurrencyRates

c = CurrencyRates()

def huf_to_eur(amount):
    conversion = c.convert('HUF', 'EUR', amount)
    print(f'{amount} HUF = {conversion} EUR')
    return conversion

    <div class="result-box-c1-c2">
                            <div>1 HUF = 0.002582
                                EUR
                            </div>
                            <div>1 EUR = 387.296669249
                                HUF</div>
                        </div> """
import requests
from bs4 import BeautifulSoup

def get_huf_to_eur_rate():
    url = "https://www.forbes.com/advisor/money-transfer/currency-converter/huf-eur/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        exchange_rate_element = soup.find("div", class_="result-box-c1-c2")
        #print(exchange_rate_element)
        if exchange_rate_element: 
            exchange_rate_element_text = exchange_rate_element.text
            start_index = exchange_rate_element_text.find('=')  # Az '=' karakter pozíciója
            end_index = exchange_rate_element_text.find('EUR', start_index)  # Az 'EUR' string pozíciója az '=' karakter után
            exchange_rate_text = exchange_rate_element_text[start_index + 1 :end_index].strip()  # Az '=' utáni rész kivágása és tisztítása
            exchange_rate = float(exchange_rate_text)          
            return exchange_rate
        
        else: print("Az átváltott árfolyam nem található az oldalon.")
    else: print(response.status_code)

def main():
    exchange_rate = get_huf_to_eur_rate()
    print(exchange_rate)

if __name__ == "__main__":
    main()
    
"""
if exchange_rate is not None:
    print(f"Aktuális HUF/EUR árfolyam: {exchange_rate}")
else:
    print("Nem sikerült lekérni az árfolyamot.") """
