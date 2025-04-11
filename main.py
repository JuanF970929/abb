from http.client import HTTPException

from fastapi import FastAPI
from controller import abb_controller
from controller.abb_controller import abb_route, abb_service

app = FastAPI()

app.include_router(abb_controller.abb_route)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@abb_route.get("/{id}")
async def get_pet_by_id(id: int):
    try:
        return abb_service.abb.find_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@abb_route.get("/report/location_gender")
async def report_by_location_and_gender():
    return abb_service.abb.report_by_location_and_gender()