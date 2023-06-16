from TextSummarizer.logging import logger
from TextSummarizer.pipelines.stege_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'DATA_INGESTION_STAGE'

try:
    logger.info(f'>>>>>> stage %s started <<<<<<<' % STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage %s completed <<<<<<<' % STAGE_NAME)

except Exception as e:
    logger.exception(e)
    raise e



