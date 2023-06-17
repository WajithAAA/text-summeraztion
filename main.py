from TextSummarizer.logging import logger
from TextSummarizer.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipelines.stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = 'DATA_INGESTION_STAGE'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<<' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'DATA_VALIDATION_STAGE'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_Validation = DataValidationTrainingPipeline()
    data_Validation.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<<' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e

