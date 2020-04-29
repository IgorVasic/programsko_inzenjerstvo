class Kruznica(object):

    def __init__(self, radijus):
        self.radijus = radijus


    def __str__(self):
        return f'Kruznica radiusa {round(self.radijus,2):f}'


class Kvadrat():

    def __init__(self, duljina_stranice):
        self.duljina_stranice = duljina_stranice





    def __str__(self):
        return f'Kvadrat duljine stranice {round(self.duljina_stranice,2):f}'







if __name__ == '__main__':
    kruznica = Kruznica(12)
    kvadrat = Kvadrat(5)
    print(kruznica)
    print(kvadrat)
