import backoff
import json

#Cambia el valor
def backoff_hdlr(details):
    print (f'[backoff_hdlr]A backoff llega el valor: {details["args"][0]["estado"]}')
    elementos= details["args"][0];
    elementos["estado"]=False
    print (f'[backoff_hdlr]De backoff sale el valor: {elementos["estado"]}')


#Imprime el valor original
@backoff.on_exception(backoff.expo, RuntimeError, on_backoff=backoff_hdlr)
def func_a(elementos: dict):
    print(f"[func_a]El estado que se recibe es: {elementos['estado']}")
    if elementos['estado'] == True :
        raise RuntimeError
    else:
        print(f"[func_a]El estado final es: {elementos['estado']}")
    ...

#Inicio de la prueba

elementos={
         "estado": True #Se declara diccionario con valor en True
        }

print(f"[MAIN]El estado inicial es: {elementos['estado']}")
func_a(elementos)
print(f"[MAIN]El estado final es: {elementos['estado']}")