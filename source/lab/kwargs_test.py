import pydantic
import pydash

class Test(pydantic.BaseModel):
    nombre: str
    apellido: str
    edad: int


def create_test(**kwargs):
    return Test(**kwargs)


print( create_test(nombre="Pepe", apellido="Manrique", edad=23))