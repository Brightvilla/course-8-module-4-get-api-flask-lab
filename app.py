from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200


@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        normalized_category = category.lower()
        filtered_products = [
            product
            for product in products
            if product.get("category", "").lower() == normalized_category
        ]
        return jsonify(filtered_products), 200

    return jsonify(products), 200


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return jsonify(
            {
                "error": "Product not found",
                "details": f"No product found with id {product_id}",
            }
        ), 404

    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)
