import random
class Matrix:
    '''
    Een klasse om Matrices te definiëren
    We werken met matrices modulo 2 dus alle getallen in de matrices zijn ofwel 0 ofwel 1
    
    De attributen zijn een lijst van elementen en een positief geheel getal dat
    het aantal kolommen representeert.
    '''
    def __init__(self, elementen = [], kolommen = 1):
        self.elementen = elementen #De getallen van de matrix als lijst met gehele getallen
        self.kolommen = kolommen #Aantal kolommen van de matrix
    
    def isMatrix(self):
        '''
        Controleert of de invoer een matrix kán zijn, dus of de matrix überhaupt 
        in de klasse Matrix zit, of het aantal kolommen overeenkomt met het aantal 
        elementen, en of de elementen gehele getallen zijn.
            Invoer: alles kan ingevoerd worden
            Uitvoer: boolean True of False
        '''
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
        '''
        Print de matrix in lijst vorm met het aantal kolommen er naast.
            Invoer: self: een element uit de klasse Matrix
            Uitvoer: str: de lijst met de elementen van de matrix, waarnaast het aantal
                     kolommen wordt geprint.
        '''
        if self.isMatrix():
            output = Matrix([],1)
            for i in range(0, len(self.elementen)):
                output.elementen.append(self.elementen[i] % 2)
            output.kolommen = self.kolommen
            return str(output.elementen) + ', ' + str(output.kolommen)
        else:
            raise TypeError('input is geen matrix')

    def __add__(self,other):
        '''
        Geeft de optelling van twee matrices terug.
            Invoer: self: een element van de klasse Matrix
                    other: een element van de klasse Matrix
                    de matrices moeten evenveel elementen bevatten en evenveel kolommen hebben
            Uitvoer: som: de som van de matrices self en other
        '''
        som = Matrix([],1)
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0,len(self.elementen)):
                som.elementen.append((self.elementen[i] + other.elementen[i]) % 2)
            som.kolommen = self.kolommen
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return som

    def __sub__(self,other):
        '''
        Geeft het verschil van twee matrices terug.
            Invoer: self: een element van de klasse Matrix
                    other: een element van de klasse Matrix
            Uitvoer: verschil: het verschil van de matrices self en other
        '''
        verschil = Matrix([],1)
        if self.isMatrix() and other.isMatrix() and len(self.elementen) == len(other.elementen) and self.kolommen == other.kolommen:
            for i in range(0,len(self.elementen)):
                verschil.elementen.append((self.elementen[i] - other.elementen[i]) % 2)
            verschil.kolommen = self.kolommen
        else:
            raise TypeError('de matrices hebben niet de juiste afmetingen')
        return verschil

    def __mul__(self,other):
        ''' 
        Geeft het product van twee matrices terug.
            Invoer: self: een element van de klasse Matrix
                    other: een element van de klasse Matrix
            Uitvoer: product: het product van de matrices self en other
        '''
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
        '''
        Controleert of twee matrices gelijk aan elkaar zijn.
            Invoer: self: een element uit de klasse Matrix
                    other: een element uit de klasse Matrix
            Uitvoer: boolean True of False
        '''
        if len(self.elementen)!=len(other.elementen) or self.kolommen!=other.kolommen:
            return False
        else:
            for i in range(0,len(self.elementen)):
                if (self.elementen[i] % 2 ) != (other.elementen[i] % 2):
                    return False
            return True
    
    def __neq__(self,other):
        '''
        Controleert of twee matrices ongelijk aan elkaar zijn.
            Invoer: self: een element van de klasse Matrix
                    other: een element van de klasse Matrix
                Uitvoer: boolean True of False
        '''
        if len(self.elementen)!=len(other.elementen) or self.kolommen!=other.kolommen:
            return True
        else:
            for i in range(0, len(self.elementen)):
                if (self.elementen[i] % 2) != (other.elementen[i] % 2):
                    return True
            return False
        
    def __pos__(self):
        '''
        Geeft de positieve van de matrix terug.
            Invoer: self: een element van de klasse Matrix
            Uitvoer: positief: de positieve van self
        '''
        if self.isMatrix():
            positief = Matrix([],1)
            for i in range(0, len(self.elementen)):
                positief.elementen.append(self.elementen[i] % 2)
            positief.kolommen = self.kolommen
            return positief
    
    def __neg__(self):
        '''
        Geeft het negatieve van de matrix terug.
            Invoer: self: een element van de klasse Matrix
            Uitvoer: negatie: de negatie van self
        '''
        if self.isMatrix():
            negatie = Matrix([],1)
            for i in range(0, len(self.elementen)):
                negatie.elementen.append((-1 * self.elementen[i] % 2))
            negatie.kolommen = self.kolommen
            return negatie
        
