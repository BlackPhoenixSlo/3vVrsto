import math
import random
import copy


polje_novo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


class BotAI:
    polja_memo = {}
    # 4 spominske celice, ali zmaga ali zgubi ko gre prvi ali drugi
    polja_memo["w1"] = []
    polja_memo["w2"] = []
    polja_memo["l1"] = []
    polja_memo["l2"] = []

    # Podam vse spremenljivke in jih nastavim na 0
    def __init__(self, op=1):
        import math
        import random
        import copy

        self.op = op

        self.last_polje = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_polje = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.lastset = -1
        self.lastset = -1

        self.polje = copy.deepcopy(polje_novo)

    # igralno polje se zavrti za 90° v levo , map = 0 je zaradi spletnega vmesnika
    def zasuk(self, map=0):

        if map == 0:
            map = self.polje

        polje2 = copy.deepcopy(polje_novo)

        polje2[0][0] = map[0][2]
        polje2[1][0] = map[0][1]
        polje2[2][0] = map[0][0]
        polje2[0][1] = map[1][2]
        polje2[0][2] = map[2][2]
        polje2[1][1] = map[1][1]
        polje2[2][1] = map[1][0]
        polje2[1][2] = map[2][1]
        polje2[2][2] = map[2][0]

        if map == 0:
            self.polje = map

        return polje2

    # Funkcija za spletni umesnik, igra se začne znova
    def res(self):

        self.polje = copy.deepcopy(polje_novo)

        self.last_polje = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.lastset = -1

    # Program vnese spoznanje kam mora oz. nesme postaviti križca/krožca če želi zmagat oz. ne želi izgubutu
    def pomnitev(self, placement="l1"):

        type1 = 3
        if placement == "l1" or placement == "l2":
            type1 = 2

        self.last_polje[self.lastset // 3][self.lastset % 3] = 0

        self.last_polje[self.lastset // 3][self.lastset % 3] = type1

        for _ in range(4):
            BotAI.polja_memo[placement].append(copy.deepcopy(self.last_polje))
            self.last_polje = self.zasuk(copy.deepcopy(self.last_polje))

    # Program določi svojo naslednjo pozicijo na polju za 3 v vrsto
    def nasledni(self, mapa, placement="l1"):

        self.polje = mapa
        op = self.op
        test = copy.deepcopy(self.polje)

        if (placement == "l1"):
            placement2 = "w1"
        else:
            placement2 = "w2"

        # Preveri če lahko zmaga
        for i in range(9):
            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = 3
                if (test in BotAI.polja_memo[placement2]):
                    self.last_polje = copy.deepcopy(self.polje)
                    self.polje[i // 3][i % 3] = -op

                    self.lastset = i
                    return copy.deepcopy(self.polje)
                test[i // 3][i % 3] = 0

        # Da na prazno mesto
        mesto = random.randint(0, 8)
        while self.polje[mesto // 3][mesto % 3] != 0:
            mesto = random.randint(0, 8)

        test[mesto // 3][mesto % 3] = 2

        # Preveri, da ne bo igubil zaradi postavitve na to mesto
        if (test in BotAI.polja_memo[placement]):
            test[mesto // 3][mesto % 3] = 0
            # V Primeru da izgubi preveri ali obstaja kakšno drugo pravilno mesto
            for i in range(9):
                if test[i // 3][i % 3] == 0:
                    test[i // 3][i % 3] = 2

                    if (not test in BotAI.polja_memo[placement]):

                        test[i // 3][i % 3] = -op
                        self.polje = copy.deepcopy(test)
                        self.lastset = i
                        self.last_polje = copy.deepcopy(self.polje)
                        return copy.deepcopy(self.polje)

                    test[i // 3][i % 3] = 0
            # Če takšnega mesta ni si zapomni da na prejšno pozicijo nesme dati križca ali krožca
            self.pomnitev()
            # Program nadaljuje kot da neve da nesme postaviti na prvotno mesto

        # Program postavi na mesto križec ali krožec in konča
        self.last_polje = copy.deepcopy(self.polje)
        self.polje[mesto // 3][mesto % 3] = -op

        self.lastset = mesto

        return copy.deepcopy(self.polje)
