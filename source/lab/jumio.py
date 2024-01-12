
import kyc_logger as log
import time

_LOGGER= log.get_lambda_logger()

def start_jumio():
    _LOGGER.info("STAGE(IDENTITY_PROOFING): Starting Jumio")
    time.sleep(3)
    _LOGGER.info("STAGE(IDENTITY_PROOFING): Jumio Finished")
