import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('query') or 'world'
    category = request.form.get('category') or 'general'

    url = f"https://newsapi.org/v2/top-headlines?category={category}&q={query}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])

    return render_template('index.html', articles=articles, query=query, category=category)


if __name__ == '__main__':
    app.run(debug=True)
