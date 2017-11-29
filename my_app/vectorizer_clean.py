from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import en_core_web_sm
import numpy as np
import pandas as pd
from MongoDB_hacks import simple_read_mongo
import pickle as pickle
from pymongo import MongoClient


class TextClassifer(object):
    ''' vectorize the preproccessed text into features'''

    def __init__(self):
        self._vectorizer = TfidfVectorizer(decode_error='ignore')

    def fit(self, X):
        '''fit_transform the vectorizer'''
        Tfidf = self._vectorizer.fit_transform(X)
        return Tfidf

    def transform(self, clean_ingredients):
        new_Tfidf = self._vectorizer.transform(clean_ingredients)
        return new_Tfidf



if __name__ == '__main__':
    db_client = MongoClient()
    db = db_client['allrecipes']
    savory_recipe_db = db['savory_recipe']
    df = simple_read_mongo(savory_recipe_db)
    X = df['combined']
    tc = TextClassifer()
    Tfidf = tc.fit(X)
    nlp = en_core_web_sm.load()
    with open('data/model.pkl', 'wb') as f:
        pickle.dump(tc, f)
    with open('data/tfidf.pkl', 'wb') as f:
        pickle.dump(Tfidf, f)
