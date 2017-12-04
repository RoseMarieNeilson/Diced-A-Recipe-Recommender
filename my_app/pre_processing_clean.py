import spacy
import en_core_web_sm
import numpy as np
import pandas as pd
from MongoDB_hacks import simple_read_mongo
from pymongo import MongoClient

def nlp_list(ingredients_list, nlp):
    doc = []
    for line in ingredients_list:
        fixed = nlp(line)
        doc.append(fixed)
    return doc

def remove_pos(doc):
    doc_update = [t for t in doc if t.pos_ not in  ['VERB', 'NUM', 'PUNCT', 'ADP']]
    doc_updated = [t for t in doc_update if t.lemma_ not in stop_words_singular]
    return doc_updated

def remove_pos_list(lst):
    ready = [remove_pos(i) for i in lst]
    return ready


def combine_words(ingredient_parts):
    string = '_'.join(str(word) for word in ingredient_parts)
    return string

def combine_words_list(ingredient_parts_list):
    combine = [combine_words(i) for i in ingredient_parts_list]
    return combine


def remove_extra_quotes(recipe):
    string = ' '.join(word for word in recipe)
    return string


def add_cleaned_to_df(clean):
    df['clean'] = clean

def add_to_mongo(coll, df):
    for x in range(0,len(df)):
        coll.update_many({'item_name': df.item_name[x]}, {'$set': {'combined': df.clean[x]}})


stop_words_singular = ['fresh', 'head', 'chunk', 'cup', 'teaspoon', 'tablespoon', 'pound', 'ounce', 'ground', 'grind', 'powder', 'can', 'large', 'loaf', 'skinless', 'spray', 'such', 'and', 'each', 'portion', 'quarters', 'slice', 'package', 'food', 'dice', 'or', 'to', 'optional', 'boneless','®', 'RO*TEL', 'and', 'spray', 'at', 'joint', 'inch', 'piece', 'pinch', 'half', 'third', 'white', 'quart', 'deep', 'frying', 'halve', 'fry', 'all', 'purpose', 'wide', 'thick', 'sprig', 'more', 'sharp', 'chuck', '2-inch', 'flat', 'leaf', 'floret', 'light', 'thin', 'blend','slice', 'small', 'cube', 'style', 'garnish', 'fine', 'natural', 'plus', 'much', 'granule', 'rough', 'casing', 'container', 'lean', 'sheet', 'mild', 'extra', 'jar', 'finely', 'spin-dry', 'bit', 'fat', 'giblets', 'stalk', 'freshly', 'thinly', 'lightly', 'real', 'bit', 'prepare', 'roughly', 'rough', 'low', 'sodium', 'uncooked', 'freeze', 'pasta', 'skim', 'part', 'strip', 'grate', 'crosswise', 'lengthwise', 'room', 'temperature', 'bottle', 'tough', 'bunch', 'bulk', 'store', 'refrigerated', 'dish', 'lightly', 'virgin', 'medium', 'pulp', 'wedge', 'the', 'no', 'boil', 'liquid', 'bite', 'size', 'clove', '1-inch', 'box', 'quarter', 'shred', 'shredded', 'enough', 'tart', 'core', 'cored', 'tough', 'bunch', 'undrained', 'your', 'favorite']


if __name__ == '__main__':
    nlp = en_core_web_sm.load()
    stop_words_singular = ['fresh', 'head', 'chunk', 'cup', 'teaspoon', 'tablespoon', 'pound', 'ounce', 'ground', 'grind', 'powder', 'can', 'large', 'loaf', 'skinless', 'spray', 'such', 'and', 'each', 'portion', 'quarters', 'slice', 'package', 'food', 'dice', 'or', 'to', 'optional', 'boneless','®', 'RO*TEL', 'and', 'spray', 'at', 'joint', 'inch', 'piece', 'pinch', 'half', 'third', 'white', 'quart', 'deep', 'frying', 'halve', 'fry', 'all', 'purpose', 'wide', 'thick', 'sprig', 'more', 'sharp', 'chuck', '2-inch', 'flat', 'leaf', 'floret', 'light', 'thin', 'blend','slice', 'small', 'cube', 'style', 'garnish', 'fine', 'natural', 'plus', 'much', 'granule', 'rough', 'casing', 'container', 'lean', 'sheet', 'mild', 'extra', 'jar', 'finely', 'spin-dry', 'bit', 'fat', 'giblets', 'stalk', 'freshly', 'thinly', 'lightly', 'real', 'bit', 'prepare', 'roughly', 'rough', 'low', 'sodium', 'uncooked', 'freeze', 'skim', 'part', 'strip', 'grate', 'crosswise', 'lengthwise', 'room', 'temperature', 'bottle', 'tough', 'bunch', 'bulk', 'store', 'refrigerated', 'dish', 'lightly', 'virgin', 'medium', 'pulp', 'wedge', 'the', 'no', 'boil', 'liquid', 'bite', 'size', 'clove', '1-inch', 'box', 'quarter', 'shred', 'shredded', 'enough', 'tart', 'core', 'cored', 'tough', 'bunch', 'undrained', 'your', 'favorite']
    db_client = MongoClient()
    db = db_client['allrecipes']
    savory_recipe= db['actual']
    df = simple_read_mongo(savory_recipe)
    '''
    to clean and add corpus'''
    corpus = list(df.ingred_list)
    list_nlp = [nlp_list(i) for i in corpus]
    removed = [remove_pos_list(i) for i in list_nlp]
    combined = [combine_words_list(i) for i in removed]
    clean = [remove_extra_quotes(i) for i in combined]
    add_cleaned_to_df(clean)
    add_to_mongo(savory_recipe, df)
    '''
    to clean ingredient list'''
    '''
    ingredients = input_ingredients
    list_nlp = nlp_list(ingredients)
    remove = remove_pos_list(list_nlp)
    combine = combine_words_list(remove)
    clean = remove_extra_quotes(combine)
    clean_raw = [clean]'''