def decimaalBinair(decimaal):
    '''
    Geeft een binair getal terug wat equivalent is aan het decimaal getal
        Invoer: decimaal: een decimaal integer
        Uitvoer: tekst: het binaire getal wat decimaal representeert    
    '''
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
    '''
    Geeft een decimaal getal terug wat equivalent is aan het binaire getal
        Invoer: binair: een binair getal, beginnend met 1
        Uitvoer: decimaal: het decimale getal wat binair representeert
    '''
    lijst = [int(x) for x in str(binair)]
    decimaal = 0
    for i in range(0,len(lijst)):
        decimaal += lijst[i] * 2**(len(lijst)-i-1)
    return decimaal

def splitsen(input,m):
    '''
    Geeft een lijst terug, waarin lijsten van bineaire code van 2^m-m-1 bits staan
        Invoer: input: een string
        Invoer: m: het getal m dat aangeeft dat we Hamming(2^m-1,2^m-m-1)code gebruiken
        Uitvoer: lijst: lijst van lijsten van telkens vier bits. Elke acht bits 
                 representeren één karakter van invoer
    '''
    binair=''
    for i in input:
        x=decimaalBinair(ord(i))
        l=8-len(x)
        if l==0:
            binair += x
        else:
            binair += '0'*l+x
    
    n = 2**m-m-1
    while len(binair) % n != 0:
        binair = binair + '0'
    lengte = len(binair)
    lijst=[[] for i in range(0,lengte,n)]
    for i in range(len(lijst)):
        for j in range(0,n):
            lijst[i] += [int(binair[i*n+j])]
    return lijst

def parity_vector(input,m):
    '''
    Geef een lijst van vectoren terug, waarin pariteitsbits zijn verwerkt
        Invoer: input: een lijst van lijsten van lengte 2^m-m-1
        Invoer: m: het getal m dat aangeeft dat we Hamming(2^m-1,2^m-m-1)code gebruiken
        Uitvoer: lijst: een lijst van vectoren van lengte 2^m-1 terug, waarin
                 de pariteitsbits van de nibbles van input zijn verwerkt    
    '''
    lijst=[]
    if m == 3:
        G=Matrix([1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1],4)
    elif m == 4:
        G = Matrix([1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],11)
    else:
        raise TypeError('Voor m=' + str(m) + ' hebben we geen code geschreven.')
    for i in range(len(input)):
        x=Matrix(input[i],1)
        lijst+=[G*x]
    return lijst

def parity_check(input,m):
    '''
    Geeft een lijst van vectoren terug, welke zijn gecheckt op fouten m.b.v. de pariteitsbits
        Invoer: input: lijst van vectoren van lengte 2^m-1, met pariteitsbits
        Invoer: m: het getal m dat aangeeft dat we Hamming(2^m-1,2^m-m-1)code gebruiken
        Uitvoer: lijst: lijst van vectoren van lengte m, die aangeeft of er fouten in het ontvangen bericht zitten en waar die fouten zitten
    '''
    lijst=[]
    if m == 3:
        H=Matrix([1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1],7)
    elif m == 4:
        H = Matrix([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],15)
    else:
        raise TypeError('Voor m=' + str(m) + ' hebben we geen code geschreven.')
        
    for i in range(len(input)):
        lijst+=[H*input[i]]
    return lijst
        
def correct(vector,check,m):
    '''
    Corrigeerd de fouten die zijn aanstaan tijdens het versturen van het bericht
        Invoer: vector: lijst van matrices, elke matrix is een vector waar eventueel fouten inzitten
        Invoer: check: lijst van matrices, elke matrix is een vector die aangeeft waar de fout zit als er een fout in het ontvangen bericht zit
        Invoer: m: het getal m dat aangeeft dat we Hamming(2^m-1,2^m-m-1)code gebruiken
        Uitvoer: lijst_vector: lijst van matrices, elke matrix is een vector waarin de eventuele fouten zijn verbeterd
    '''
    lijst_check=check
    lijst_vector=vector
    elementenNulmatrix = []
    for i in range(0,m):
        elementenNulmatrix.append(0)
    nulmatrix = Matrix(elementenNulmatrix,1) #De nulmatrix met m rijen en 1 kolom
    
    for i in range(len(lijst_check)):
        if lijst_check[i] != nulmatrix:
            plek0=int(lijst_check[i].elementen[0])
            plek1=int(lijst_check[i].elementen[1])
            plek2=int(lijst_check[i].elementen[2])
            if m == 3:
                plek=binairDecimaal(str(plek2)+str(plek1)+str(plek0))-1
                lijst_vector[i].elementen[plek]=(lijst_vector[i].elementen[plek]+1)%2
            elif m == 4:
                plek3=int(lijst_check[i].elementen[3])
                plek=binairDecimaal(str(plek3)+str(plek2)+str(plek1)+str(plek0))-1
                lijst_vector[i].elementen[plek]=(lijst_vector[i].elementen[plek]+1)%2
    return lijst_vector
      
