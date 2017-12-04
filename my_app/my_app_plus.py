from flask import Flask, request, render_template
import pickle as pickle
import pandas as pd
import numpy as np
import spacy
import en_core_web_sm
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from vectorizer_clean import TextClassifer
from sklearn.metrics.pairwise import cosine_similarity
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
    print(ingredients)
    ingredients = ingredients[0].replace(', ', ',')
    ingredients=[ingredients]
    ingredients = ingredients[0].split(',')
    list_nlp = nlp_list(ingredients, nlp)
    print(list_nlp)
    remove = remove_pos_list(list_nlp)
    combined = [combine_words(i) for i in remove]
    clean = remove_extra_quotes(combined)
    print(combined)
    clean_raw = [clean]
    print(clean_raw)

    with open('data/pandas_actual.pkl', 'rb') as f:
        df = pickle.load(f)
    with open('data/model_actual.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('data/tfidf_actual.pkl', 'rb') as f:
        Tfidf = pickle.load(f)

    Tfidf_ingred = model.transform(clean_raw)
    new_Tfidf = np.append(Tfidf_ingred.toarray(), Tfidf.toarray())
    new_Tfidf = new_Tfidf.reshape(637, 1075)
    cosine_similarities = cosine_similarity(Tfidf, Tfidf_ingred)
    similar_indices = np.argsort(cosine_similarities, axis=0)[-5:-1]
    similar_items = [df.values[i] for i in similar_indices]
    title = similar_items[-1][0][4]
    description = similar_items[-1][0][7]
    ingredients = similar_items[-1][0][3]
    stars = similar_items[-1][0][6][:3]
    link= similar_items[-1][0][5]
    title_2 = similar_items[-2][0][4]
    description_2 = similar_items[-2][0][7]
    ingredients_2 = similar_items[-2][0][3]
    stars_2 = similar_items[-2][0][6][:3]
    link_2= similar_items[-2][0][5]
    title_3 = similar_items[-3][0][4]
    description_3 = similar_items[-3][0][7]
    ingredients_3 = similar_items[-3][0][3]
    stars_3 = similar_items[-3][0][6][:3]
    link_3= similar_items[-3][0][5]
    ingredients_for_groceries = similar_items[-1][0][1]

    return render_template('predict_template.html', data =(title, stars, description, ingredients, link, title_2, stars_2, description_2, ingredients_2, link_2, title_3, stars_3, description_3, ingredients_3, link_3), ingredients=ingredients_for_groceries, input_ingredients=clean)

@app.route('/get_groceries', methods=['GET', 'POST'])
def get_groceries():
    input_ingredients = request.args.get('input_ingredients')
    choice = request.args.get('ingredients')
    choice_update = choice.split(' ')
    input_ingredients_update = input_ingredients
    grocery_list = [val for val in choice_update if val not in input_ingredients_update]
    grocery_update = [grocery_list[i].replace('_', ' ') for i in range(len(grocery_list))]
    return render_template('grocery_template.html', data=grocery_update)
@app.route('/get_info')
def get_info():
    return render_template('info.html')

if __name__ == '__main__':
    nlp = en_core_web_sm.load()
    app.run(host='0.0.0.0', port=8080, debug=True)
