class Matrix:
    def __init__(self, elementen = [0], kolommen = 1):
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
            print(som.elementen)
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return som

    __radd__ = __add__ #vgm kunnen we dit weghalen ,omdat we alleen matrices met elkaar op kunnen tellen en niet een matrix met een int bijv

    def __sub__(self,other):
        verschil = Matrix()
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0,len(self.elementen)):
                verschil.elementen.append(self.elementen[i] - other.elementen[i])
            verschil.kolommen = self.kolommen
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return verschil

    __rsub__ = __sub__  #vgm kunnen we dit weghalen omdat we alleen matrices van elkaar af kunnen halen en niet een matrix van een int af bijv

    def __mul__(self,other):
        product = Matrix()
        if self.isMatrix() and isinstance(other,int):
            m=len(self.elementen)
            for i in range(0,m):
                product.elementen.append(self.elementen[i]*other)
                product.kolommen=self.kolommen
        elif self.isMatrix() and other.isMatrix():
            m = len(self.elementen) // self.kolommen
            n = self.kolommen
            p = other.kolommen
            print(product)
            if n == len(other.elementen) // other.kolommen:
                for i in range(0,m):
                    for j in range(0,p):
                        resultaat = 0
                        for k in range(0,n):
                            resultaat += self.elementen[i*n+k] * other.elementen[j+k*p]
                        product.elementen.append(resultaat%2)
                        print(product.elementen)
                product.kolommen=other.kolommen
            else:
                raise TypeError('de matrices hebben niet de juiste afmetingen')
        return product

    __rmul__=__mul__ #deze moet wel blijven staan omdat je een matrix met int kan vermenigvuldigen
    
    def __eq__(self,other):
        if len(self.elementen)!=len(other.elementen) or self.kolommen!=other.kolommen:
            return False
        else:
            for i in range(len(self.elementen)):
                if self.elementen[i]!=other.elementen[i]:
                    return False
            return True
    
    def __neq__(self,other):
        if len(self.elementen)!=len(other.elementen) or self.kolommen!=other.kolommen:
            return True
        else:
            for i in range(len(self.elementen)):
                if self.elementen[i]!=other.elementen[i]:
                    return True
            return False
    
def nibbles(input):
    binair=''
    for i in input:
        binair+=bin(ord(i))[2:]
    lengte=len(binair)
    if lengte%4==1: #ik heb dit hier even gezet omdat we anders een error kregen als de lengte van de binaire code niet deelbaar was door 4
        binair+='000'
    elif lengte%4==2:
        binair+='00'
    elif lengte%4==3:
        binair+='0'
    lengte=len(binair)
    lijst=[[] for i in range(0,lengte,4)]
    for i in range(len(lijst)):
        for j in range(0,4):
            lijst[i].append(int(binair[i*4+j]))
    return lijst

def parity_vector(input):
    lijst=nibbles(input)
    print(lijst)
    G=Matrix([1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1],4)
    for i in range(len(lijst)):
        print(lijst[i])
        x=Matrix(lijst[i],1)
        lijst[i]=G*x
        print('G*x=',str(G*x))
        print(type(lijst[i]))
    return lijst

def parity_check(input):
    lijst=parity_vector(input)
    print(lijst)
    H=Matrix([1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1],7)
    for i in range(len(lijst)):
        print(lijst[i])
        lijst[i]= H*lijst[i]
    return lijst
        
def correct(input):
    lijst_check=parity_check(input)
    lijst_vector=parity_vector(input)
    for i in range(len(lijst_check)):
        if lijst_check[i]!=Matrix([0,0,0],1):
            plek0=str(lijst_check[i].elementen[0])
            plek1=str(lijst_check[i].elementen[1])
            plek2=str(lijst_check[i].elementen[2])
            plek=plek0*(4)+plek1*(2)+plek2*1
            lijst_vector[i][plek]=(lijst_vector[i][plek]+1)%2
    return lijst_vector
      
def decodeer(input):
    lijst=correct(input)
    R=Matrix([0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],7)
    for i in range(len(lijst)):
        x=R*lijst[i]
        x=[str(element) for element in x]
        lijst[i]=''.join(x)
    lijst=[element for element in lijst]
    binair_rij=int(''.join(lijst))
    n=len(binair_rij)//7
    binair=binair_rij[:n]
    uitvoer=''
    for i in range(0,len(binair),7):
        uitvoer+=chr(binair[i]*64+binair[i+1]*32+binair[i+2]*16+binair[i+3]*8+binair[i+4]*4+binair[i+5]*2+binair[i+6]*1)
        