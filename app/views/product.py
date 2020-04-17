from flask import Blueprint, render_template, request, redirect, url_for, flash

from ..extension import db
from ..models import Product


product_page = Blueprint('product_page', __name__)


@product_page.route('/products/list')
def product_list():
    products = Product.query.all()
    return render_template('products/list.html', products=products)


@product_page.route('/products/add', methods=['GET', 'POST'])
def product_add():
    if request.method == 'GET':
        return render_template('products/addproduct.html')
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
    product = Product.query.filter_by(id=product_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product_page.product_list'))


@product_page.route('/products/modify/<int:product_id>', methods=['GET', 'POST'])
def product_modify(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if request.method == 'GET':
        return render_template('products/modifyproduct.html', product=product)
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
