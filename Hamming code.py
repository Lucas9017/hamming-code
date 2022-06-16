class Matrix:
    def __init__(self, elementen = [], kolommen = 0):
        self.elementen = elementen
        self.kolommen = kolommen
    
    def isMatrix(self):
        if isinstance(self,Matrix) and len(self.elementen) % self.kolommen == 0:
            return True
        else:
            return False

    def __str__(self):
        if self.isMatrix():
            return str(self.elementen) + ', ' + str(self.kolommen)
        else:
            raise TypeError('input is geen matrix')

    def __add__(self,other):
        som = Matrix()
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0,len(self.elementen)):
                som.elementen.append(self.elementen[i] + other.elementen[i])
            som.kolommen = self.kolommen
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return som

    __radd__ = __add__

    def __sub__(self,other):
        verschil = Matrix()
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0,len(self.elementen)):
                verschil.elementen.append(self.elementen[i] - other.elementen[i])
            verschil.kolommen = self.kolommen
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return verschil

    __rsub__ = __sub__  

    def __mul__(self,other):
        product = Matrix()
        if self.isMatrix() and other.isMatrix():
            m = self.elementen // self.kolommen
            n = self.kolommen
            p = other.kolommen
            if n == other.elementen // other.kolommen:
                for i in range(0,m):
                    for j in range(0,p):
                        1
                product.kolommen = self.kolommen
            else:
                raise TypeError('de matrices hebben niet de juiste afmetingen')
        return product

    __rmul__=__mul__

    def __eq__(self,other):
        teller_s=self.a*other.b
        teller_o=other.a*self.b
        return teller_s==teller_o

    def __ne__(self,other):
        teller_s=self.a*other.b
        teller_o=other.a*self.b
        return teller_s!=teller_o

    def __neg__(self):
        negatie=Breuk()
        negatie.a=-self.a
        negatie.b=self.b
        return negatie

    def __pos__(self):
        return self