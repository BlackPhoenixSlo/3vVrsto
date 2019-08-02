IGRALEC_ZNAK = 'x'
RAČUNALNIK_ZNAK = 'o'
ZMAGA = 'W'
PORAZ = 'X' 
ZACETEK = 'Z'
polje_novo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

import math
import random
import copy
class Igra:
    def __init__(self):
        self.polje = copy.deepcopy(polje_novo)
        #if 1==random.randint(0,1):
        #    self.dodaj()
        #else:
        self.main()

    def transponiraj(self,map):
        polje2 = copy.deepcopy(polje_novo)
        for x in range(0, 3):
            for y in range(0, 3):
                polje2[y][x] = map[x][y]
        map = copy.deepcopy(polje2)
        return map

    def konec(self, map , d = 0 ):
        for x in map:
            if x.count(1) == 3 : 
                print ("Zmaga") 
                self.izpisi(map)
                return (map, 1)
            if x.count(-1) == 3 : 
                print ("Poraz") 
                self.izpisi(map)
                return (map, -1)

        map=self.transponiraj(map)
        for x in map:
            if x.count(1) == 3 : 
                print ("Zmaga") 
                self.izpisi(map)
                return (map, 1)
            if x.count(-1) == 3 : 
                print ("Poraz")
                self.izpisi(map)
                return (map, -1)

        map=self.transponiraj(map)

        st = 0

        for x in range(0,3):
            st += map[x][x]
        if st == 3 : 
            print ("Zmaga") 
            self.izpisi(map)
            return (map, 1)
        if st == -3 : 
            print ("Poraz") 
            self.izpisi(map)
            return (map, -1)
        
        st = 0

        for x in range(0,3):
            st += map[x][2-x]
        if st == 3 : 
            print ("Zmaga") 
            self.izpisi(map)
            return (map, 1)
        if st == -3 : 
            print ("Poraz") 
            self.izpisi(map)
            return (map, -1)

        st=0

        for x in map:
            st += x.count(0)
        if st == 0:
            return (map, 2)

        self.izpisi(map)
        return (map, 0)
        

        
        


    def main(self):       
        for i in range (0,5):
            self.dodaj()
            _,st=self.konec(self.polje)
            if st==2 :
                return
            self.dodam()
            _,st=self.konec(self.polje)
            if st==2 :
                return

    def dodam(self): 

        test = copy.deepcopy(self.polje)

        # za zmago
        for i in range(0,9):
            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = -1
                _,info= self.konec(test,1)
                
                print(info)
                if info == -1:
                    print("jaaas")
                    self.polje = copy.deepcopy(test)
                    return self.konec(self.polje)
                else:
                    test = copy.deepcopy(self.polje)
        
       
         # proti porazu
        for i in range(0,9):
            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = 1
                

                _,info= self.konec(test,1)
                
                print(info)
                if info == 1:
                    print("jaaas")
                    test[i // 3][i % 3] = -1
                    self.polje = copy.deepcopy(test)
                    return self.konec(self.polje)

                else:
                    test = copy.deepcopy(self.polje)    

        mesto = 4
        while self.polje[mesto // 3][mesto % 3] != 0:
            mesto = random.randint(0,8) 

        self.polje[mesto // 3][mesto % 3 ]= -1
        self.konec(self.polje)
        if info==1 or info == -1:
            return
        

    def dodaj(self):

        mesto = 9-int(input())
        while self.polje[mesto // 3][2 - mesto % 3] != 0:
            mesto = 9-int(input())

        self.polje[mesto // 3][2 - mesto % 3] = 1
        _,info=self.konec(self.polje)
        if info==1 or info == -1:
            return
        

    def izpisi(self,map):
        for x in map:
            print(x)


igra= Igra()
