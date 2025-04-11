from model.pet import Pet
from service import abb_service
from fastapi import APIRouter, Response, status, HTTPException

abb_service = abb_service.ABBService()

abb_route = APIRouter(prefix="/abb")

@abb_route.get("/")
async def get_pets():
    return abb_service.abb.root

@abb_route.get("/inorder")
async def get_pets_inorder():
    try:
        return abb_service.abb.inorder()
    except Exception as e:
        return {"message": e.args[0]}

@abb_route.post("/", status_code=200)
async def create_pet(pet: Pet, response: Response):
    try:
        validate_pet(pet)
        abb_service.abb.add(pet)
        return {"message": "Adicionado exitosamente"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.args[0]}

@abb_route.put("/{id}")
async def update_pet(id: int, pet: Pet, response: Response):
    try:
        validate_pet(pet)
        abb_service.abb.update(pet, id)
        return {"message": "Actualizado exitosamente"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.args[0]}

@abb_route.delete("/{id}")
async def delete_pet(id: int, pet:Pet, response: Response):
    try:
        abb_service.abb.delete(id)
        return {"message": "Eliminado exitosamente"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.args[0]}

@abb_route.get("/count_by_breed")
async def count_by_breed():
    try:
        return abb_service.abb.count_by_breed()
    except Exception as e:
        return {"message": e.args[0]}

def validate_pet(pet: Pet):
    if not pet.name or not pet.breed:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre y raza son obligatorios")
    if pet.age < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La edad no puede ser negativa")
