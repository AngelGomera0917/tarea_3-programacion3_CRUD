
# Clase de Programacion 3, los Martes de 20:00 PM a 22:00 PM

# Mi nombre es: Angel Antonio Gomera Romero
# Matricula: 2022-0493

# Este es un proyecto creado con FasatAPI, CRUD de usuarios con get, post, put y delete 

from fastapi import  FastAPI, HTTPException

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

# Get
# =================== # ruta principal con get que devuelve todos los usuarios # =================== #
@app.get("/")
async def get_users():
    return databese_users

# ======================= # path que se usa para buscar un usuario por su id # ===================== #
@app.get("/user_path/{user_id}")
async def get_user(user_id: int):
    for user in databese_users:
        if user.id == user_id:
            return {"Usuario encontrado con exito ✅": user}
    return {"error ❌": "User not found"}


        # ======================= # Post para agregar un nuevo usuario # ======================= #
@app.post("/user_post/", status_code=201)
async def post_user(user: User):
    
    for existing_user in databese_users:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail = {"error ❌": "User with this ID already exists"})
        
        if user.age <= 0:
            raise HTTPException(status_code=404, detail = {"error ❌": "Age cannot be less than or equal to zero"})
        
        if not user.name or not user.surname or not user.educacion:
            raise HTTPException(status_code=400, detail = {"error ❌": "Name, surname and education cannot be empty"})
        
    databese_users.append(user)
    return {"Nuevo usuario agregado con exito ✅": user} 


# ======================= # Put para actualizar un usuario por su id # ======================= #
@app.put("/user_put/")
async def put_user(user: User):
    
    for index, existing_user in enumerate(databese_users):
        if existing_user.id == user.id:
            databese_users[index] = user
            return {"Usuario actualizado con exito ✅": user}
    
    raise HTTPException(status_code=404, detail = {"error ❌": "User not found"}) 

