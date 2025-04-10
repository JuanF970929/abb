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

