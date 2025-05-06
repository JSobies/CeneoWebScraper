import os
from app import app
from flask import render_template,request,redirect, url_for,json

@app.route('/')
def index(): 
    return render_template("base.html")

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    product_id = request.form.get('product_id')
    if request.method == 'POST':
        url = request.form['product_url']
        num = request.form.get('num_opinions', 50)
        rating = request.form.get('rating_filter', '')

        
        print(f"URL: {url}, Opinie: {num}, Ocena: {rating}")
        return redirect(url_for('product', product_id=product_id))

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
def product(product_id): 
    return render_template("product.html", product_id=product_id)

