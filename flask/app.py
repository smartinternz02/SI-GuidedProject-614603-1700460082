import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the dataset
restaurant_data = pd.read_csv("restaurant1.csv")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommendation', methods=['POST'])
def recommendation():
    # Get user input from the form
    user_preference = request.form.get('preference')

    # Recommendation logic (Replace this with your actual recommendation logic)
    recommended_restaurants = recommend_restaurants(user_preference)

    return render_template('recommendation.html', user_preference=user_preference, recommendations=recommended_restaurants)

def recommend_restaurants(user_preference):
    # Replace this with your actual recommendation logic
    # For now, it just returns a random restaurant
    recommended_restaurants = restaurant_data.sample(5)
    return recommended_restaurants

if __name__ == '__main__':
    app.run(debug=True)
