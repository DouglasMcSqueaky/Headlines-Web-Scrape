import requests 
from bs4 import BeautifulSoup 

def scrape_goldprice(): 
    url = "https://www.marketwatch.com/investing/future/gc00"
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("h2", {"class": "intraday__price"})
    
    for article in articles: 
        price = article.find("bg-quote").text
        print("Gold: $", price)
        print()
        
def scrape_btcprice(): 
    url = "https://www.marketwatch.com/investing/cryptocurrency/btcusd?mod=home-page"
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("h2", {"class": "intraday__price"})
    
    for article in articles: 
        price = article.find("bg-quote").text
        print("Bitcoin: $", price)
        print()
        
def scrape_xmrprice(): 
    url = "https://www.marketwatch.com/investing/cryptocurrency/xmrusd?mod=home-page"
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("h2", {"class": "intraday__price"})
    
    for article in articles: 
        price = article.find("bg-quote").text
        print("Monero: $", price)
        print()
    
def scrape_reuters(): 
    url = "https://www.reuters.com/news/archive/worldNews"
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("div", {"class": "story-content"})
    
    for article in articles: 
        title = article.find("a").text
        link = article.find("a")["href"]
        titleStrip = title.strip()
        print(f"{titleStrip}")
        print("reuters.com",link)
        print()
        
    
scrape_goldprice()
scrape_btcprice()
scrape_xmrprice()
scrape_reuters()