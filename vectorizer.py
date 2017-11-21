from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


http://blog.untrod.com/2016/06/simple-similar-products-recommendation-engine-in-python.html
vectorizer, unknowns, ignore

data = df['clean']


vec = TfidfVectorizer()
Tfidf = vec.fit_transform(data)
'''
look at tfidf
In [82]: print (Tfidf.toarray())
In [86]: vec.vocabulary_
'''

S = cosine_similarity(Tfidf)


ingredients = ['flour', 'salt', 'bacon', 'black pepper']

remove = remove_pos_list(nlp_list)
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
