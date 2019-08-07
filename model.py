import math
import random
import copy

polje_novo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
countratio = {}


class Igra:

    # Podam vse spremenljivke in jih nastavim na 0
    def __init__(self):
        import botAI

        self.last_polje = {}
        self.lastset = {}

        countratio[-1] = 0
        countratio[1] = 0
        countratio[2] = 0
        self.polje = copy.deepcopy(polje_novo)

        self.bot1 = botAI.BotAI(1)
        self.bot2 = botAI.BotAI(-1)

    # Program igra sam proti sebi in se s tem nauči igrati 3 v vrsto
    def learn(self):

        for i in range(1000):
            self.polje = copy.deepcopy(polje_novo)

            self.learning_course()

            # izpiše score
            if (i % 10 == 0):
                print(i)
                print(countratio)

    # Potek igre ko AI igra sam proti sebi
    def learning_course(self):

        for _ in range(0, 5):

            self.polje = self.bot1.nasledni(self.polje, "l1")

            st = self.konec(self.polje)

            if st == -1:
                self.bot2.pomnitev("l2")
                self.bot1.pomnitev("w1")

            if st != 0:
                countratio[st] += 1
                return

            self.polje = self.bot2.nasledni(self.polje, "l2")

            st = self.konec(self.polje)

            if st == 1:
                self.bot1.pomnitev("l1")
                self.bot2.pomnitev("w2")

            if st != 0:

                countratio[st] += 1
                return

    # Program začne igro kjer igra človek proti AI
    def boy_vs_mashine_realAI(self, cmd=0):
        self.polje = copy.deepcopy(polje_novo)

        self.izpisi(self.polje, 1)

        self.polje = copy.deepcopy(polje_novo)

        self.real_play_2_0()

        self.izpisi(self.polje, 1)

        print("Konec, vpisi karkoli tazen 0 za nadaljevanje")
        if (cmd == 1):
            a = input()

            if int(a) != 0:
                self.boy_vs_mashine_realAI(1)

    # igralno polje se zavrti za 90° v levo
    def zasuk(self, map):

        polje2 = copy.deepcopy(polje_novo)

        polje2[0][0] = copy.deepcopy(map[0][2])
        polje2[1][0] = copy.deepcopy(map[0][1])
        polje2[2][0] = copy.deepcopy(map[0][0])
        polje2[0][1] = copy.deepcopy(map[1][2])
        polje2[0][2] = copy.deepcopy(map[2][2])
        polje2[1][1] = copy.deepcopy(map[1][1])
        polje2[2][1] = copy.deepcopy(map[1][0])
        polje2[1][2] = copy.deepcopy(map[2][1])
        polje2[2][2] = copy.deepcopy(map[2][0])

        return copy.deepcopy(polje2)

    # igralno polje se zavrti za 180° v levo
    def transponiraj(self, map):

        polje2 = copy.deepcopy(polje_novo)

        for x in range(0, 3):

            for y in range(0, 3):
                polje2[y][x] = map[x][y]

        map = copy.deepcopy(polje2)
        return map

    # Program preveri ali se je igra končala in določi kdo je zmagal ali neodločeno
    def konec(self, map, op=1):

        for i in range(3):
            if all([self.polje[i][j] == op for j in range(3)]):
                #print ("Zmaga")
                return (op)

            if all([self.polje[i][j] == -op for j in range(3)]):
                #print ("poraz")
                return (-op)

            if all([self.polje[j][i] == op for j in range(3)]):
                #print ("Zmaga")
                return (op)

            if all([self.polje[j][i] == -op for j in range(3)]):
                #print ("poraz")
                return (-op)

        if all([self.polje[i][i] == op for i in range(3)]):
            #print ("Zmaga")
            return (op)

        if all([self.polje[i][i] == -op for i in range(3)]):
            #print ("poraz")
            return (-op)

        if all([self.polje[i][2-i] == op for i in range(3)]):
            #print ("Zmaga")
            return (op)

        if all([self.polje[i][2-i] == -op for i in range(3)]):
            #print ("poraz")
            return (-op)

        st = 0
        for x in map:
            st += x.count(0)

        if st == 0:
            #print ("Izenaceno")
            return (2)

        return (0)

    # Potek igre igralec proti AI
    def real_play_2_0(self):
        # izbira kdo gre 1. ali drugi
        if (random.randint(0, 1) == 1):
            for _ in range(0, 5):
                self.dodaj()

                st = self.konec(self.polje)

                if st == 1:
                    self.bot1.pomnitev("l2")

                if st != 0:
                    return

                self.polje = self.bot1.nasledni(self.polje, "l2")
                self.izpisi(self.polje, 1)

                st = self.konec(self.polje, 1)

                if st == -1:

                    self.bot1.pomnitev("w2")

                if st != 0:
                    return
        else:
            for _ in range(0, 5):

                self.polje = self.bot1.nasledni(self.polje, "l1")
                self.izpisi(self.polje, 1)

                st = self.konec(self.polje, 1)

                if st == -1:
                    self.bot1.pomnitev("w1")

                if st != 0:
                    return

                self.dodaj()
                st = self.konec(self.polje)

                if st == 1:
                    self.bot1.pomnitev("l1")

                if st != 0:
                    return

    # Metoda doda element preko tipkovnice ali preko spletnega vmesnika
    def dodaj(self, mesto=-1):

        if mesto == -1:
            mesto = 9-int(input())

            while self.polje[mesto // 3][2 - mesto % 3] != 0:
                mesto = 9-int(input())

            self.polje[mesto // 3][2 - mesto % 3] = 1

        else:

            if self.polje[mesto // 3][mesto % 3] == 0:
                self.polje[mesto // 3][mesto % 3] = 1

    # Program izpiše polje v terminal
    def izpisi(self, map, d=0):
        if d == 1:
            for x in map:
                print(x)
            print("_________")
