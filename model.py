import math
import random
import copy

polje_novo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

polja_memo_forlink = []
polja_memo = []

countratio={}
import botAI
class Igra:

    def __init__(self):
        import math
        import random
        import copy
        import botAI

        self.last_polje={}
        self.lastset={}

        countratio[-1]=0
        countratio[1]=0
        countratio[2]=0
        self.polje = copy.deepcopy(polje_novo)

        self.bot1 = botAI.BotAI(1)
        self.bot2 = botAI.BotAI(-1)

        #self.learn()
        self.polje = copy.deepcopy(polje_novo)

        #self.soft_botvsbot()
        #print(polja_memo)
        #print(countratio)
        
        #self.boy_vs_mashine_realAI()

    def learn(self):

        for i in range(2000):
            self.polje = copy.deepcopy(polje_novo)

            self.learning_course()

            if (i%10==0):
                print (i)
                print(countratio)

    
    def learning_course (self): 

        if (random.randint(0,1)== 1):
            for _ in range (0,5):

                
                self.polje = self.bot1.nasledni(self.polje)

                _, st = self.konec(self.polje,0)

                if st == -1:
                    self.bot2.pomnitev()                 
                    #self.bot1.pomnitev(3)

                if st == 2 or st == 1 or st == -1 :
                    countratio[st] += 1
                    return

                #self.dodam_memo(-1)
                self.polje = self.bot2.nasledni(self.polje)

                _, st = self.konec(self.polje, 0)

                if st == 1:
                    self.bot1.pomnitev()
                    #self.bot2.pomnitev(3)            

                if st == 2 or st == 1 or st == -1 :
                    countratio[st] += 1
                    return

        else:
            for _ in range (0,5):

                
                #self.dodam_memo(-1)
                self.polje = self.bot2.nasledni(self.polje)

                _, st = self.konec(self.polje,0)

                if st == 1:
                    self.bot1.pomnitev()
                    #self.bot2.pomnitev(3) 
                if st == 2 or st == 1 or st == -1 :
                    countratio[st] += 1
                    return

                self.polje = self.bot1.nasledni(self.polje)

                _, st = self.konec(self.polje, 0)

                if st == -1:
                    self.bot2.pomnitev()            
                    #self.bot1.pomnitev(3) 
                if st == 2 or st == 1 or st == -1 :
                    countratio[st] += 1
                    return    


    def zasuk(self, map):

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

        return copy.deepcopy(polje2)


    def transponiraj(self, map):

        polje2 = copy.deepcopy(polje_novo)

        for x in range(0, 3):

            for y in range(0, 3):
                polje2[y][x] = map[x][y]

        map = copy.deepcopy(polje2)
        return map


    def konec(self, map , d = 0 ):

        for x in map:

            if x.count(1) == 3 : 

                #print ("Zmaga") 
                self.izpisi(map, d)
                return (map, 1)

            if x.count(-1) == 3 : 

                #print ("Poraz") 
                self.izpisi(map, d)
                return (map, -1)

        map = self.transponiraj(map)

        for x in map:

            if x.count(1) == 3 : 

                #print ("Zmaga") 
                self.izpisi(map, d)
                return (map, 1)

            if x.count(-1) == 3 : 
                #print ("Poraz")
                self.izpisi(map, d)
                return (map, -1)

        map = self.transponiraj(map)

        st = 0

        for x in range(0,3):
            st += map[x][x]

        if st == 3 : 

            #print ("Zmaga") 
            self.izpisi(map, d)
            return (map, 1)

        if st == -3 : 

            #print ("Poraz") 
            self.izpisi(map, d)
            return (map, -1)
        
        st = 0

        for x in range(0, 3):
            st += map[x][2-x]

        if st == 3 : 

            #print ("Zmaga") 
            self.izpisi(map, d)
            return (map, 1) 

        if st == -3 : 

            #print ("Poraz") 
            self.izpisi(map, d)
            return (map, -1)

        st=0

        for x in map:
            st += x.count(0)

        if st == 0:
            #print ("Izenaceno") 
            return (map, 2)

        self.izpisi(map, d)
        return (map, 0)


    def boy_vs_mashine(self):
        self.polje = copy.deepcopy(polje_novo)
        self.izpisi(self.polje,1)
        
        self.last_polje[-1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_polje[1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.lastset[-1] = -1
        self.lastset[1] = -1
        
        self.real_play()

        print("Konec, vpisi karkoli tazen 0 za nadaljevanje")
        a = input()

        if int(a) != 0:
            self.boy_vs_mashine()


    def boy_vs_mashine_realAI(self , cmd = 0):
        self.polje = copy.deepcopy(polje_novo)
        self.izpisi(self.polje,1)
        
        self.polje = copy.deepcopy(polje_novo)
        
        self.real_play_2_0()

        self.izpisi(self.polje,1)

        print("Konec, vpisi karkoli tazen 0 za nadaljevanje")
        if (cmd == 1):
            a = input()

            if int(a) != 0:
                self.boy_vs_mashine_realAI(1)
            

    def soft_botvsbot(self,rand = 1):
        for i in range(100000):
            self.polje = copy.deepcopy(polje_novo)
            if (i%10==0):
                print (i)
                print(countratio)

            self.last_polje[1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            self.last_polje[-1] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            self.lastset[1] = -1
            self.lastset[-1] = -1
            self.learning_for_soft_AI(i * rand)
            if (i%10==0):
                print (i)
                print(countratio)


    def learning_for_soft_AI(self, first): 

        a = 1      

        if first % 2 == 0:
            a = 1 

        for _ in range (0,5):

            self.dodam_memo(a)

            _, st = self.konec(self.polje,0)                                 
            if st == 2 or st == 1 or st == -1 :
                countratio[st] += 1
                return

            #self.dodam_memo(-a)
            self.good_add_for_guy()
            _, st = self.konec(self.polje, 0)

            if st == 2 or st == 1 or st == -1 :
                countratio[st] += 1
                return
         
    
    def real_play_2_0(self):     
        if (random.randint(0,1)== 1):
            for _ in range (0,5):
                self.dodaj()

                _, st = self.konec(self.polje)
            
                if st == 1:

                        self.bot1.pomnitev()

                if st == 2 or st == 1 or st == -1:
                    self.izpisi(self.polje, 1)
                    return

                self.polje = self.bot1.nasledni(self.polje)
                
                _, st = self.konec(self.polje, 1)
                
                if st == -1:

                        self.bot1.pomnitev(3)
                
                if st == 2 or st == 1 or st == -1:
                    return
        else:
            for _ in range (0,5):
                
                self.polje = self.bot1.nasledni(self.polje)
                
                _, st = self.konec(self.polje, 1)
                
                if st == -1:

                        self.bot1.pomnitev(3)
                
                if st == 2 or st == 1 or st == -1:
                    return

                self.dodaj()

                _, st = self.konec(self.polje)

                if st == 1:

                        self.bot1.pomnitev()
                if st == 2 or st == 1 or st == -1:
                    self.izpisi(self.polje, 1)
                    return


    def real_play(self):     

        for _ in range (0,5):
            self.dodaj()

            _, st = self.konec(self.polje)
          
            if st == 2 or st == 1 or st == -1:
                self.izpisi(self.polje, 1)
                return

            self.dodam_memo()
            
            _, st = self.konec(self.polje, 1)
            
            if st == 2 or st == 1 or st == -1:
                return


    def dodam_memo(self, op = 1): 

        test = copy.deepcopy(self.polje)

        # za zmago
        for i in range(0,9):

            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = -op
                _, info = self.konec(test, 0)

                if info == -op:

                    self.polje = copy.deepcopy(test)
                    self.lastset[op] = i
                    return

                else:

                    test = copy.deepcopy(self.polje)
        
       
        # proti porazu
        for i in range(0,9): 

            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = op

                _, info = self.konec(test,0)
                
                if info == op:

                    # 2 poražen
                    test[i // 3][i % 3] = 0
                    for j in range(i+1,9):

                        if test[j // 3][j % 3] == 0:
                            test[j // 3][j % 3] = op
                            _, info = self.konec(test, 0)

                            if info == op:

                                self.last_polje[1] [self.lastset[op] // 3][self.lastset[op] % 3] = 0
                                polja_memo_forlink.append(copy.deepcopy(self.last_polje[1]))

                                self.last_polje[1] [self.lastset[op] // 3][self.lastset[op] % 3] = 2
                                polja_memo.append(copy.deepcopy(self.last_polje[1]))
                                self.last_polje[1] = self.zasuk(copy.deepcopy(self.last_polje[1]))
                                polja_memo.append(copy.deepcopy(self.last_polje[1]))
                                self.last_polje[1] = self.zasuk(copy.deepcopy(self.last_polje[1]))
                                polja_memo.append(copy.deepcopy(self.last_polje[1]))
                                self.last_polje[1] = self.zasuk(copy.deepcopy(self.last_polje[1]))
                                polja_memo.append(copy.deepcopy(self.last_polje[1]))
                                    

                                test[j // 3][j % 3] = 0
                                break
                            test[j // 3][j % 3] = 0

                    test[i // 3][i % 3] = -op
                    self.last_polje[1] = copy.deepcopy(self.polje)
                    self.polje = copy.deepcopy(test)
                    self.lastset[op] = i
                    
                    return 

                else:
                    test = copy.deepcopy(self.polje)    

        if (self.polje in polja_memo_forlink) :

            mesto = 4
            while self.polje[mesto // 3][mesto % 3] != 0:
                mesto = random.randint(0, 8) 
            test = copy.deepcopy(self.polje)
            test[mesto // 3][mesto % 3] = 2

            if (test in polja_memo):
                test[mesto // 3][mesto % 3] = 0

                for i in range(9):

                    if test[i // 3][i % 3] == 0:
                        test[i // 3][i % 3] = 2

                        if (not test in polja_memo):
                            test[i // 3][i % 3] = -op
                            self.polje=copy.deepcopy(test) 
                            self.lastset[op] = i
                            self.last_polje[1] = copy.deepcopy(self.polje)
                            return

                        test[i // 3][i % 3] = 0
            else:

                test[mesto // 3][mesto % 3] = -op
                self.polje = copy.deepcopy(test) 
                self.lastset[op] = mesto
                self.last_polje[1] = copy.deepcopy(self.polje)
                return
        else: 

            mesto = 4

            if self.polje[mesto // 3][mesto % 3] != 0:
                mesto = random.randint(0,1)*2
            
            while self.polje[mesto // 3][mesto % 3] != 0:
                mesto = random.randint(0,8) 

            self.last_polje[1] = copy.deepcopy(self.polje)
            self.polje[mesto // 3][mesto % 3 ] = -op

            self.lastset[op] = mesto
            
   
    def good_add_for_guy(self): 

        test = copy.deepcopy(self.polje)

        # za zmago
        for i in range(0,9):

            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = 1
                _, info = self.konec(test,0)

                if info == 1:
                    self.polje = copy.deepcopy(test)
                    return 

                else:

                    test = copy.deepcopy(self.polje)

        # proti porazu
        for i in range(0,9):

            if test[i // 3][i % 3] == 0:
                test[i // 3][i % 3] = -1
                _, info = self.konec(test, 0)    

                if info == 1:
       
                    test[i // 3][i % 3] = 1
                    self.polje = copy.deepcopy(test)
                    return 

                else:

                    test = copy.deepcopy(self.polje)  

        mesto = random.randint(0,8) 
        while self.polje[mesto // 3][mesto % 3] != 0:
            mesto = random.randint(0,8) 

        self.polje[mesto // 3][mesto % 3 ] = 1
        self.konec(self.polje)

        if info == 1 or info == -1:
            return
        

    def dodaj(self, a = -1 ):

        if a == -1 : 
            mesto = 9-int(input())

            while self.polje[mesto // 3][2 - mesto % 3] != 0:
                mesto = 9-int(input())

            self.polje[mesto // 3][2 - mesto % 3] = 1
            _, info=self.konec(self.polje)
            if info == 1 or info == -1:
                return
        else:
            mesto = a
            if self.polje[mesto // 3][ mesto % 3] == 0:

                

                self.polje[mesto // 3][ mesto % 3] = 1
                _, info=self.konec(self.polje)
                if info == 1 or info == -1:                
                    return
        

    def izpisi(self, map, d = 0):
        if d == 1:
            for x in map:
                print(x)
            print("_________")


#igra= Igra()
#igra.boy_vs_mashine_realAI()