def decodeer(input,m):
    '''
    Decodeert het bericht waardoor de ontvanger de boodschap kan lezen
        Invoer: input: lijst van matrices, elke matrix is een vector van 2^m-1 bits
        Invoer: m: het getal m dat aangeeft dat we Hamming(2^m-1,2^m-m-1)code gebruiken
        Uitvoer: uitvoer: de tekst die we krijgen als we de input hebben gedecodeerd
    '''
    lijst=[]
    if m == 3:
        R = Matrix([0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],7)
    elif m == 4:
        R = Matrix([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],15)
    for i in range(len(input)):
        x=R*input[i]
        x=[str(element) for element in x.elementen]
        lijst+=[''.join(x)]
    lijst=[element for element in lijst]
    binair_rij=''.join(lijst)
    binair=str(binair_rij)
    lengte=len(binair)//8
    uitvoer=''
    for i in range(0,lengte*8,8):
        uitvoer+=chr(binairDecimaal(binair[i:i+8]))
    return uitvoer

def random_verandering(input,aantal,m):
    '''
    Zorgt voor fouten bij het versturen, op willekeurige plaatsen worden nullen veranderd in enen en andersom 
        Invoer: input: lijst van matrices, elke matrix is een vector van 2^m-1 bits
        Invoer: aantal: het aantal fouten dat moet optreden bij het verzenden van het bericht
        Invoer: m: het getal m dat aangeeft dat we Hamming(2^m-1,2^m-m-1)code gebruiken
        Uitvoer: uitvoer: de tekst die we krijgen als we de input hebben gedecodeerd
    '''
    verstuur=input
    lijst=[]
    for i in range(len(verstuur)):
        lijst+=list(verstuur[i].elementen)
    lengte=len(lijst)
    k = random.sample(range(0,lengte),aantal)
    for j in k:
        lijst[j]=(int(lijst[j])+1)%2
        
    ontvangst=[]
    for i in range(0,lengte,2**m-1):
        elementen = []
        for j in range(0,2**m-1):
            elementen.append(lijst[i+j])
        ontvangst += [Matrix(elementen, 1)]
    return ontvangst
        
def hamming(input,aantal,m):
    '''
    In een boodschap worden een aantal fouten gemaakt en door het hammingcode algoritme verbeterd
        Invoer: input: string, tekst die we willen versturen
        Invoer: aantal: het aantal fouten dat we in het verzonden bericht willen hebben
        Invoer: m: het getal m dat aangeeft dat we Hamming(2^m-1,2^m-m-1)code gebruiken (dit werkt alleen voor m=3 en m=4)
        Uitvoer: d: de tekst die we krijgen als we de input hebben verzonden en verbeterd
    '''
    if type(aantal)!=int or aantal<0:
        raise TypeError('Er is geen geldig aantal fouten opgegeven')
    n=splitsen(str(input),m)
    v=parity_vector(n,m)
    r=random_verandering(v,aantal,m)
    print('Uw boodschap na de fouten is:',decodeer(r,m))
    c=parity_check(r,m)
    cor=correct(r,c,m)
    d=decodeer(cor,m)
    return d

def hamming_code(): #Hamming(7,4)code
    code=str(input('Wat wilt u versturen? '))
    binair=''
    for i in code:
        x=decimaalBinair(ord(i))
        l=8-len(x)
        if l==0:
            binair+=x
        else:
            binair+='0'*l+x
    hvh=len(binair)//4
    lengte=hvh*7
    aantal=int(input('Uw boodschap bevat '+str(lengte )+' bits. Hoeveel fouten moeten er ontstaan in deze bits bij het versturen? '))
    if aantal>lengte:
        raise TypeError('Er is geen geldig aantal fouten opgegeven.')
    return hamming(code,aantal,3)