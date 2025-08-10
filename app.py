from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
import numpy as np

# --- CORRECTED IMPORT ---
# We import the required class directly from keras_nlp
from keras_nlp.models import DistilBertClassifier


app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# --- CORRECTED MODEL LOADING ---
# The key 'DistilBertTextClassifier' must match the name from the error message.
# The value 'DistilBertClassifier' is the actual class we just imported.
model = tf.keras.models.load_model(
    'feedback_analysis_model.keras',
    custom_objects={'DistilBertTextClassifier': DistilBertClassifier}
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        review_text = data['review']
        
        # The model expects a list of raw text strings.
        prediction = model.predict([review_text])
        
        predicted_id = np.argmax(prediction, axis=1)[0]
        predicted_rating = int(predicted_id) + 1 
        
        return jsonify({'sentiment': f'{predicted_rating} Star(s)'})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to process the review on the server.'}), 500


if __name__ == '__main__':
    app.run(debug=True)