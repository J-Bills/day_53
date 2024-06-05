import requests
from dataclasses import dataclass, fields
from selenium import webdriver
from selenium.webdriver import By, Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selectolax.parser import HTMLParser



@dataclass
class RentalListing:
    url: str
    price: str
    address: str

# WIll be scraping the zillow snapshot and return list of rentallistings that are structured by our dataclass
class zillowScraper():
    def __init__(self) -> None:
        response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
        response.raise_for_status()
        self.html = HTMLParser(response.text)
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
    def rentalListingInfo(self, rental_listings) -> None:
        for field in fields(rental_listings):
            field_name = field.name
            field_value = getattr(rental_listings, field_name)
            input = self.driver.find_element()
            ActionChains(self.driver)\
            .move_to_element(input)\
            .pause(1)\
            .send_keys(field_value)\
            .send_keys(Keys.TAB)\
            .send_keys(field_value)\
            .send_keys(Keys.TAB)\
            .send_keys(field_value)\
            .send_keys(Keys.TAB)\
            .perform()