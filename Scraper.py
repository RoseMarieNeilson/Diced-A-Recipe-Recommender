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
    appetizers_snacks_urls = ["http://allrecipes.com/recipe/260696/cauliflower-pizza-bites/", "http://allrecipes.com/recipe/157940/outrageous-warm-chicken-nacho-dip/", "http://allrecipes.com/recipe/237835/big-rays-mexican-monkey-bread/", "http://allrecipes.com/recipe/219106/garlic-ginger-chicken-wings/", "http://allrecipes.com/recipe/68461/buffalo-chicken-dip/", "http://allrecipes.com/recipe/15184/mouth-watering-stuffed-mushrooms/", "http://allrecipes.com/recipe/212394/flayed-man-cheese-ball/", "http://allrecipes.com/recipe/216756/baked-ham-and-cheese-party-sandwiches/", "http://allrecipes.com/recipe/176957/baked-kale-chips/", "http://allrecipes.com/recipe/239969/no-bake-energy-bites/", "http://allrecipes.com/recipe/189930/southern-pimento-cheese/", "http://allrecipes.com/recipe/9450/glazed-nuts/", "http://allrecipes.com/recipe/137428/blue-bacon-stuffed-mushrooms/", "http://allrecipes.com/recipe/260318/chorizo-fundido/", "http://allrecipes.com/recipe/19687/cream-cheese-penguins/",
    "http://allrecipes.com/recipe/19687/cream-cheese-penguins/", "http://allrecipes.com/recipe/14231/guacamole/", "http://allrecipes.com/recipe/13768/roasted-pumpkin-seeds/", "http://allrecipes.com/recipe/13870/deviled-eggs/", "http://allrecipes.com/recipe/15206/cocktail-meatballs/", "http://allrecipes.com/recipe/220080/sausage-stuffed-mushrooms/", "http://allrecipes.com/recipe/240136/crispy-pork-belly/", "http://allrecipes.com/recipe/240246/easy-endive-cranberry-walnut-appetizers/", "http://allrecipes.com/recipe/240805/boudin-balls/", "http://allrecipes.com/recipe/241555/homemade-beef-jerky/", "http://allrecipes.com/recipe/242208/grilled-spicy-sweet-potato-chips/", "http://allrecipes.com/recipe/245291/brie-cups/", "http://allrecipes.com/recipe/245295/crispy-fried-tofu/", "http://allrecipes.com/recipe/257651/ashleis-smoked-trout-dip/", "http://allrecipes.com/recipe/222589/simple-deviled-eggs/",
    "http://allrecipes.com/recipe/223491/fully-loaded-deviled-eggs/", "http://allrecipes.com/recipe/20509/best-ever-party-appetizer/", "http://allrecipes.com/recipe/17076/king-crab-appetizers/", "http://allrecipes.com/recipe/240702/pine-cone-cheese-ball/", "http://allrecipes.com/recipe/22617/best-spinach-dip-ever/", "http://allrecipes.com/recipe/68461/buffalo-chicken-dip/", "http://allrecipes.com/recipe/26692/annies-fruit-salsa-and-cinnamon-chips/", "http://allrecipes.com/recipe/15184/mouth-watering-stuffed-mushrooms/", "http://allrecipes.com/recipe/139012/jalapeno-popper-spread/", "http://allrecipes.com/recipe/24087/restaurant-style-buffalo-chicken-wings/", "http://allrecipes.com/recipe/20669/double-tomato-bruschetta/", "http://allrecipes.com/recipe/19673/seven-layer-taco-dip/", "http://allrecipes.com/recipe/14939/brown-sugar-smokies/", "http://allrecipes.com/recipe/71722/asian-lettuce-wraps/", "http://allrecipes.com/recipe/14830/hummus-iii/"]

    others = ["http://allrecipes.com/recipe/13838/sugar-coated-pecans/", "http://allrecipes.com/recipe/17753/coconut-shrimp-i/", "http://allrecipes.com/recipe/81298/playgroup-granola-bars/", "http://allrecipes.com/recipe/69919/bacon-wrapped-smokies/", "http://allrecipes.com/recipe/25502/southwestern-egg-rolls/"]

    dinner = ["http://allrecipes.com/recipe/190100/porkolt-hungarian-stew-made-with-pork/", "http://allrecipes.com/video/7761/cider-braised-pork-shoulder/", "http://dish.allrecipes.com/rich-and-delicious-pumpkin-pastas-for-fall/", "http://allrecipes.com/recipes/17139/main-dish/chicken/chicken-marsala/", "http://allrecipes.com/recipe/23600/worlds-best-lasagna/", "http://allrecipes.com/recipe/178498/mushroom-slow-cooker-roast-beef/", "http://allrecipes.com/recipe/23431/to-die-for-fettuccine-alfredo/", "http://allrecipes.com/recipe/223042/chicken-parmesan/", "http://allrecipes.com/recipe/51283/maple-salmon/", "http://allrecipes.com/recipe/25203/brown-sugar-meatloaf/", "http://allrecipes.com/recipe/219164/the-best-parmesan-chicken-bake/", "http://allrecipes.com/recipe/220854/chef-johns-italian-meatballs/", "http://allrecipes.com/recipe/222002/chef-johns-stuffed-peppers/", "http://allrecipes.com/recipe/83557/juicy-roasted-chicken/"]
    dinner_more = ["http://allrecipes.com/recipe/235997/unstuffed-cabbage-roll/", "http://allrecipes.com//recipe/15679/asian-beef-with-snow-peas/", "http://allrecipes.com/recipe/23847/pasta-pomodoro/", "http://allrecipes.com/recipe/50435/fry-bread-tacos-ii/", ]

    mongo_list = scrape_search(dinner)
    store_data(mongo_list, recipe_db)

