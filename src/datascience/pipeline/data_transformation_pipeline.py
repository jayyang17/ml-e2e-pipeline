from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path
STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                # call the configuration manager
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()

                # call the data transformation class
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid.")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        data_tranformation = DataTransformationTrainingPipeline()
        data_tranformation.initiate_data_transformation()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e