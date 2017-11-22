from flask import Flask, request, render_template
import pickle as pickle
import pandas as pd
import numpy as np
import spacy
import en_core_web_sm
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from vectorizer_clean import TextClassifer
from sklearn.metrics.pairwise import cosine_similarity
from MongoDB_hacks import simple_read_mongo
from pre_processing_clean import nlp_list, remove_pos, remove_pos_list, combine_words, combine_words_list, remove_extra_quotes, stop_words_singular


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('css_template.html')

@app.route('/get_recommendation')
def get_recommendation():
    return '''
    <form action="/predict"
    method = 'POST'>
        <input type="text"
        name="user_input"/>
        <input type="submit" />
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    ingredients = [str(request.form['user_input'])]
    list_nlp = nlp_list(ingredients, nlp)
    remove = remove_pos_list(list_nlp)
    combine = combine_words_list(remove)
    clean = remove_extra_quotes(combine)
    clean_raw = [clean]
    db_client = MongoClient()
    db = db_client['allrecipes']
    savory_recipe_db = db['savory_recipe']
    df = simple_read_mongo(savory_recipe_db)
    X = df['combined']
    with open('data/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('data/tfidf.pkl', 'rb') as f:
        Tfidf = pickle.load(f)
    Tfidf_ingred = model.transform(clean_raw)
    new_Tfidf = np.append(Tfidf_ingred.toarray(), Tfidf.toarray())
    new_Tfidf = new_Tfidf.reshape(356, 679)
    cosine_similarities = cosine_similarity(Tfidf, Tfidf_ingred)
    similar_indices = np.argsort(cosine_similarities, axis=0)[-5:-1]
    similar_items = [df.values[i] for i in similar_indices]
    what_i_want = []
    what_i_want.append([similar_items[1][0][4], similar_items[1][0][6], similar_items[1][0][3]])
    return ','.join(str(lst) for lst in what_i_want)



if __name__ == '__main__':
    nlp = en_core_web_sm.load()
    app.run(host='0.0.0.0', port=8080, debug=True)
