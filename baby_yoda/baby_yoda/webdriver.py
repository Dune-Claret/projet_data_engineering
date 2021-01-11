from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common import exceptions  

def get_genre_year_price(artist, album_title):

    #define webdriver
    chrome = webdriver.Chrome('chromedriver') 

    #connect the site discogs ==> to find the genre and the year of the album
    chrome.get("https://www.discogs.com/fr/")

    #accept cookies ==> to allow the following scraping
    button_cookies = chrome.find_element_by_id("onetrust-accept-btn-handler")
    if button_cookies is not None :
        button_cookies.click()

    #search the album
    search_bar_discogs = chrome.find_element_by_id("search_q")
    search_bar_discogs.click()
    search_bar_discogs.send_keys(album_title + " ‎– " + artist)

    #show the searching result menu and click on the first element 
    chrome.implicitly_wait(5)
    cartes = chrome.find_elements_by_class_name("ui-menu-item")
    cpt = 0
    for element in cartes :
        cpt += 1
        try :
            if "(toutes les versions)" in element.text:
                #element.click()
                chrome.execute_script("arguments[0].click();", element)
                break
        except exceptions.StaleElementReferenceException:
            pass
    if cpt == len(cartes) :
        cartes[0].click()




    #get the genre and the year as album information and show it 
    heads = chrome.find_elements_by_class_name('head')
    infos = chrome.find_elements_by_class_name("content")
    iterator_genre = 0
    iterator_year = 0
    for i in range(len(heads)):
        if heads[i].text == "Genre:":
            iterator_genre = i
        elif heads[i].text in ["Year:", "Année:", "Sortie:"] :
            iterator_year = i
        else : pass
            
    genre = [element.text for element in infos][iterator_genre]
    year = int([element.text for element in infos][iterator_year])
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
    try :
        prices = chrome.find_elements_by_class_name("a-price-whole")
        price = float(prices[0].text.replace(",", "."))
        print(price)
    except NoSuchElementException:
        price = 0

    chrome.close()
    return genre, year, price
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