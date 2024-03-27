from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"Starting stage {STAGE_NAME}")
    data_ingestion =DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Stage {STAGE_NAME} completed successfully")
except Exception as e:
    logger.error(f"Failed to complete the stage {STAGE_NAME}")
    logger.error(e)
    raise e    