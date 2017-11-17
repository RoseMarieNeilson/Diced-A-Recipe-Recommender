# Use spaCy
import spacy
import en_core_web_sm
from spacy.attrs import IS_STOP
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang import en
import numpy as np
import pandas as import pd
from MongoDB_hacks import simple_read_mongo
from pymongo import MongoClient

'''run MongoDB_hacks_first to trans form into pandas
    ingredients = list(df.ingred_list)
    three = list(ingredients[0:3]) (get a small list of ingredients to work on)
 '''

stop_words_singular = ['freshly', 'head', 'chunk', 'cup', 'teaspoon', 'tablespoon', 'pound', 'ounce', 'ground', 'grind', 'powder', 'can', 'large', 'loaf', 'skinless', 'spray', 'such', 'and', 'each', 'portion', 'quarters', 'slices', 'package', 'food', 'diced', 'or', 'to', 'optional', 'boneless','®', 'RO*TEL', 'and', 'spray', 'at', 'joint', 'inch', 'piece', 'pinch', 'half', 'third', 'white', 'quart', 'deep', 'frying', 'halve', 'fry', 'all', 'purpose' ]

nlp = en_core_web_sm.load()
nlp.vocab.add_flag(lambda string: string in stop_words, IS_STOP)

#doc = nlp(document)
corpus = simple_read_mongo(coll)

def nlp_list(ingredients_list):
    doc = []
    for line in ingredients_list:
        fixed = nlp(line)
        doc.append(fixed)
    return doc

list_nlp = [nlp_list(i) for i in corpus ]
'''
not really working
def get_lemmas(recipe):
    lems = []
    for line in recipe:
        combine = []
        for token in line:
            combine.append(token.lemma_)
        lems.append(','.join(combine))
    return lems

lemmas = [get_lemmas(i) for i in list_nlp]
'''
    doc_updated = [ t for t in doc_update if t.is_stop == False]


def remove_pos(doc):
    doc_update = [t for t in doc if t.pos_ not in  ['VERB', 'NUM', 'PUNCT', 'ADP']]
    doc_updated = [t for t in doc_update if t.lemma_ not in stop_words_singular]
    return doc_updated

def remove_pos_list(lst):
    ready = [remove_pos(i) for i in lst]
    return ready

removed = [remove_pos_list(i) for i in list_nlp]



def combine_words(ingredient_parts):
    string = '_'.join(str(word) for word in ingredient_parts)
    return string

def combine_words_list(ingredient_parts_list):
    combine = [combine_words(i) for i in ingredient_parts_list]
    return combine

combined = [combine_words_list(i) for i in removed]

def remove_extra_quotes(recipe):
    string = ' '.join(word for word in recipe)
    return string

clean = [remove_extra_quotes(i) for i in combined]

def add_combined_to_df(combined):
    df['combined'] = combined

def add_to_mongo(coll, df):
    for x in range(0,len(df)):
        coll.update_many({'item_name': df.item_name[x]}, {'$set': {'combined': df.combined[x]}})

def add_to_mongo(coll, df):
    coll.update({'item_name': df.item_name[0]}, {'$set': {'combined': df.combined[0]}})



