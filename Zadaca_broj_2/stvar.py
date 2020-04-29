class Stvar(object):
    broj_stvari = 0

    def __init__(self):
        Stvar.broj_stvari += 1

    def __del__(self):
        Stvar.broj_stvari -= 1