import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from pymongo import MongoClient
from urllib.request import urlopen




def get_url(url):
    all_recipes = urlopen(url)
    recipes_html = all_recipes.read()
    all_recipes.close()

    soup = BeautifulSoup(recipes_html, 'lxml')
    all_recipes_all = soup.find_all("a")
    url_links = []
    # for links in soup.find_all('a'):
    #     url_links.append((links.get('href')))

    for a in url_links:
        link = str(a.get('href')).strip()

        if link[:8]=='/recipe/':
            url_list.append(a)

def store_data(mongo_update_lst, recipe_db):
    '''
    Store Recipe Information in MongoDB
    '''
    for json_dct in mongo_update_lst:
        recipe_db.insert_one(json_dct)
    pass

def scrape_search(list_link):
    '''

    Input:  (1) link to search page
            (2) recipe MongoDB
    Output: (1) list of data to be stored in MongoDB
    '''

    #Parse url string to locate recipe name and number

    mongo_update_lst = []
    for recipe in list_link:
        r= request_info(recipe)
        mongo_update_lst.append(r)

    return mongo_update_lst

def request_info(link):
    content = requests.get(link).content
    soup = BeautifulSoup(content, "lxml")

    item_name = soup.find('h1', {'class':'recipe-summary__h1'}).text
    submitter_name = soup.find('span', {'class':'submitter__name'}).text
    submitter_desc = soup.find('div', {'class':'submitter__description'}).text
    stars = soup.find('div', {'class':'rating-stars'}).get('data-ratingstars')
    ingred_list = []

    for s in soup.findAll('li', {'class': 'checkList__line'}):
            ingred = s.text.strip()
            if not ingred.startswith('Add') and not ingred.startswith('ADVERTISEMEN'):
                ingred_list.append(ingred[:s.text.strip().find('\n')])

    directions = soup.findAll('span', {'class':'recipe-directions__list--item'})
    direction_list = [d.text for d in directions]


    json_dct = ({'item_name': item_name, 'ingred_list':ingred_list, 'direction_list':direction_list, 'stars': stars, 'submitter_name':submitter_name, 'submitter_desc': submitter_desc})
    return json_dct



if __name__ == '__main__':
    url = "http://allrecipes.com/recipe/260696/cauliflower-pizza-bites/"
    db_client = MongoClient()
    db = db_client['allrecipes']
    recipe_db = db['recipe_data']
    savory_recipe_db = db['savory_recipe']
    practice_db = db['practice']
    
