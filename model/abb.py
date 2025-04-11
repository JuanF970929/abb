import status
from starlette import status

from model.pet import Pet

class ABB():
    def __init__(self):
        self.root = None

    def add(self, pet:Pet):
        if self.root == None:
            self.root = NodeABB(pet)
        else:
            self.root.add(pet)

    def update(self, pet:Pet, id: int):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            self.root.update(pet, id)

    def inorder(self):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.inorder()


class NodeABB:
    def __init__(self, pet:Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    def add(self, pet:Pet):
        if pet.id == self.pet.id:
            raise Exception("La mascota ya existe")
        if pet.id < self.pet.id:
            if self.left != None:
                self.left.add(pet)
            else:
                self.left = NodeABB(pet)
        elif self.right != None:
            self.right.add(pet)
        else:
            self.right = NodeABB(pet)
        self.size +=1

    def delete(self, id: int):
        if id < self.pet.id:
            if self.left is None:
                raise Exception("ID no encontrado")
            self.left = self.left.delete(id)
        elif id > self.pet.id:
            if self.right is None:
                raise Exception("ID no encontrado")
            self.right = self.right.delete(id)
        else:

            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_larger_node = self.right.get_min_node()
            self.pet = min_larger_node.pet
            self.right = self.right.delete(min_larger_node.pet.id)

        self.size -= 1
        return self

    def update(self, pet: Pet, id: int):
        if self.pet.id == id:
            self.pet.name = pet.name
            self.pet.age = pet.age
            self.pet.breed = pet.breed
        elif id < self.pet.id:
            if self.left is not None:
                self.left.update(pet, id)
            else:
                raise Exception("Id no encontrado")
        elif id > self.pet.id:
            if self.right is not None:
                self.right.update(pet, id)
            else:
                raise Exception("Id no encontrado")
        else:
            raise Exception("Id no encontrado")
    def validate_pet(pet: Pet):
        if not pet.name or not pet.breed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Nombre y raza son obligatorios"
            )
        if pet.age < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La edad no puede ser negativa"
            )

    def inorder(self):
        listPets = []
        if self.left != None:
            listPets.append(self.left.inorder())
        listPets.append(self.pet)
        if self.right != None:
            listPets.append(self.right.inorder())
        return listPets


class NodeAVL(NodeABB):
    def __init__(self, pet:Pet):
        super().__init__(pet)
        self.height = 1
        self.balance = 1


    def validate_pet(pet: Pet):
        if not pet.name or not pet.breed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Nombre y raza son obligatorios"
            )
        if pet.age < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La edad no puede ser negativa"
            )
