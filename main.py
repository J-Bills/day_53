import requests
from dataclasses import dataclass, fields
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selectolax.parser import HTMLParser



@dataclass
class RentalListing:
    url: str
    price: str
    address: str

# WIll be scraping the zillow snapshot and return list of rentallistings that are structured by our dataclass
class zillowScraper():
    def __init__(self) -> None:
        self.response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
        self.response.raise_for_status()
        self.html = HTMLParser(self.response.text)
        self.listings = list()
    
    def scrapePage(self) -> list:
        return self.listings

class googleFormInput():
    def __init__(self) -> None:
        self.chrome_options = self.webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get('https://doc.google.com/forms/')
        
    def login(self) -> None:
        pass
    
    def createForm(self) -> None:
        pass
    
    def inputData(self) -> None:
        pass
    
    #Will loop through and input all data returned from scraping
    def rentalListingInfo(self) -> None:
        pass