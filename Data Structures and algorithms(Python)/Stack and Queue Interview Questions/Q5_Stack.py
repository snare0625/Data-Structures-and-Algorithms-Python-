#Animal shelter

class AnimalShelter:
    def __init__(self):
        self.cat = []
        self.dog = []

    def enqueue(self, animal, type):
        if type == "Cat":
            self.cat.append(animal)
        else:
            self.dog.append(animal)

    def dequeueDog(self):
        if len(self.dog) == 0:
            return None
        else:
            dog = self.dog.pop()
            return dog

    def dequeueCat(self):
        if len(self.cat) == 0:
            return None
        else:
            cat = self.cat.pop()
            return cat

    def dequeueAny(self):
        if len(self.dog) == 0:
            result = self.cat.pop()
        else:
            result = self.dog.pop()
        return result

customQueue = AnimalShelter()
customQueue.enqueue()