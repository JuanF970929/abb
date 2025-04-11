from pydantic import BaseModel

class Pet(BaseModel):
    id:int
    name:str
    age: int
    breed:str
    location: str
    gender: str