# cursor = recipe_db.find({})
# for document in cursor:
#     print(document)
#url_list = [/recipes/76/appetizers-and-snacks/
# /recipes/78/breakfast-and-brunch/
# /recipes/79/desserts/
# /recipes/17562/dinner/
# /recipes/77/drinks/
# /recipes/200/meat-and-poultry/beef/
# /recipes/201/meat-and-poultry/chicken/
# /recipes/95/pasta-and-noodles/
# /recipes/205/meat-and-poultry/pork/
# /recipes/416/seafood/fish/salmon/
# /recipes/739/healthy-recipes/diabetic/
# /recipes/741/healthy-recipes/gluten-free/
# /recipes/84/healthy-recipes/
# /recipes/1232/healthy-recipes/low-calorie/
# /recipes/1231/healthy-recipes/low-fat/
# http://allrecipes.com/recipes/198/holidays-and-events/thanksgiving/
# http://allrecipes.com/recipes/841/holidays-and-events/christmas/desserts/christmas-cookies/
# http://allrecipes.com/recipes/190/holidays-and-events/hanukkah/
# http://allrecipes.com/recipes/187/holidays-and-events/christmas/
# http://allrecipes.com/recipes/85/holidays-and-events/
# /recipes/156/bread/
# /recipes/276/desserts/cakes/
# /recipes/96/salad/
# /recipes/138/drinks/smoothies/
# /recipes/94/soups-stews-and-chili/
# /recipes/88/bbq-grilling/
# /recipes/1947/everyday-cooking/quick-and-easy/
# /recipes/253/everyday-cooking/slow-cooker/
# /recipes/1227/everyday-cooking/vegan/
# /recipes/87/everyday-cooking/vegetarian/
# /recipes/227/world-cuisine/asian/
# /recipes/233/world-cuisine/asian/indian/
# /recipes/723/world-cuisine/european/italian/
# /recipes/728/world-cuisine/latin-american/mexican/
# /recipes/15876/us-recipes/southern/
# http://allrecipes.com/recipes/17235/everyday-cooking/allrecipes-magazine-recipes/
# http://allrecipes.com/recipes/16791/everyday-cooking/special-collections/web-show-recipes/food-wishes/]
#
