from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "Hello, World!"

# Define a route that accepts GET and POST methods
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('greet_form.html')

if __name__ == '__main__':
    app.run(debug=True)
