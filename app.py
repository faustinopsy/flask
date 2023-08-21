import os
from flask import Flask, request, render_template,jsonify
import joblib

model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    if text=="":
        return jsonify(sentiment="Neutro")
    else:
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)
        
        sentiment = "Positivo" if prediction[0] == "pos" else "Negativo" if prediction[0] == "neg" else "Neutro"

        return jsonify(sentiment=sentiment)

if __name__ == '__main__':
     #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
