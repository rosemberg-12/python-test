from pydantic import BaseModel


class Persona(BaseModel):
    nombre: str
    edad: int
    email: str
    direccion: str
        
persona = Persona(nombre="Juan", edad=30, email="juan@example.com", direccion="Calle 123")
print(persona.json(exclude={"edad"}))
