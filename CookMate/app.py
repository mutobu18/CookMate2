from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Temporary mock user database (for demonstration purposes)
users_db = {"test@example.com": "password123"}

@app.route("/")
def home():
    return render_template("login.html")
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the user exists and the password is correct
    if username in users_db and users_db[username] == password:
        return redirect(url_for('recipes'))  # Redirect to the recipes page if successful
    else:
        return render_template('login.html', error="Invalid credentials, please try again.")

@app.route('/recipes')
def recipes():
    return render_template('Recipes.html') # Render the recipes page

@app.route('/mealplan')
def mealplan():
    return render_template('MealPlan.html')  # Render the Meal Page template

@app.route('/about')
def about():
    return render_template('About.html')  # Render the Meal Page template


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Simple validation for matching passwords
        if password == confirm_password:
            # Save to database or mock database
            users_db[email] = password
            return redirect(url_for('home'))  # Redirect to login page after account creation
        else:
            return render_template('create_account.html', error="Passwords do not match.")
    return render_template('create_account.html')


if __name__ == '__main__':
    app.run(debug=True)

