from flask import Flask, render_template, request, jsonify
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_weather', methods=['POST'])
def check_weather():
    data = request.get_json()
    city = data.get('city', '')
    
    # Simulating a delay
    time.sleep(3)
    
    return jsonify({"message": "Bahar Dekh Lawde"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)

