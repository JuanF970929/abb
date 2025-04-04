from model.pet import Pet

class ABB():
    def __init__(self):
        self.root = None

    def add(self, pet:Pet):
        if self.root == None:
            self.root = NodeABB(pet)
        else:
            self.root.add(pet)

class NodeABB:
    def __init__(self, pet:Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    def add(self, pet:Pet):
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


class NodeAVL(NodeABB):
    def __init__(self, pet:Pet):
        super().__init__(pet)
        self.height = 1
        self.balance = 1