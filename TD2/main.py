# Exercice 1

class fraction:
    def __init__(self, numerateur, denominateur):
        self.num = numerateur
        self.denom = denominateur

    def __str__(self):
        return "(%s/%s)"%(self.num, self.denom)
    
if __name__ == '__main__':
    f = fraction(2, 3)
    print(f)