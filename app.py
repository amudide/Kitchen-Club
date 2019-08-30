from flask import Flask, render_template, request, jsonify

import requests
import csv

app = Flask(__name__)

posts = []

@app.route('/', methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        caption = request.form.get('caption')
        recipe = request.form.get('recipe')
        pic = request.form.get('pic')

        afile = open("posts.csv", "a")
        writer = csv.writer(afile)
        writer.writerow((caption, pic, recipe))
        afile.close()

    rfile = open("posts.csv", "r")
    reader = csv.reader(rfile)
    posts = list(reader)
    rfile.close()

    return render_template("home.html", posts = posts, num = len(posts) - 1)

@app.route('/search')
def search():
    q = request.args.get('q')

    rfile = open("posts.csv", "r")
    reader = csv.reader(rfile)
    posts = list(reader)
    rfile.close()

    match_posts = []
    num = len(posts) - 1
    for i in range(0, num, 2):
        if (posts[i][2].upper()).startswith(str(q).upper()):
            match_posts.append([posts[i][0], posts[i][1], posts[i][2]])

    print(jsonify(match_posts))
    return jsonify(match_posts)

@app.route('/getIngredient')
def getIngredient():
    return render_template("index.html")

@app.route('/makePost')
def makePost():
    return render_template("makepost.html")

@app.route('/recipes', methods = ["POST"])
def recipes():
    ingredient = request.form.get("ingredient")
    recipes = int(request.form.get("recipes"))
    api_key = "b835ff1f349d4dbb8b5e138e9a99b25b"

    parameters = {'query' : ingredient, 'number' : recipes, 'apiKey' : api_key}
    r = requests.get('https://api.spoonacular.com/recipes/search', params = parameters)
    recipe_names = []
    recipe_links = []
    data = r.json()
    for i in range(recipes):
        recipe_names.append(data['results'][i]['title'])
        id = str(data['results'][i]['id'])
        link = 'https://spoonacular.com/recipeImages/' + id + '-240x150.jpg'
        recipe_links.append(link)

    return render_template("recipes.html", ingredient = ingredient, recipes = recipes, recipe_names = recipe_names, recipe_links = recipe_links)




















#
