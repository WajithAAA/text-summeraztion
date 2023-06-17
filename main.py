from TextSummarizer.logging import logger
from TextSummarizer.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipelines.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipelines.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipelines.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = 'DATA_INGESTION_STAGE'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'DATA_VALIDATION_STAGE'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_Validation = DataValidationTrainingPipeline()
    data_Validation.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'DATA_TRANSFORMATION_STAGE'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_Validation = DataTransformationTrainingPipeline()
    data_Validation.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'MODEL_TRAINER_STAGE'

try:
    logger.info(f'****************')
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_Validation = ModelTrainerTrainingPipeline()
    data_Validation.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME )

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'MODEL_EVALUATION_STAGE'

try:
    logger.info(f'****************')
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_Validation = ModelEvaluationTrainingPipeline()
    data_Validation.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<< \n\nx==========x' % STAGE_NAME )

except Exception as e:
    logger.exception(e)
    raise e