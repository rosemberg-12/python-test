from typing import Callable

def function_handler(var1: str, on_success: Callable):
    print("[function_handler]Funcion Handler")
    on_success()
    ...

def _publish_payment_fraud_assessment_completed_event():
    print("[printy]Funcion que se envia.")
    ...

print("Inicio")

function_handler(var1="test", on_success=_publish_payment_fraud_assessment_completed_event)

print("Final")
