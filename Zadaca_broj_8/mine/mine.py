clacc Kvadrat(object):
    #Zadatak 7.2 - Kvadrat: implementacija
    def __init__(self, broj = 0):
        self.__broj = broj
        self.__otkriven = False
        self.__oznaka = False

    def otkrij(self):
        if self.__otkriven == False and self.__oznaka == False:
            self.__otkriven = True


    def oznaci(self):
        if self.__oznaka = False
            self.__oznaka = True

        else:
            self.__ozmaka = False



    @property
    def jeMIna(self):
        if self.__broj == -1:
            return True
        else:
            return False

    @property
    def jeBroj(self):
        if self.__broj != 0 and self.__broj != -1:
            return True
        else:
            return False

    @property
    def je Prazan(self):
        if self.__broj == 0:
            return True
        else:
            return False

#Zadatak 7.3 - Kvadrat : implementacija

    def __str__(self):
        if self.__oznaka == True:
            return "?"
        if self.otkriven == False:
            return "."
        else:
            if self.jeMina == True:
                return "x"
            if self.jeBroj == True:
                return "%d" % self.__broj
            if self.jePrazan == True:
                return " "



