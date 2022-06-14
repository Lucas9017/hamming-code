class Matrix:
    def __init__(self, matrix = [[1]]):
        self.matrix = matrix

    def __str__(self):
        i = 1
        while i < len(self):
            if len(self[0]) == len(self[i]):
                i += 1
            else:
                raise TypeError('input is geen matrix')
        return self

    def __add__(self,other):
        som = Matrix()
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if len(self) == len(other) and len(self[0]) == len(other[0]):
                self + other
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return som.vereenvoudigBreuk()

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

    def __truediv__(self,other):
        tquotient=Breuk()
        if isinstance(self,Breuk) and isinstance(other,Breuk):
            tquotient.a=self.a*other.b
            tquotient.b=self.b*other.a
        elif isinstance(self,Breuk) and isinstance(other,int):
            tquotient.a=self.a
            tquotient.b=self.b*other
        else:
            raise TypeError("/: alleen breuken, integers")
        return tquotient.vereenvoudigBreuk()

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
        
def check(rooster, plaats, getal):
    vierkantjes={0:5,1:4,2:7,3:6,4:1,5:0,6:3,7:2,8:13,9:12,10:15,11:14,12:9,13:8,14:11,15:10}
    rij=plaats//4
    kolom=plaats%4

    for n in range(4):
        if rooster[rij*4+n]==getal:
            return False
      
        if rooster[kolom+n*4]==getal:
            return False

        if rooster[vierkantjes[plaats]]==getal:
            return False
    return True

def verander(rooster):
    if not 0 in rooster:
        return True

    for i in range(16):
        if rooster[i]==0:
            for getal in range(1,5):
                if check(rooster,i,getal)==True:
                    rooster[i]=getal
                    if verander(rooster)==True:
                        return True

                    rooster[i]=0
            return False

def los_op(rooster):
    if verander(rooster)==True:
        return rooster