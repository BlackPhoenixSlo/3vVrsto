import math
import random
import copy


polje_novo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


class BotAI:
    polja_memo_forlink = {}
    polja_memo = {}

    polja_memo_forlink["w1"] = []
    polja_memo["w1"] = {}
    polja_memo_forlink["w2"] = []
    polja_memo["w2"] = {}
    polja_memo_forlink["l1"] = []
    polja_memo["l1"] = {}
    polja_memo_forlink["l2"] = []
    polja_memo["l2"] = {}

    def __init__(self, op=1):

        self.op = op

        self.last_polje = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_polje = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.lastset = -1
        self.lastset = -1

        self.polje = copy.deepcopy(polje_novo)

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

    def res(self):

        self.polje = copy.deepcopy(polje_novo)

        self.last_polje = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.lastset = -1

    # V Prešnem AI sem imel za vsak možni izid poraza toliko celic kot je bilo prostih mest
    # Tukaj za vsak možni poraz le ena celica in to celico zapolnujem z 2 proti porazom oz 3 za zmago
    # To sem naredil tako, da sem
    # BotAI.polja_memo[zmaga/zguba/prvi/drugi][str(prejšna_polja)][prejšna_pozicija // 3][prejšna_pozicija % 3]
    # nastavil na 2 ali 3 po potrebi

    def pomnitev(self, placement="l1"):

        type1 = 3
        if placement == "l1" or placement == "l2":
            type1 = 2

        for _ in range(4):
            # Najprej pa seveda preveril ali takšna pozicija obstaja
            if self.last_polje in BotAI.polja_memo_forlink[placement]:
                BotAI.polja_memo[placement][str(self.last_polje).replace(
                    " ", "")][self.lastset // 3][self.lastset % 3] = type1

            else:

                BotAI.polja_memo_forlink[placement].append(
                    copy.deepcopy(self.last_polje))
                test = copy.deepcopy(self.last_polje)
                self.last_polje[self.lastset // 3][self.lastset % 3] = type1

                BotAI.polja_memo[placement][str(test).replace(
                    " ", "")] = copy.deepcopy(self.last_polje)

                self.last_polje[self.lastset // 3][self.lastset % 3] = 0

            self.last_polje = self.zasuk(copy.deepcopy(self.last_polje))

    def nasledni(self, mapa, placement="l1"):

        self.polje = mapa
        op = self.op
        test = copy.deepcopy(self.polje)

        if (placement == "l1"):
            placement2 = "w1"
        else:
            placement2 = "w2"

        for i in range(9):
            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = 3

                if any([test == BotAI.polja_memo[placement2][str(x).replace(" ", "")] for x in BotAI.polja_memo_forlink[placement2]]):
                    self.last_polje = copy.deepcopy(self.polje)
                    self.polje[i // 3][i % 3] = -op

                    self.lastset = i
                    return copy.deepcopy(self.polje)
                test[i // 3][i % 3] = 0

        # če je polje v poziciji iščem v tej poziciji toliko časa dokler ne najdem praznega polja,
        # če take pozicije ni, kličem pomnitem

        if (test in BotAI.polja_memo_forlink[placement]):
            for i in range(9):
                if str(test).replace(" ", "") in BotAI.polja_memo:
                    if BotAI.polja_memo[placement][str(test).replace(" ", "")][i // 3][i % 3] == 0:
                        test[i // 3][i % 3] = -op
                        self.polje = copy.deepcopy(test)
                        self.lastset = i
                        self.last_polje = copy.deepcopy(self.polje)
                        return copy.deepcopy(self.polje)
                    self.pomnitev()

        mesto = random.randint(0, 8)

        while self.polje[mesto // 3][mesto % 3] != 0:
            mesto = random.randint(0, 8)

        self.last_polje = copy.deepcopy(self.polje)
        self.polje[mesto // 3][mesto % 3] = -op

        self.lastset = mesto

        return copy.deepcopy(self.polje)
