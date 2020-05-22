class Polje(object):
#Zadatak 7.2 - Polje implementacije

    __init__(self, broj = 0):
        self.__broj = broj



    def vratiBroj(self):
        return Polje.__broj


    @property
    def jeBroj(self):
        if self.__broj == 0:
            return False
        else:
            return True


    @property
    def jePrazno(self):
        if Polje.__broj == 0:
            return False
        else:
            return True

    def __str__(self):
        broj = self.vratiBroj()
        if broj > 0:
            return str(broj)
        elif broj == 0:
            return " "

    def __repr__(self):
        return "Polje({})".format(self.vratiBroj())

#Zadatak 7.3 - Polje implementacije

brojevi = list(range(8))
for broj in brojevi:
    p = Polje(broj)
    print(p.vratiBroj(), p.jeBroj, p.jePolje)




