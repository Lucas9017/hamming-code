class Matrix:
    def __init__(self, elementen = [1], kolommen = 1):
        self.elementen = elementen
        self.kolommen = kolommen

    def __str__(self):
        if self.elementen is list and len(self.elementen) % self.kolommen == 0:
            return self.elementen
        else:
            raise TypeError('input is geen matrix')

    def __add__(self,other):
        som = Matrix()
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            for i in range(0,len(self)):
                som.elementen[i] = self.elementen[i] + other.elementen[i]
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return som

    __radd__ = __add__

    def __sub__(self,other):
        verschil = Breuk()
        if isinstance(self,Breuk) and isinstance(other,Breuk):
            verschil.a = int(self.a * other.b - other.a * self.b)
            verschil.b = int(self.b * other.b)
        elif isinstance(self,Breuk) and isinstance(other,int):
            verschil.a=self.a-other*self.b
            verschil.b=self.b
        else:
            raise TypeError("-: alleen breuken, integer")
        return verschil.vereenvoudigBreuk()

    __rsub__ = __sub__  

    def __mul__(self,other):
        product=Breuk()
        if isinstance(self,Breuk) and isinstance(other,Breuk):
            product.a=self.a*other.a
            product.b=self.b*other.b
        elif isinstance(self,Breuk) and isinstance(other,int):
            product.a=self.a*other
            product.b=self.b
        else:
            raise TypeError("*: alleen breuken, integers")
        return product.vereenvoudigBreuk()

    __rmul__=__mul__
      

    def __rtruediv__(self,other):
        tquotient=Breuk()
        if isinstance(self,Breuk) and isinstance(other,int):
            tquotient.a=self.b*other
            tquotient.b=self.a
        else:
            raise TypeError("/: alleen breuken, integers")
        return tquotient.vereenvoudigBreuk()

    def __lt__(self,other):
        teller_s=self.a*other.b
        teller_o=other.a*self.b
        return teller_s<teller_o

    def __le__(self,other):
        teller_s=self.a*other.b
        teller_o=other.a*self.b
        return teller_s<=teller_o

    def __gt__(self,other):
        teller_s=self.a*other.b
        teller_o=other.a*self.b
        return teller_s>teller_o

    def __ge__(self,other):
        teller_s=self.a*other.b
        teller_o=other.a*self.b
        return teller_s>=teller_o

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

    def __abs__(self):
        if self.a<0:
            return -self
        elif self.a>=0:
            return self
        
