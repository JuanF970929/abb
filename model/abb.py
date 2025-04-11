import status
from fastapi import HTTPException
from starlette import status

from model.pet import Pet


class ABB():
    def __init__(self):
        self.root = None

    def add(self, pet: Pet):
        if self.root == None:
            self.root = NodeABB(pet)
        else:
            self.root.add(pet)

    def update(self, pet: Pet, id: int):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            self.root.update(pet, id)

    def delete(self, id: int):
        if self.root is None:
            raise Exception("No existen mascotas en el árbol")
        self.root = self.root.delete(id)

    def inorder(self):
        if self.root == None:
            raise Exception("No existen mascotas en el listado")
        else:
            return self.root.inorder()

    def find_by_id(self, id: int):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.find_by_id(id)

    def preorder(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.preorder()

    def postorder(self):
        if self.root is None:
            raise Exception("No existen mascotas en el listado")
        return self.root.postorder()

    def count_by_breed(self):
        if self.root is None:
            return {}
        return self.root.count_by_breed()

    def report_by_location_and_gender(self):
        if self.root is None:
            return {}
        return self.root.report_by_location_and_gender()


class NodeABB:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    def add(self, pet: Pet):
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
        self.size += 1

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

    def delete(self, id: int):
        if id < self.pet.id:
            if self.left is not None:
                self.left = self.left.delete(id)
        elif id > self.pet.id:
            if self.right is not None:
                self.right = self.right.delete(id)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_larger_node = self.right.get_min()
            self.pet = min_larger_node.pet
            self.right = self.right.delete(min_larger_node.pet.id)
        return self


    def get_min(self):
        if self.left is None:
            return self
        return self.left.get_min()

    def find_by_id(self, id: int):
        if self.pet.id == id:
            return self.pet
        elif id < self.pet.id and self.left:
            return self.left.find_by_id(id)
        elif id > self.pet.id and self.right:
            return self.right.find_by_id(id)
        else:
            raise Exception("ID no encontrado")

    def preorder(self):
        pets = [self.pet]
        if self.left:
            pets.extend(self.left.preorder())
        if self.right:
            pets.extend(self.right.preorder())
        return pets

    def postorder(self):
        pets = []
        if self.left:
            pets.extend(self.left.postorder())
        if self.right:
            pets.extend(self.right.postorder())
        pets.append(self.pet)
        return pets

    def exists_id(self, id: int):
        try:
            self.find_by_id(id)
            return True
        except:
            return False

    def count_by_breed(self):
        count = {}
        if self.left:
            left_count = self.left.count_by_breed()
            for breed, qty in left_count.items():
                count[breed] = count.get(breed, 0) + qty
        count[self.pet.breed] = count.get(self.pet.breed, 0) + 1
        if self.right:
            right_count = self.right.count_by_breed()
            for breed, qty in right_count.items():
                count[breed] = count.get(breed, 0) + qty
        return count

    def report_by_location_and_gender(self):
        report = {}
        if self.left:
            left_report = self.left.report_by_location_and_gender()
            for loc, genders in left_report.items():
                if loc not in report:
                    report[loc] = genders
                else:
                    for gen, count in genders.items():
                        report[loc][gen] = report[loc].get(gen, 0) + count
        loc = self.pet.location
        gen = self.pet.gender
        if loc not in report:
            report[loc] = {}
        report[loc][gen] = report[loc].get(gen, 0) + 1
        if self.right:
            right_report = self.right.report_by_location_and_gender()
            for loc, genders in right_report.items():
                if loc not in report:
                    report[loc] = genders
                else:
                    for gen, count in genders.items():
                        report[loc][gen] = report[loc].get(gen, 0) + count
        return report

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
    def preorder(self):
        pets = [self.pet]
        if self.left:
            pets.extend(self.left.preorder())
        if self.right:
            pets.extend(self.right.preorder())
        return pets

    def postorder(self):
        pets = []
        if self.left:
            pets.extend(self.left.postorder())
        if self.right:
            pets.extend(self.right.postorder())
        pets.append(self.pet)
        return pets


class NodeAVL(NodeABB):
    def __init__(self, pet: Pet):
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
