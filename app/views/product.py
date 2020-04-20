from flask import Blueprint, render_template, request, redirect, url_for, flash ,session

from ..extension import db
from ..models import User, Product


product_page = Blueprint('product_page', __name__)


@product_page.route('/products/list')
def product_list():
    userName = session['userName']
    user = User.query.filter_by(username=userName).first()
    if user.role in [0, 1]:
        products = Product.query.all()
    elif user.role == 2:
        products = Product.query.filter_by(status=1)
    else:
        products = Product.query.filter_by(status=2)
    return render_template('products/product-list.html', products=products, username=userName, user_role=user.role)


@product_page.route('/products/add', methods=['GET', 'POST'])
def product_add():
    userName = session['userName']
    if request.method == 'GET':
        return render_template('products/product-add.html',username=userName)
    else:
        name = request.form.get('name')
        number = request.form.get('number')
        dest = request.form.get('dest')
        desc = request.form.get('desc')
        if name and number and dest:
            product = Product(name, int(number), dest, 1, desc)
            db.session.add(product)
            db.session.commit()
            return '1'
        else:
            return '0'


@product_page.route('/products/delete/<int:product_id>')
def product_delete(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product_page.product_list'))


@product_page.route('/products/modify/<int:product_id>', methods=['GET', 'POST'])
def product_modify(product_id):
    userName = session['userName']
    user = User.query.filter_by(username=userName).first()
    product = Product.query.get(product_id)
    if request.method == 'GET':
        if user.role in [0, 1]:
            return render_template('products/product-modify.html', product=product,username=userName)
        else:
            product.status += 1
            db.session.commit()
            return redirect(url_for('product_page.product_list'))
    else:
        name = request.form.get('name')
        number = request.form.get('number')
        dest = request.form.get('dest')
        status = request.form.get('status')
        desc = request.form.get('desc')
        if name and number and dest:
            product.name, product.number, product.dest, product.status, product.desc = name, int(number), dest, int(status), desc
            db.session.commit()
            return '1'
        else:
            return '0'
