class Kruznica(object):

    def __init__(self, radijus):
        self.radijus = radijus


    def __str__(self):
        return "Kruznica radiusa %.2f" % (self.radijus)


class Kvadrat():

    def __init__(self, duljina_stranice):
        self.duljina_stranice = duljina_stranice





    def __str__(self):
        return 'Kvadrat duljine stranice %.2f'%(self.duljina_stranice)







if __name__ == '__main__':
    kruznica = Kruznica(12)
    kvadrat = Kvadrat(5)
    print(kruznica)
    print(kvadrat)
