from flask import Flask, request, render_template
import pickle as pickle
import pandas as pd
import numpy as np
import spacy
import en_core_web_sm
import string
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
    return render_template('recommend_template.html')

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
    title = similar_items[1][0][4]
    description = similar_items[1][0][6]
    ingredients = similar_items[1][0][3]
    title_2 = similar_items[2][0][4]
    description_2 = similar_items[2][0][6]
    ingredients_2 = similar_items[2][0][3]
    title_3 = similar_items[3][0][4]
    description_3 = similar_items[3][0][6]
    ingredients_3 = similar_items[3][0][3]
    ingredients_for_groceries = similar_items[1][0][1]

    return render_template('predict_template.html', data = (title, description, ingredients, title_2, description_2, ingredients_2, title_3, description_3, ingredients_3), ingredients=ingredients_for_groceries, input_ingredients=clean)

@app.route('/get_groceries', methods=['GET', 'POST'])
def get_groceries():
    input_ingredients = request.args.get('input_ingredients')
    choice = request.args.get('ingredients')
    print(type(input_ingredients))
    print(input_ingredients)
    print(type(choice))
    print(choice)
    choice_update = choice.split(' ')
    print(type(choice_update))
    print(choice_update)
    input_ingredients_update = input_ingredients
    print(type(input_ingredients_update))
    print(input_ingredients_update)
    grocery_list = [val for val in choice_update if val not in input_ingredients_update]
    print(type(grocery_list))
    print(grocery_list)
    grocery_update = [grocery_list[i].replace('_', ' ') for i in range(len(grocery_list))]
    print(grocery_update)
    return render_template('grocery_template.html', data=grocery_update)

if __name__ == '__main__':
    nlp = en_core_web_sm.load()
    app.run(host='0.0.0.0', port=8080, debug=True)
