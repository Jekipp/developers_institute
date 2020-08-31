import random

class Gene():
    def __init__(self):
        self.value = random.choice([True, False])

    def mutate(self):
        self.value = not self.value

class Chromosome():
    def __init__(self):
        self.value = [ Gene() for i in range(10)]

        def mutate(self):
            for gene in self.value:
                must_mutate = random.choice([True, False])
                gene.mutate()
