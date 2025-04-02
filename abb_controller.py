from model.pet import Pet
from service import abb_service
from fastapi import APIRouter

abb_service = abb_service.ABBService()

abb_route = APIRouter(prefix="/abb")

@abb_route.get("/")
async def get_pets():
    return abb_service.abb.root

@abb_route.post("/")
async def create_pet(pet:Pet):
    abb_service.abb.add(pet)
    return "Adicionado"