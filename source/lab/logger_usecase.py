import typing
import time
import kyc_logger as log
import jumio
import log_decorator
import uuid

_LOGGER= log.get_lambda_logger(reset_tx_id=True)
print( "Logger creado")
class KYC:

    @log_decorator.transactional_log(route="GET /kyc")
    def execute_kyc(self, document_type: str, document_number: str, stages: typing.List[str])-> None:
        #_LOGGER.info("Starting Execute KYC for [%s][%s] \nStages:[%s]", document_type, document_number, stages)
        jumio.start_jumio()
        #_LOGGER.info("Ending Execute KYC for [%s][%s]", document_type, document_number)

    @log_decorator.transactional_log(route="POST /kyc")
    def get_kyc(self, document_type: str, document_number: str)-> None:
        #_LOGGER.info("Starting GET KYC for [%s][%s]", document_type, document_number)
        time.sleep(5)        
        #_LOGGER.info("Ending GET KYC for [%s][%s]", document_type, document_number)


kyc_component= KYC()

kyc_component.get_kyc(document_type= "Cedula", document_number= "1098764098")

kyc_component.execute_kyc(document_type= "Cedula", document_number= "1098764098", stages=["IDENTITY_PROOFING", "BOLD_LIST"])