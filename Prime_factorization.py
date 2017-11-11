# David Omrai 4.PT
# 17.10.2017

# Simple program for prime factorization
class rozklad():
    def __init__(self):
        self.i = 2
        self.pom = 0
        try:
            self.cislo = int(input("Enter a number: "))
        except:
            self.cislo = -1
            print("Please, enter a number.")  
        self.zjisti()         
    def zjisti(self):
        while self.cislo <= 0:
            print("Please, enter a number bigger than 1.")
            try:
                self.cislo = int(input("Enter a number: "))
            except:
                cislo = -1
                print("Please, enter a number")
        self.vystup = "Entered "+str(self.cislo)+", division to prime numbers: "
        if self.cislo == 1:
            self.vystup += str(1)
            self.vypis()
        else: self.vypocti()
    def vypocti(self):
        while self.cislo != 1:
            self.pom = 0
            while self.pom != 1:
                if self.cislo % self.i == 0:
                    self.vystup += str(self.i)+" "
                    self.cislo = int(self.cislo / self.i)
                    self.pom = 1
                    self.i = 2
                else: self.i += 1
        self.vypis()
    def vypis(self):
        print(self.vystup)
rozklad()
