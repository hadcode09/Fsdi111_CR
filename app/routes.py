#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Route definitions"""

from app import app
from datetime import datetime

@app.route("/version")
def version():
    return {
        "ok" : True,
        "message": "success",
        "version": "1.0.0",
        "server time": datetime.now().strftime("%F %H:%M:%S")
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def get_products():
    """Retrieve all products"""
    return "Return all products"

@app.route("/products/<int:pid>")
def get_product_detail(pid):
    """Retrieve a single product"""
    return "Single product detail"

@app.route("/products/<int:pid>", methods=["PUT"])
def update_product(pid):
    """Update a single product"""
    return "Single product update"

@app.route("/products", methods=["POST"])
def create_product():
    """Create a new product"""
    return "Create new product"

@app.route("/products/<int:pid>", methods=["DELETE"])
def delete_product(pid):
    """Soft delete a single product"""
    return "Soft delete a product"