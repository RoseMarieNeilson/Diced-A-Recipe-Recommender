# Diced-capstone

[Concept](concept)
[Data](data)
[Data Storage](data_storage)
[Natural Language Processing](natural_language_processing)
[Modeling](modeling)
[Web App](web_app)
[Visualization](visualization)
[Future Goals](future_goals)





### Concept
The goal of this project is to create a recipe recommender system that will produce recipe suggestions based on ingredients the user has on hand. This app will also provide ratings of the recipes based on the star ratings provided by the scraped data from Allrecipes.com. A further goal would be to create user profiles that can rate recipes and get improved suggestions with time.

### Data
Data was scraped from Allrecipes.com using BeautifulSoup with an attempt to get a variety of recipes under topics such as dessert, dinner, and appetizers. It was stored in a MongoDB database with the following keys: item_name, ingredient_list, direction_list, stars, submitter_name, and submitter_desc.


### Data Storage
The data will be stored on an S3 bucket.


### Natural Language Processing
  In order to recommend recipes the ingredient list column needs to processed. This includes removing stop words ('cup', 'teaspoon', etc), lowercasing all words, and experimenting with different stemming and lemmatizing techniques to find the root words (changing 'apples' to 'apple').
  call counter on my words, see what's most common.

### Modeling
Distance metric (cosine similarity), pairwise similarity. content based recommender. ingredient comparison for recipes. pull recipes that are most similar. bonus would be to order by similarity and stars. Extra bonus would be t make a hybrid recommender.

### Resources to read
https://www.kernix.com/blog/recommender-system-based-on-natural-language-processing_p10

https://in.pycon.org/cfp/2016/proposals/creating-a-recommendation-engine-based-on-nlp-and-contextual-word-embeddings~aOZGe/?ref=schedule

http://courses.ischool.berkeley.edu/i256/f09/Final%20Projects%20write-ups/Suzuki_Park_project_final.pdf

### Web App
A web app using flask will be developed and run on AWS.


### Visualization

  ![Word clouds](images/Figure_1.png)

  <br />


### Schedule

11/14-11/17
Read relevant articles about best approaches
Test different NLP techniques and develop a pipeline to test on new data. Potentially switch from removing stopwords to generating a list of accepted ingredients   
11/18-11/19
Develop an MVP and begin to test other models and potentially look into more sophisticated methods(adding stars rating system).
11/20-11/24
Select best model and optimize parameters.
Develop Web App MVP.
11/25-11/28
Make the Web App look pretty.
Continue to scrape data and make the database more robust.
Make web app user friendly and easy on the eyes
Develop a good README

### Future Goals
