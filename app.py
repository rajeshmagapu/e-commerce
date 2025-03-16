from flask import Flask, render_template, request, jsonify
from database import get_products, create_order
from email_service import send_email

app = Flask(__name__)

@app.route('/')
def home():
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        data = request.json
        order_id = create_order(data['cart'])
        send_email(data['email'], order_id, data['cart'])
        return jsonify({"order_id": order_id, "message": "Order placed successfully!"})
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True)
