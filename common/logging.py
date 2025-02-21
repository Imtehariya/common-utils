import logging
import watchtower
import boto3
from logging.handlers import RotatingFileHandler

# AWS CloudWatch Config
AWS_LOG_GROUP = "your-log-group-name"
AWS_REGION = "your-region"

def get_logger(name: str):
    """
    Get a configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s"))

    # File Handler (local logs)
    file_handler = RotatingFileHandler("app.log", maxBytes=5*1024*1024, backupCount=5)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # AWS CloudWatch Handler
    # session = boto3.Session()
    # cloudwatch_handler = watchtower.CloudWatchLogHandler(
    #     log_group=AWS_LOG_GROUP,
    #     stream_name=name,
    #     boto3_session=session,
    #     region_name=AWS_REGION,
    # )

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    # logger.addHandler(cloudwatch_handler)

    return logger
