import os
import pandas as pd
from src.datascience import logger
from src.datascience.entity.config_entity import (DataValidationConfig)


## component - Data Validation
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)

            all_schema = self.config.all_schema.keys()


            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else: 
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        
        except:
            validation_status = True



    def validate_column_dtypes(self):
        try:
            validation_status = {}

            # Load data
            data = pd.read_csv(self.config.unzip_data_dir)

            # Iterate over all schema types
            for column, expected_dtype in self.config.all_schema.items():
                actual_dtype = data[column].dtype

                if actual_dtype != expected_dtype:
                    validation_status[column] = {
                        "status": False,
                        "message": f"Expected dtype {expected_dtype}, but got {actual_dtype}"
                    }
                else:
                    validation_status[column] = {
                        "status": True,
                        "message": f"Types match ({actual_dtype})"
                    }
        
            # Check overall status
            all_valid = all(status["status"] for status in validation_status.values())
            
            with open(self.config.STATUS_FILE, 'a') as f:
                if all_valid:
                    f.write(f"\nValidation status is: True")
                else:
                    f.write("Some columns have invalid types. Check details below:\n")
                    for column, status in validation_status.items():
                        f.write(f"{column}: {status['message']}\n")
            
            return validation_status
        
        except Exception as e:
            # Log the exception to the file for better traceability
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation failed with error: {str(e)}\n")
            # Optionally, raise the exception or handle it as needed
            return {"error": str(e)}