practice_db.update({'item_name': 'sugar coated peacans'}, {'$set': {'combined':


'''
doc_update = [t for t in line if t.pos_ not in  ['VERB', 'NUM', 'PUNCT', 'ADP'] for line in doc]

 doc _update = [t for line in doc for t in line if t.pos_ not in ['VERB', 'NUM', 'PUNCT', 'ADP']]

 doc_update = [t for t in l for l in doc if t.pos_ not in ['VERB', 'NUM', 'PUNCT', 'ADP']]

 doc_update = [l for l in doc for t in l if t.pos_ not in ['VERB', 'NUM', 'PUNCT', 'ADP']]

 for line in doc:
     for t in line:
         if t.pos_ not in  ['VERB', 'NUM', 'PUNCT', 'ADP'] for line in doc
         return t
'''
doc_update = [t for t in doc if t.pos_ not in  ['VERB', 'NUM', 'PUNCT', 'ADP']]
doc_updated = [ t for t in doc_update if t.is_stop == False]


'''Why do not in instead of t.pos_ == 'NOUN'? cauliflower = ADV, so it accidentally gets removed. Better to remove most things that don't belong and than add a list of adverb stopwords and other noun stop_words. '''

'''Thoughts on stopwords, how to handle cheese? read in each ingredient as a whole line so that cheese stays with its relative word ''

stop_words = ['freshly', 'head', 'chunks', 'cup', 'teaspoon', 'tablespoon', 'pound', 'ounce', 'ground', 'powder', 'can', 'large', 'loaf', 'skinless', 'halves']


'''
to look at tokens

for line in doc:
    for token in line:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

'''

# pipeline


from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(tokenizer=tokenize, stop_words=stop_words)



# stop words, tokenizing, spaCy, the restaurant

def tokenize(articles):
    corpus = [word_tokenize(word.lower()) for word in articles]
    return corpus

doc
def split_data(ingredients_list):
        string = ','.split(ingredients_list)
        return string

def clean_data(ingredients_list):
   string = ' '.join(ingredient for ingredient in ingredients_list)
   return string

lst = []
for ingred_list in corpus:
    clean = clean_data(ingred_list)
    lst.append(clean)

lst = [clean_data(i) for i in corpus]

def remove_stop_words(corpus):
    stop_words = ['1', '2', '3', '4','small', 'large', 'peeled', 'cubed', 'and', 'teaspoon', 'teaspoons', 'tablespoons', 'tablespoon', 'pound', 'gallon', 'ounce', 'ounces', 'pounds', 'chopped']
    corpus_clean = [[token for token in document if token not in stop_words] for document in corpus]
    return corpus_clean


['egg water pecan sugar salt cinnamon',
 'egg flour beer flour coconut shrimp oil',
 'oats brown_sugar wheat_germ cinnamon flour raisins salt honey egg vegetable_oil vanilla_extract',
 'bacon beef_cocktail_wieners brown_sugar',
 'vegetable_oil chicken_breast green_onion red_bell_pepper frozen_corn_kernels black_beans spinach jalapeno_peppers fresh_parsley cumin chili salt cayenne_pepper Monterey_Jack_cheese flour_tortillas oil_frying']


['egg water pecan sugar salt cinnamon',
 'egg all purpose flour beer  all purpose flour coconut shrimp oil',
 'oats brown sugar wheat germ cinnamon all purpose flour raisins salt honey egg vegetable oil vanilla extract',
 'bacon beef cocktail wieners brown sugar',
 'vegetable oil chicken breast green onion red bell pepper frozen corn kernels black beans spinach jalapeno peppers fresh parsley cumin chili salt cayenne pepper Monterey Jack cheese flour tortillas oil frying']

In [54]: S(underscores)
Out[54]:
array([[ 1.        ,  0.0791966 ,  0.24895476,  0.        ,  0.05412375],
       [ 0.0791966 ,  1.        ,  0.22606592,  0.        ,  0.        ],
       [ 0.24895476,  0.22606592,  1.        ,  0.13711971,  0.09704208],
       [ 0.        ,  0.        ,  0.13711971,  1.        ,  0.        ],
       [ 0.05412375,  0.        ,  0.09704208,  0.        ,  1.        ]])


In [60]: S(no scores)
Out[60]:
array([[ 1.        ,  0.0679605 ,  0.28249902,  0.09935216,  0.04007512],
       [ 0.0679605 ,  1.        ,  0.37682562,  0.        ,  0.09707128],
       [ 0.28249902,  0.37682562,  1.        ,  0.13772133,  0.12353923],
       [ 0.09935216,  0.        ,  0.13772133,  1.        ,  0.        ],
       [ 0.04007512,  0.09707128,  0.12353923,  0.        ,  1.        ]])




if __name__ == '__main__':
    main()
