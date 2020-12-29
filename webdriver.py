from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_genre_year_price(artist, album_title):

    #define webdriver
    chrome = webdriver.Chrome('chromedriver') 

    #connect the site discogs ==> to find the genre and the year of the album
    chrome.get("https://www.discogs.com/fr/")

    #accept cookies ==> to allow the following scraping
    button_cookies = chrome.find_element_by_id("onetrust-accept-btn-handler")
    button_cookies.click()

    #search the album
    search_bar_discogs = chrome.find_element_by_id("search_q")
    search_bar_discogs.click()
    search_bar_discogs.send_keys(album_title)

    #show the searching result menu
    time.sleep(3)
    cartes = chrome.find_elements_by_class_name("ui-menu-item")

    #select the album with the correct artist on the menu
    for menu_item in cartes:
        if(menu_item.find_element_by_class_name("sublabel").text == artist):
            menu_item.click()
            break

    #get the genre and the year as album information and show it 
    infos = chrome.find_elements_by_class_name("content")
    genre = [element.text for element in infos][0]
    year = [element.text for element in infos][2]
    print(genre)
    print(year)

    chrome.get("https://www.amazon.fr")
    button_cookies = chrome.find_element_by_id("sp-cc-accept")
    button_cookies.click()
    search_bar_amazon = chrome.find_element_by_id("twotabsearchtextbox")
    search_bar_amazon.click()
    search_bar_amazon.send_keys(artist + " " + album_title + " CD")
    button_search = chrome.find_element_by_id("nav-search-submit-text")
    button_search.click()
    price = chrome.find_element_by_class_name("a-price-whole")
    print(price.text)

    return genre, year, price.text
    """#connect the site Fnac ==> to get the price of the album
    chrome.get("https://www.fnac.com")

    #search the album
    search_bar_fnac = chrome.find_element_by_id("Fnac_Search")
    search_bar_fnac.click()
    search_bar_fnac.send_keys(album_title + artist)
    button_search = chrome.find_elements_by_xpath('//*[@id="QuickSearchForm"]/div[2]/div/button')
    button_search[0].click()

    #search the correct album in the result page and show the price
    albums = chrome.find_elements_by_class_name("Article-itemGroup")
    for element in albums :
        if album_title in element.text:
            price = element.find_element_by_class_name("userPrice")
            print(price.text)
            break"""