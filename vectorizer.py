from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import en_core_web_sm
import numpy as np
import pandas as import pd
from MongoDB_hacks import simple_read_mongo
from pymongo import MongoClient

'''
http://blog.untrod.com/2016/06/simple-similar-products-recommendation-engine-in-python.html
vectorizer, unknowns, ignore
'''

class TextClassifer(object):
    ''' vectorize the preproccessed text into features'''

    def __init__(self):
        self._vectorizer = TfidfVectoizer(decode_error='ignore')

    def fit(self, X):
        '''fit_transform the vectorizer'''
        Tfidf = self._vectorizer.fit_transform(X)

    def transform(self, X):
        new_Tfidf = self._vectorizer.transform(X)




if __name__ == '__main__':
    db_client = MongoClient()
    db = db_client['allrecipes']
    savory_recipe_db = db['savory_recipe']
    X = clean_data
    tc = TextClassifer
    tc.fit(X)
    with open('data/model.pkl', 'wb') as f:
        pickle.dump(tc, f)


stop_words_singular = ['fresh', 'head', 'chunk', 'cup', 'teaspoon', 'tablespoon', 'pound', 'ounce', 'ground', 'grind', 'powder', 'can', 'large', 'loaf', 'skinless', 'spray', 'such', 'and', 'each', 'portion', 'quarters', 'slice', 'package', 'food', 'dice', 'or', 'to', 'optional', 'boneless','®', 'RO*TEL', 'and', 'spray', 'at', 'joint', 'inch', 'piece', 'pinch', 'half', 'third', 'white', 'quart', 'deep', 'frying', 'halve', 'fry', 'all', 'purpose', 'wide', 'thick', 'sprig', 'more', 'sharp', 'chuck', '2-inch', 'flat', 'leaf', 'floret', 'light', 'thin', 'blend','slice', 'small', 'cube', 'style', 'garnish', 'fine', 'natural', 'plus', 'much', 'granule', 'rough', 'casing', 'container', 'lean', 'sheet', 'mild', 'extra', 'jar', 'finely', 'spin-dry', 'bit', 'fat', 'giblets', 'stalk', 'freshly', 'thinly', 'lightly', 'real', 'bit', 'prepare', 'roughly', 'rough', 'low', 'sodium', 'uncooked', 'freeze', 'pasta', 'skim', 'part', 'strip', 'grate', 'crosswise', 'lengthwise', 'room', 'temperature', 'bottle', 'tough', 'bunch', 'bulk', 'store', 'refrigerated', 'dish', 'lightly', 'virgin', 'medium', 'pulp', 'wedge', 'the', 'no', 'boil', 'liquid', 'bite', 'size', 'clove', '1-inch', 'box', 'quarter', 'shred', 'shredded', 'enough', 'tart', 'core', 'cored', 'tough', 'bunch', 'undrained', 'your', 'favorite']

data = df['clean']


vec = TfidfVectorizer()
Tfidf = vec.fit_transform(data)
'''

for app?
    with open('data/model.pkl', 'rb') as f:
        model = pickle.load(f)

look at tfidf
In [82]: print (Tfidf.toarray())
In [86]: vec.vocabulary_
'''

S = cosine_similarity(Tfidf)


ingredients = ['flour', 'salt', 'bacon', 'black pepper']
list_nlp = nlp_list(ingredients)
remove = remove_pos_list(list_nlp)
combine = combine_words_list(remove)
clean = remove_extra_quotes(combine)
clean_raw = [clean]




clean_one = run ingredients through pre-processing

Tfidf_ingred = vec.transform(clean_one)


new_Tfidf = np.append(Tfidf_ingred.toarray(), Tfidf.toarray())

In [104]: new_Tfidf = new_Tfidf.reshape(355 + 1, 685)

In [106]: cosine_similarities = cosine_similarity(new_Tfidf)
cosine_similarities = cosine_similarity(Tfidf, Tfidf_ingred)

In [114]: for s in S_new:
     ...:     print (s)

'''
finds indices of most similar and returns top 10'''
similar_indices = np.argsort(cosine_similarities, axis=0)[-10:-1]
similar_items = [df.values[i] for i in similar_indices]

'''
create list of needed ingredients
returns clean ingred_list'''
choice = [similar_items[2][0][-1]]
input_ingredients

choice_update = choice.split(' ')
input_ingredients_update = ingredients[0].split(' ')

grocery_list = [val for val in choice_update if val not in input_ingredients_update]

grocery_update = [grocery_list[i].replace('_', ' ') for i in range(len(grocery_list))]


'''
rank by stars as well'''

stars = [similar_items[i][0][4] for i in range(len(similar_items))]

star_index = np.argsort(stars, axis=0)
highest_rated = [similar_items[i] for i in star_index][::-1]
