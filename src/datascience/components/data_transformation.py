import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig

## component - Data Transformation
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: you can add different data transfomration techniques such as SCaler
    # PCA and all.
    # Per form all kinds of EDA in ML cycle here before passing this data to model
    # only train_test_split is added here cause the data is already clean    

    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        # split the data into train and test 
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)