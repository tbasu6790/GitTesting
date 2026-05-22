products = []

def get_products()
    return products

def add_product(name, price):
    products.append({"name": name, "price": price})
    return {"added": True}
