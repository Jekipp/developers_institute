# class Library
#     books = []
#
# class Book:
#     title
#     author
#     pub date
#
# class Gene:
#     1 / 0
#
# class Chromosome:
#     gene = [gene1, gene2 ... gene10]
#
# variables, data structure, functions, loops, classes, inheritence

# __init__
#  __repr__ returns a string that uniquely identifies an instance of a class
# represented         double underscore, default method
#  __str__ similar to __repr__ method
# __call__


from random import choice

class Gene():
    def__init__(self):
    self.value = random.choice([0, 1])

      def mutate(self):
        self.value = 1 if self.value == 0 else 0
  def mutate2(self):
      abs(self.value - 1)

  def mutate3(self):

class Gene():
    def__init__(self):
    self.value = random.choice([True, False])

    def mutate(self):
        self.value = not self.value
    def __repr__(self):
        return str(self.value)
        return "1" if self.value else "0"

class Chromosome():
    def __init__(self):
        self.value = [Gene() for i in range(10)]

    def mutate(self):
        for gene in self.value:
            if random.choice([True, False]):
                gene.mutate()
        def__repr__(self):
            return str(self.value)

class DNA():
    def __init__(self):
        self.value = [Chromosome() for i in range(10)]
            for choromosome in self.value:
                if random.choice([True, False]):
                    chromosome.mutate()


class Organism():
    def __init__ (self, dna, probability_to_mutate)
        self.dna = dna
        self.probility_to_mutate = probility_to_mutate

    def mutate(self):
        if random.random() <= self.probility_to_mutate:
            self.dna.mutate()
    def __repr__ (self):
        return str(self.dna)

class Evolution():
    def __init__ (self, num_of_organisms)
        self.population = [Organism(DNA, .8) for i in range(num_of_organisms)]
        self.generations = 0

        def is_compete(self):
            for organism in self.population:
                for dna in organism:
                    for chromosome in dna:

                        for gene in chromosome:
                            return all(gene.value)


    def big_bang(self):

        for organism in self.population:
            organism.mutate()
