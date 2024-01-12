import logging
import os
import sys
from typing import Optional
import uuid

_FORMAT = (
    "%(asctime)s | %(levelname)-7s | %(module)s.%(funcName)s:%(lineno)d | KYC [%(kyc_tx)s] : %(message)s"
)
kyc_logger: Optional[logging.Logger] = None

class ContextFilter(logging.Filter):
    """
    This is a filter that injects contextual information into the log.
    """
    
    def __init__(self, kyc_uuid: uuid.UUID):
        self.kyc_tx = kyc_uuid

    def filter(self, record):
        record.kyc_tx = self.kyc_tx
        return True

def get_lambda_logger(reset_tx_id: bool= False) -> logging.Logger:
    global kyc_logger

    print(f"value of {kyc_logger} and {reset_tx_id}")

    if kyc_logger is None:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(logging.Formatter(_FORMAT))
        kyc_logger = logging.getLogger(
            os.environ.get("AWS_LAMBDA_FUNCTION_NAME", "NoLambdaEnvironment")
        )
        kyc_logger.propagate = False
        kyc_logger.setLevel(logging.INFO)
        stdout_handler.setLevel(logging.INFO)
        kyc_logger.addFilter(ContextFilter(kyc_uuid=uuid.uuid4()))
        kyc_logger.addHandler(stdout_handler)

    if reset_tx_id:
        kyc_logger.filters=[]
        kyc_logger.addFilter(ContextFilter(kyc_uuid=uuid.uuid4()))

    return kyc_logger
    

