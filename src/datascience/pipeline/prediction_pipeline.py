import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        # Ensure the model has attribute for feature names (if it does)
        self.feature_names = self.model.feature_names_in_ if hasattr(self.model, 'feature_names_in_') else None

    def predict(self, data):
        # Ensure `self.feature_names` is available
        if self.feature_names is None:
            raise ValueError("Model does not have feature names. Unable to validate input data.")

        # Convert NumPy array to DataFrame if needed
        if isinstance(data, np.ndarray):
            if data.shape[1] != len(self.feature_names):
                raise ValueError(f"Expected {len(self.feature_names)} features, got {data.shape[1]}")
            data = pd.DataFrame(data, columns=self.feature_names)
        
        # Validate columns for pandas DataFrame
        elif isinstance(data, pd.DataFrame):
            if data.columns.tolist() != self.feature_names:
                raise ValueError("Input data columns do not match model's training feature columns.")
        
        else:
            raise TypeError("Input data must be a pandas DataFrame or a NumPy array.")
        
        # Predict using the model
        prediction = self.model.predict(data)
        return prediction
