# question 1
class Fraction:
    def __init__(self, num, den):
        assert den != 0, "Le dénominateur ne peut pas être nul"
        self.__num = num
        self.__den = den

 # Q2

class Fraction:
    def __init__(self, num, den):
        assert den != 0, "Le dénominateur ne peut pas être nul"
        self.__num = num
        self.__den = den

    def __str__(self):
        if self.__den == 1:
            return str(self.__num)
        else:
            return str(self.__num) + '/' + str(self.__den)   

    #Q3

class Fraction:
    def __init__(self, num, den):
        assert den != 0, "Le dénominateur ne peut pas être nul"
        self.__num = num
        self.__den = den

    def __str__(self):
        if self.__den == 1:
            return str(self.__num)
        else:
            return str(self.__num) + '/' + str(self.__den)

# Création des instances
F1 = Fraction(3, 4)
F2 = Fraction(-8, 1)
F3 = Fraction(2, 3)
F4 = Fraction(21, 28)

# Affichage des instances
print(F1)
print(F2)
print(F3)
print(F4)    

# Q4 

class Fraction:
    def __init__(self, num, den):
        assert den != 0, "Le dénominateur ne peut pas être nul"
        self.__num = num
        self.__den = den

    def __str__(self):
        if self.__den == 1:
            return str(self.__num)
        else:
            return str(self.__num) + '/' + str(self.__den)

    def __eq__(self, other):
        return self.__num * other.__den == self.__den * other.__num
    
    # Création des instances
F1 = Fraction(3, 4)
F2 = Fraction(-8, 1)
F3 = Fraction(2, 3)
F4 = Fraction(21, 28)

# Tests d'égalité
print(F1 == F2)  # False
print(F1 == Fraction(6, 8))  # True
print(F3 == Fraction(4, 6))  # True
print(F3 == F4)  # False



