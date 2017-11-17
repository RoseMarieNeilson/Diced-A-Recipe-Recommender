# Use spaCy
import spacy
import en_core_web_sm
from spacy.attrs import IS_STOP
from spacy.lang.en.stop_words import STOP_WORDS
'''run MongoDB_hacks_first to transform into pandas
    ingredients = df.ingred_list
    three = ingredients[0:2] (get a small list of ingredients to work on)
 '''
stop_words = ['freshly', 'head', 'chunks', 'cup','cups', 'teaspoon', 'teaspoons', 'tablespoon', 'tablespoons', 'pound', 'pounds', 'ounce', 'ounces', 'ground', 'powder', 'can', 'large', 'loaf', 'skinless', 'halves', 'spray', 'such', 'and', 'each', 'portion', 'quarters', 'slices']
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

def remove_pos(doc):
    doc_update = [t for t in doc if t.pos_ not in  ['VERB', 'NUM', 'PUNCT', 'ADP']]
    doc_updated = [ t for t in doc_update if t.is_stop == False]
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
for token in doc:
    print(token.text, token.pos_, token.tag_, token.dep_,     token.shape_, token.is_alpha, token.is_stop)

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

if __name__ == '__main__':
    main()
