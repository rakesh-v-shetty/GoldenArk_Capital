from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = 'your_super_secret_key_that_you_must_change_for_production'


@app.route('/')
def home():
    """Renders the home page."""
    return render_template('home.html')

@app.route('/products')
def products():
    """Renders the products page."""
    return render_template('products.html')

@app.route('/performance')
def performance():
    """Renders the performance page."""
    return render_template('performance.html')

@app.route('/whyus')
def whyus():
    """Renders the whyus page."""
    return render_template('whyus.html')

@app.route('/security')
def security():
    """Renders the security page."""
    return render_template('security.html')

@app.route('/strategy')
def strategy():
    """Renders the strategy page."""
    return render_template('strategy.html')

@app.route('/market')
def market():
    """Renders the market page."""
    return render_template('market.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)