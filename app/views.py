import os
import pandas as pd 
from app import app
from flask import render_template,request,redirect, url_for,json


def list_to_html(l):
    str_repr = "<ul>"
    for element in l:
        str_repr += f"<li>{element}<li/>"
    str_repr += "<ul>"
    return "<ul>"+"".join([])+"<ul/>"

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/extract', methods=['post'])
def extract_data():
    product_id = request.form.get('product_id')
    return redirect(url_for('product', product_id=product_id))

@app.route('/extract', methods=['get'])
def display_form():
    return render_template("extract.html")

@app.route('/products')
def products(): 
    products = []
    for file in os.listdir("./app/data/products"):
        if file.endswith(".json"):
            with open(os.path.join("./app/data/products", file), "r", encoding="utf-8") as f:
                data = json.load(f)
                products.append(data)
    return render_template("products.html",products = products)

@app.route('/author')
def author(): 
    return render_template("author.html")

@app.route('/product/<int:product_id>')
def product(product_id:int): 
    with open(f"./app/data/opinions/{product_id}.json", "r", encoding="UTF-8") as jf:
        try:
            opinions = json.load(jf)
        except json.JSONDecodeError:
            error = "Dla produktu o podanym ID nie pobrano jeszcze opinii."
            return render_template("product.html", error=error)
    opinions = pd.DataFrame.from_dict(opinions)
    opinions.pros = opinions.pros.apply(list_to_html)
    opinions.cons = opinions.pros.apply(list_to_html)

    
    return render_template("product.html", opinions=opinions.to_html(classes="table table-hover table-bordered"))

