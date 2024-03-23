# Exercice 1

def pgcd(a, b):
    """Returns the maximum devider of a and b"""
    if b==0: 
        return a 
    else:
        r = a % b 
        return pgcd(b, r)

class fraction:
    def __init__(self, numerator, denominator):
        self.__num = numerator
        self.__denom = denominator
        if type(numerator) != int or type(denominator) != int: # we check the types
            raise TypeError("Numbers are not integers")
        if denominator == 0:
            raise ValueError("Denominator must be none zero") # we check if the denominator is none zero

    def show(self):
        return "(%s/%s)"%(self.__num, self.__denom)
    
    def __eq__(self, other):
        """We define == operator"""
        self = self.__simplify__()
        other = other.__simplify__()
        if self.__denom == other.__denom and self.__num == other.__num:
            return True
        return False
    
    def __simplify__(self):
        """Simplifies fractions self and other"""
        devider = pgcd(self.__num, self.__denom)
        self.__num = int(self.__num/devider)
        self.__denom = int(self.__denom/devider)
        return self

    def __add__(self, other):
        """Adds fractions self and other"""
        self.__num = self.__num * other.__denom + other.__num * self.__denom
        self.__denom = self.__denom * other.__denom
        self = self.__simplify__()
        return fraction(self.__num,self.__denom)

    def __mult__(self, other):
        """Mutliplies fractions self and other"""
        self.__num = self.__num * other.__num
        self.__denom = self.__denom * other.__denom
        return fraction(self.__num,self.__denom)


    
if __name__ == '__main__':
    fraction1 = fraction(1,2)
    fraction2 = fraction(1,2)
    fraction3 = fraction(4,4)
    # asserts __add__ & __eq__ & __simplify__
    assert fraction1.__eq__(fraction2)
    assert (fraction1+fraction2).__eq__(fraction3)
    
    # asserts __mult__
    #assert fraction1.__mult__(fraction2) == fraction(1,4)


# Exercice 3
    
def harmonic(n):
    value = fraction(1,2)
    value_before = fraction(1,1)
    for i in range (3,n+1):
        value = value.__add__(fraction(1,i))
        # verification
        value = value.show().replace("(", "").replace(")", "")
        value_before = value_before.show().replace("(", "").replace(")", "")
        # splting numerator and denominator
        num_value, denom_value = value.split("/")
        num_value_before, denom_value_before = value_before.split("/")
        # converting into integers
        numerator = int(num_value)
        denominator = int(denom_value)
        numerator_before = int(num_value_before)
        denominator_before = int(denom_value_before)
        #assert numerator/denominator > numerator_before/denominator_before
    return value.show()



# Exercice 4

def leibniz(n):
    value = fraction(1,1)
    for i in range (1,n):
        if i%2 == 0:
            value += fraction(1,2*i+1)
        else:
            value += fraction(-1,2*i+1)
    return value.show()

#print(leibniz(10000))
#print(3.14/4)

# Exercice 5

class Polynomial():
    def __init__(self, coefficients) -> None:
        self.coefficients = coefficients

    def __str__(self):
        polynomial_str = ""
        degree = len(self.coefficients) - 1

        for power, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if power == 0:
                    polynomial_str += f"{coeff} "
                elif power == 1:
                    polynomial_str += f"{coeff}x "
                else:
                    polynomial_str += f"{coeff}x^{power} "
                if power < degree:
                    polynomial_str += "+ "
        return polynomial_str
    def differentiate(self):
        """
        Differentiate the polynomial.
        """
        derivative_coefficients = [i * coeff for i, coeff in enumerate(self.coefficients)][1:]
        return Polynomial(derivative_coefficients)
    
    def add(self, other):
        """
        Add another polynomial to this polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        result_coefficients = []

        for i in range(max_length):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            result_coefficients.append(coeff1 + coeff2)

        return Polynomial(result_coefficients)
    
    def integrate(self, constant=0):
        """
        Integrate the polynomial.
        """
        integral_coefficients = [constant] + [(1 / (i + 1)) * coeff for i, coeff in enumerate(self.coefficients)]
        return Polynomial(integral_coefficients)
    
if __name__ == '__main__':
    P = Polynomial([1,2,3, 9])
    print(P)
    print(P.differentiate())
    print(P.integrate())
    print(P.add(Polynomial([1,2,3])))