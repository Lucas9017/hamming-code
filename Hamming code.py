class Matrix:
    def __init__(self, elementen = [], kolommen = 0):
        self.elementen = elementen
        self.kolommen = kolommen
    
    def isMatrix(self):
        if isinstance(self,Matrix) and len(self.elementen) % self.kolommen == 0 and isinstance(self.kolommen, int):
            return True
        else:
            return False

    def __str__(self):
        if self.isMatrix():
            return str(self.elementen) + ', ' + str(self.kolommen)
        else:
            raise TypeError('input is geen matrix')

    def __add__(self,other):
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            som = self
            for i in range(0,len(self.elementen)):
                som.elementen[i]= self.elementen[i] + other.elementen[i]
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return som

    def __sub__(self,other):
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            verschil = self
            for i in range(0,len(self.elementen)):
                verschil.elementen[i]= self.elementen[i] - other.elementen[i]
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return verschil

    def __mul__(self,other):
        if self.isMatrix() and other.isMatrix():
            product = Matrix()
            m = len(self.elementen) // self.kolommen #Aantal rijen self
            n = self.kolommen
            p = other.kolommen
            if n == len(other.elementen) // other.kolommen: #Afmetingen kloppen dus de matrices kunnen met elkaar vermenigvuldigd worden
                for i in range(1,m+1):
                    for j in range(1,p+1):
                        resultaat = 0
                        for k in range(1,n+1):
                            resultaat += self.elementen[(i-1)*n+k-1] * other.elementen[(k-1)*p+j-1]
                        product.elementen.append(resultaat)
                product.kolommen = p
            else:
                raise TypeError('de matrices hebben niet de juiste afmetingen')
        else:
            raise TypeError('De input zijn geen matrices')
        return product

    def __eq__(self,other):
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0, len(self.elementen)):
                if self.elementen[i] != other.elementen[i]:
                    return False
            return True
        else:
            return False

    def __ne__(self,other):
        if self == other:
            return False
        else:
            return True
        
    def __pos__(self):
        if self.isMatrix():
            return self

    def __neg__(self):
        if self.isMatrix():
            negatie = self
            for i in range(0, len(self.elementen)):
                negatie.elementen[i] = -1 * self.elementen[i]
            return negatie