from app import app
from flask import render_template
from models.shop_list import item_list

@app.route('/')
def index():
    return "Hello here be shop of things"

@app.route('/order')
def inventory():
    return render_template('index.html',order_list=item_list)

@app.route('/order/<index>')
def order(index):
    order=item_list[int(index)]

    return render_template('index_1.html',order=order)