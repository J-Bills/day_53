from config import credential_dict
import requests
from dataclasses import dataclass, fields
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get('https://forms.gle/RYsCCz1QF3jSkJJPA')
            
    #Will loop through and input all data returned from scraping
    def inputRentalListingInfo(self, rental_listings) -> None:
        for listing in rental_listings:
            for field in fields(listing):
                field_name = field.name
                field_value = getattr(listing, field_name)
                input = self.driver.find_element()
                ActionChains(self.driver)\
                .move_to_element(input)\
                .pause(1)\
                .send_keys(field_value)\
                .pause(1)\
                .send_keys(Keys.TAB)\
                .pause(1)
            submit = self.driver.find_element(By.XPATH, '//span[text()="Submit"]').click()
            self.driver.implicitly_wait(5)
            refresh = self.driver.find_element(By.TAG_NAME, 'a').click()
    print('finished')
sum = googleFormInput()
sum.inputRentalListingInfo(rental_listings=placeholder)