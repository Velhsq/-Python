class Clothes:
    @property
    def get_tissue_consuption(self):
        pass

    def summ_tissue_consuption(self, *args):
        tissue_consuption_summ = self.get_tissue_consuption()
        for i in args:
            tissue_consuption_summ += i.get_tissue_consuption()
        return tissue_consuption_summ

    def __add__(self, other):
        return self.get_tissue_consuption() + other.get_tissue_consuption()


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    def get_tissue_consuption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    def get_tissue_consuption(self):
        return 2 * self.h + 0.3


coat = Coat(5)
suit = Suit(4)

print(coat.get_tissue_consuption())
print(suit.get_tissue_consuption())
print(coat.summ_tissue_consuption(suit))
print(coat + suit)
print(suit + coat)

