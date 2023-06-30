import backoff
import json

class Horno:

    def __init__(self) -> None:
        pass

    def cocer(self, alimento: str)-> str:
        return f"{alimento} cocinado"
    ...


import hashlib as hash_obj

class Recetario:

    def __init__(self) -> None:
        pass

    def crear_plato_1(self, arroz_cocido: str, agua: str):

        print(f"[DEBUG]Creando plato 1 con Arroz cocido: {arroz_cocido} y agua: {agua}")
        plato_hash = hash_obj.sha256(bytes(f"Plato 1 con {arroz_cocido} y {agua}", 'utf-8'))
        print("[DEBUG]Plato creado")

        return plato_hash.hexdigest()
        ...

    def crear_plato_2(self, arroz_cocido: str, yuca_cocida: str, papa_cocida: str, agua: str):
        
        print(f"[DEBUG]Creando plato 2 con Arroz cocido: {arroz_cocido}, Yuca cocida: {yuca_cocida}, Papa cocida: {papa_cocida} y agua: {agua}")
        plato_hash = hash_obj.sha256(bytes(f"Plato 2 con Arroz cocido: {arroz_cocido}, Yuca cocida: {yuca_cocida}, Papa cocida: {papa_cocida} y agua: {agua}", 'utf-8'))
        print("[DEBUG]Plato creado")

        return plato_hash.hexdigest()
        ...
    ...


class Chef:
    """ Clase de ejemplo de Chef"""

    nombre: str
    horno: Horno
    recetario: Recetario

    def __init__(self, horno: Horno, recetario: Recetario) -> None:
        self.horno= horno
        self.recetario= recetario
        pass


    def preparar_receta_1(self, arroz: str, papa: str, yuca: str) -> str:

        print("[DEBUG]Inicia preparacion plato 1")

        alimentos_dic= self.preparar_alimentos(arroz, papa, yuca)

        plato_1= self.recetario.crear_plato_1(alimentos_dic["arroz"], "Agua manantial")

        print("[DEBUG]Termina preparacion plato 1")

        return plato_1

        ...

    def backoff_hdlr(details):
        print (details["args"])

    @backoff.on_exception(backoff.expo,
                      RuntimeError,
                      on_success=backoff_hdlr)
    def preparar_alimentos(self, arroz: str, papa: str, yuca: str) -> dict:

        print(f"[DEBUG]Hola, he recibido Arroz[{arroz}], Papa[{papa}], Yuca[{yuca}]")

        alimentos_cocinados=[]
        alimentos_dic={}

        print("[DEBUG]Inicia la coccion de los alimentos")

        if arroz != None:
            arroz_h=self.horno.cocer(arroz)
            print(f"[DEBUG]{arroz_h}")
            alimentos_cocinados.append(arroz_h)
            alimentos_dic["arroz"]=arroz_h

        if  papa != None:
            papa_h=self.horno.cocer(papa)
            print(f"[DEBUG]{papa_h}")
            alimentos_cocinados.append(papa_h)
            alimentos_dic["papa"]=papa_h

        if  yuca != None:
            yuca_h=self.horno.cocer(yuca)
            print(f"[DEBUG]{yuca_h}")
            alimentos_cocinados.append(yuca_h)
            alimentos_dic["yuca"]=yuca_h

        print("[DEBUG]Cierra la cocina")

        return alimentos_dic
        ...

    ...

def handler():
    print("Inicio de la prueba")
    
    horno= Horno()
    recetario= Recetario()
    rosemberg_chef= Chef(horno, recetario)

    alimentos_cocidos=rosemberg_chef.preparar_alimentos(arroz="Arroz Gelvez", papa="Papa Pastusa", yuca="Yuca campesina")

    print(f"Los alimentos cocidos son: {alimentos_cocidos}")

    plato_preparado= rosemberg_chef.preparar_receta_1(arroz="Arroz Gelvez", papa="Papa Pastusa", yuca="Yuca campesina")

    print(f"El plato preparado es: {plato_preparado}")

    ...


"""This make executable this file, just ignore it"""

import sys

if __name__ == '__main__':
    globals()[sys.argv[1]]()