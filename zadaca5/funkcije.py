import likovi
from math import *


def opseg(lik):
    if isinstance(lik, likovi.Kruznica):
        return 2 * lik.radijus * pi
    elif isinstance(lik, likovi.Kvadrat):
        return 4 * lik.duljina_stranice


def povrsina(lik):
    if isinstance(lik, likovi.Kruznica):
        return   (lik.radijus ** 2) * pi
    elif isinstance(lik, likovi.Kvadrat):
        return lik.duljina_stranice ** 2


if __name__=='__main__':
    print(opseg.__name__)
    print(povrsina.__name__)
