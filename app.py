from flask import Flask, render_template
from market_trends_tracker.database import get_all_products

app = Flask(__name__)

@app.route('/')
def index():
    products = get_all_products()  # Get all products from the database
    print("Products from database: ", products)  # Debugging: Check the retrieved products
    return render_template('index.html', products=products)

if __name__ == "__main__":
    app.run(debug=True)
