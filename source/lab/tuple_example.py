
from typing import Tuple

class Animal():
    ...

def get_tuple()-> Tuple[str, str, bool, Animal]:
    return ("Saludo", "Despedida", "False", Animal())

print (get_tuple())

return_value= get_tuple()

print(return_value)

(uno, dos, tres, cuatro)= get_tuple()

print(uno)