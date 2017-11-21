from flask import Flask, request, render_template
import pickle as pickle
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('css_template.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
