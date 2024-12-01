from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger

STAGE_NAME="Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        # call the configuration manager
        config = ConfigurationManager()
        model_trainer_config = config.get_data_model_trainer_config()

        # call the data transformation class
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()



if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        model_trainer = ModelTrainerPipeline()
        model_trainer.initiate_model_trainer()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
