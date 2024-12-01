from flask import Flask, render_template, request
import os
import numpy as np
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline
from src.datascience import logger

app = Flask(__name__)

@app.route('/', methods=['GET'])  # route to display the homepage
def homepage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")  # to execute this command
    return "Training Successful"

@app.route('/predict', methods=['POST', 'GET'])  # route from the web UI
def index():
    if request.method == 'POST':
        try:
            # Extract input data from the form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # Combine the input data into a NumPy array
            data = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                             chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH,
                             sulphates, alcohol]).reshape(1, -1)

            # Log input data for debugging
            logger.debug(f"Input data: {data}")

            # Create prediction pipeline object and predict
            obj = PredictionPipeline()
            predict = obj.predict(data)

            # Log details of the prediction
            logger.debug(f"Raw prediction output: {predict} (type: {type(predict)})")

            # Handle different prediction types
            if isinstance(predict, np.ndarray):
                logger.debug(f"Prediction array shape: {predict.shape}")
                if predict.size == 1:
                    prediction_value = float(predict[0])  # Single value
                elif predict.ndim == 1:
                    prediction_value = predict.tolist()  # Flattened list
                else:
                    prediction_value = predict.tolist()  # General list
            else:
                prediction_value = float(predict) if isinstance(predict, (int, float)) else predict

            # Log the prediction value
            logger.debug(f"Final prediction value: {prediction_value}")

            # Render the result page with the prediction
            return render_template('results.html', prediction=str(prediction_value))

        except Exception as e:
            # Log the full traceback for better debugging
            logger.error(f"Error: {e}", exc_info=True)
            return "Something went wrong"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

