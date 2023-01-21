from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    fName= "Jerri Pat"
    fav_pizza= ['peperoni', 'cheese', 'mushrooms', 'chilie']
    return render_template('index.html',
            f_name=fName, favPizza=fav_pizza)

@app.route("/about")
def about():
    return render_template('about.html')