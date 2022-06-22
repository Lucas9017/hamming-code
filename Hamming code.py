import random
class Matrix: #De getallen van de matrix behandelen we modulo 2
    def __init__(self, elementen = [], kolommen = 1):
        self.elementen = elementen #De getallen van de matrix als lijst met gehele getallen
        self.kolommen = kolommen #Aantal kolommen van de matrix
    
    def isMatrix(self):
        if isinstance(self,Matrix) and len(self.elementen) % self.kolommen == 0 and isinstance(self.kolommen, int):
            for i in range(0, len(self.elementen)):
                if isinstance(self.elementen[i], int):
                    continue
                else:
                    return False
            return True
        else:
            return False

    def __str__(self):
        if self.isMatrix():
            output = Matrix([],1)
            for i in range(0, len(self.elementen)):
                output.elementen.append(self.elementen[i] % 2)
            output.kolommen = self.kolommen
            return str(output.elementen) + ', ' + str(output.kolommen)
        else:
            raise TypeError('input is geen matrix')

    def __add__(self,other):
        som = Matrix([],1)
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0,len(self.elementen)):
                som.elementen.append((self.elementen[i] + other.elementen[i]) % 2)
            som.kolommen = self.kolommen
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return som

    def __sub__(self,other):
        verschil = Matrix([],1)
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0,len(self.elementen)):
                verschil.elementen.append((self.elementen[i] - other.elementen[i]) % 2)
            verschil.kolommen = self.kolommen
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return verschil

    def __mul__(self,other):
        product = Matrix([],1)
        if self.isMatrix() and isinstance(other,int): #Vermenigvuldigen matrix met geheel getal
            for i in range(0,len(self.elementen)):
                product.elementen.append((self.elementen[i] * other) % 2)
        elif self.isMatrix() and other.isMatrix(): #Vermenigvuldigen van twee matrices
            m = len(self.elementen) // self.kolommen #Aantal rijen van self
            n = self.kolommen
            p = other.kolommen
            if n == len(other.elementen) // other.kolommen:
                for i in range(0,m):
                    for j in range(0,p):
                        resultaat = 0
                        for k in range(0,n):
                            resultaat += self.elementen[i*n+k] * other.elementen[k*p+j] #De som van rij i van self met kolom j van other
                        product.elementen.append(resultaat % 2)
                product.kolommen = p
            else:
                raise TypeError('de matrices hebben niet de juiste afmetingen')
        else:
            raise TypeError('De input zijn geen matrices')
        return product

    __rmul__=__mul__
    
    def __eq__(self,other):
        if len(self.elementen)!=len(other.elementen) or self.kolommen!=other.kolommen:
            return False
        else:
            for i in range(0,len(self.elementen)):
                if (self.elementen[i] % 2 ) != (other.elementen[i] % 2):
                    return False
            return True
    
    def __neq__(self,other):
        if len(self.elementen)!=len(other.elementen) or self.kolommen!=other.kolommen:
            return True
        else:
            for i in range(0, len(self.elementen)):
                if (self.elementen[i] % 2) != (other.elementen[i] % 2):
                    return True
            return False
        
    def __pos__(self):
        if self.isMatrix():
            positief = Matrix([],1)
            for i in range(0, len(self.elementen)):
                positief.elementen.append(self.elementen[i] % 2)
            positief.kolommen = self.kolommen
            return positief
    
    def __neg__(self):
        if self.isMatrix():
            negatie = Matrix([],1)
            for i in range(0, len(self.elementen)):
                negatie.elementen.append((-1 * self.elementen[i] % 2))
            negatie.kolommen = self.kolommen
            return negatie
        
        
def decimaalBinair(decimaal):
    if decimaal == 0:
        return 0
    else:
        binair = []
        while decimaal > 0:
            if decimaal % 2 == 0:
                binair.append(0)
                decimaal = decimaal // 2
            else:
                binair.append(1)
                decimaal = decimaal // 2
        
        tekst = ""
    for i in range(0,len(binair)): 
        tekst += str(binair[len(binair)-i-1])
    return tekst

def binairDecimaal(binair):
    lijst = [int(x) for x in str(binair)]
    decimaal = 0
    for i in range(0,len(lijst)):
        decimaal += lijst[i] * 2**(len(lijst)-i-1)
    return decimaal
    
def nibbles(input):
    binair=''
    for i in input:
        x=decimaalBinair(ord(i))
        l=8-len(x)
        if l==0:
            binair+=x
        else:
            binair+='0'*l+x
    lengte=len(binair)
    lijst=[[] for i in range(0,lengte,4)]
    for i in range(len(lijst)):
        for j in range(0,4):
            lijst[i]+=[int(binair[i*4+j])]
    return lijst

def parity_vector(input):
    lijst=[]
    G=Matrix([1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1],4)
    for i in range(len(input)):
        x=Matrix(input[i],1)
        lijst+=[G*x]
    return lijst

def parity_check(input):
    lijst=[]
    H=Matrix([1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1],7)
    for i in range(len(input)):
        lijst+=[H*input[i]]
    return lijst
        
def correct(vector,check):
    lijst_check=check
    lijst_vector=vector
    for i in range(len(lijst_check)):
        if lijst_check[i]!=Matrix([0,0,0],1):
            plek0=int(lijst_check[i].elementen[0])
            plek1=int(lijst_check[i].elementen[1])
            plek2=int(lijst_check[i].elementen[2])
            plek=binairDecimaal(str(plek2)+str(plek1)+str(plek0))-1
            lijst_vector[i].elementen[plek]=(lijst_vector[i].elementen[plek]+1)%2
    return lijst_vector
      
def decodeer(input):
    lijst=[]
    R=Matrix([0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],7)
    for i in range(len(input)):
        x=R*input[i]
        x=[str(element) for element in x.elementen]
        lijst+=[''.join(x)]
    lijst=[element for element in lijst]
    binair_rij=''.join(lijst)
    binair=str(binair_rij)
    uitvoer=''
    for i in range(0,len(binair),8):
        uitvoer+=chr(binairDecimaal(binair[i:i+8]))
    return uitvoer

def random_verandering(input,aantal):
    verstuur=input
    lijst=[]
    for i in range(len(verstuur)):
        lijst+=list(verstuur[i].elementen)
    lengte=len(lijst)
    k = random.sample(range(0,lengte),aantal)
    for j in k:
        lijst[j]=(int(lijst[j])+1)%2
    ontvangst=[]
    for i in range(0,lengte,7):
        ontvangst+=[Matrix([lijst[i],lijst[i+1],lijst[i+2],lijst[i+3],lijst[i+4],lijst[i+5],lijst[i+6]],1)]
    return ontvangst
        
def hamming(input,aantal):
    if type(aantal)!=int:
        raise TypeError('Er is geen geldig aantal fouten opgegeven')
    n=nibbles(str(input))
    v=parity_vector(n)
    r=random_verandering(v,aantal)
    print('Uw boodschap na de fouten is: ',decodeer(r))
    c=parity_check(r)
    cor=correct(r,c)
    d=decodeer(cor)
    return d

def hamming_code():
    code=str(input('Wat wilt u versturen? '))
    binair=''
    for i in code:
        x=decimaalBinair(ord(i))
        l=8-len(x)
        if l==0:
            binair+=x
        else:
            binair+='0'*l+x
    lengte=len(binair)
    aantal=int(input('Uw boodschap bevat '+str(lengte )+' bits. Hoeveel fouten moeten er ontstaan in deze bits bij het versturen? '))
    return hamming(code,aantal)