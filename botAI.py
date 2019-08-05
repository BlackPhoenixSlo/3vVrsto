import math
import random
import copy


polje_novo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



class BotAI:

    def __init__(self, op = 1):
        import math
        import random
        import copy

        self.polja_memo_forlink = []
        self.polja_memo = []


        self.op = op

        self.last_polje={}
        self.lastset={}

        self.last_polje[-1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_polje[1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.lastset[-1] = -1
        self.lastset[1] = -1

        self.polje = copy.deepcopy(polje_novo)

    def zasuk(self, map = 0):

        if map == 0:
            map = self.polje

        polje2 = copy.deepcopy(polje_novo)

        polje2[0][0]=copy.deepcopy(map[0][2]) 
        polje2[1][0]=copy.deepcopy(map[0][1])
        polje2[2][0]=copy.deepcopy(map[0][0]) 
        polje2[0][1]=copy.deepcopy(map[1][2]) 
        polje2[0][2]=copy.deepcopy(map[2][2]) 
        polje2[1][1]=copy.deepcopy(map[1][1]) 
        polje2[2][1]=copy.deepcopy(map[1][0]) 
        polje2[1][2]=copy.deepcopy(map[2][1]) 
        polje2[2][2]=copy.deepcopy(map[2][0]) 

        if map == 0:
            self.polje = map

        return copy.deepcopy(polje2)

    def res(self):

        self.polje = copy.deepcopy(polje_novo)

        self.last_polje[-1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_polje[1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.lastset[-1] = -1
        self.lastset[1] = -1

    def pomnitev(self, type1 = 2):

        op = self.op

        

        self.last_polje[1] [self.lastset[op] // 3][self.lastset[op] % 3] = 0
        self.polja_memo_forlink.append(copy.deepcopy(self.last_polje[1]))

        self.last_polje[1] [self.lastset[op] // 3][self.lastset[op] % 3] = type1
        self.polja_memo.append(copy.deepcopy(self.last_polje[1]))
        self.last_polje[1] = self.zasuk(copy.deepcopy(self.last_polje[1]))
        self.polja_memo.append(copy.deepcopy(self.last_polje[1]))
        self.last_polje[1] = self.zasuk(copy.deepcopy(self.last_polje[1]))
        self.polja_memo.append(copy.deepcopy(self.last_polje[1]))
        self.last_polje[1] = self.zasuk(copy.deepcopy(self.last_polje[1]))
        self.polja_memo.append(copy.deepcopy(self.last_polje[1]))
         

    def nasledni (self, mapa ):

        self.polje = mapa
        op = self.op
        test = copy.deepcopy(self.polje)

#        for i in range(9):
#            if test[i // 3][i % 3] == 0:
#                test[i // 3][i % 3] = 3
#                if (test in self.polja_memo):
#                    self.last_polje[1] = copy.deepcopy(self.polje)
#                    self.polje[i // 3][i % 3 ] = -op
#
#                    self.lastset[op] = i    
#                    return copy.deepcopy(self.polje)
#                test[i // 3][i % 3] = 0

        #za zmago
        for i in range(0,9):

            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = -op
                _, info = self.konec(test, 0)

                if info == -op:

                    self.polje = copy.deepcopy(test)
                    self.lastset[op] = i
                    return copy.deepcopy(test)
                test[i // 3][i % 3] = 0
           
        test = copy.deepcopy(self.polje)


        

        mesto = random.randint(0, 8)
        while self.polje[mesto // 3][mesto % 3] != 0:
            mesto = random.randint(0, 8)

        test = copy.deepcopy(self.polje)
        test[mesto // 3][mesto % 3] = 2


        if (test in self.polja_memo):
            test[mesto // 3][mesto % 3] = 0

            for i in range(9):
                if test[i // 3][i % 3] == 0:
                    test[i // 3][i % 3] = 2

                    if (not test in self.polja_memo):

                        test[i // 3][i % 3] = -op
                        self.polje=copy.deepcopy(test) 
                        self.lastset[op] = i
                        self.last_polje[1] = copy.deepcopy(self.polje)
                        return copy.deepcopy(self.polje)

                    test[i // 3][i % 3] = 0

            self.pomnitev()

        self.last_polje[1] = copy.deepcopy(self.polje)
        self.polje[mesto // 3][mesto % 3 ] = -op

        self.lastset[op] = mesto    

        return copy.deepcopy(self.polje)

    def konec(self, map , d = 0 ):

        for x in map:

            if x.count(1) == 3 : 

                #print ("Zmaga") 
                
                return (map, 1)

            if x.count(-1) == 3 : 

                #print ("Poraz") 
                
                return (map, -1)

        map = self.transponiraj(map)

        for x in map:

            if x.count(1) == 3 : 

                #print ("Zmaga") 
                
                return (map, 1)

            if x.count(-1) == 3 : 
                #print ("Poraz")
                
                return (map, -1)

        map = self.transponiraj(map)

        st = 0

        for x in range(0,3):
            st += map[x][x]

        if st == 3 : 

            #print ("Zmaga") 
            
            return (map, 1)

        if st == -3 : 

            #print ("Poraz") 
            
            return (map, -1)
        
        st = 0

        for x in range(0, 3):
            st += map[x][2-x]

        if st == 3 : 

            #print ("Zmaga") 
            
            return (map, 1) 

        if st == -3 : 

            #print ("Poraz") 
            
            return (map, -1)

        st=0

        for x in map:
            st += x.count(0)

        if st == 0:
            #print ("Izenaceno") 
            return (map, 2)

        
        return (map, 0)

    
    def transponiraj(self, map):

        polje2 = copy.deepcopy(polje_novo)

        for x in range(0, 3):

            for y in range(0, 3):
                polje2[y][x] = map[x][y]

        map = copy.deepcopy(polje2)
        return map



        