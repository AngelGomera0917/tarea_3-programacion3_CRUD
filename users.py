
# Clase de Programacion 3, los Martes de 20:00 PM a 22:00 PM

# Mi nombre es: Angel Antonio Gomera Romero
# Matricula: 2022-0493

# Este es un proyecto creado con FasatAPI, CRUD de usuarios con get, post, put y delete 

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    educacion: str
    
databese_users = [User(id=1, name="Dayelin", surname="Ramirez", age= 26, educacion="Ingenieria Civil"),
                User(id=2, name="Juan", surname="Perez", age=29, educacion="Ingenieria en Sistemas"),
                User(id=3, name="Maria", surname="Lopez", age=37, educacion="Contabilidad")
                ]