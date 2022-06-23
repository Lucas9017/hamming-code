import random
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
    
def nibbles(input):
    '''
    Geeft een lijst terug, waarin lijsten van nibbles van vier bits staan
        Invoer: input: een string
        Uitvoer: lijst: lijst van lijsten van telkens vier bits. Elke acht bits 
                 representeren één karakter van invoer
    '''
    binair=''
    for i in input:
        x=decimaalBinair(ord(i))
        #we zetten het decimale ASCII getal van het karakter uit de string om in binaire taal
        l=8-len(x)
        if l==0:
            binair+=x
        else:
            binair+='0'*l+x
        #we zorgen ervoor dat elk karakter door een binair getal van lengte 8 wordt gerepresenteert
    lengte=len(binair)
    lijst=[[] for i in range(0,lengte,4)]
    for i in range(len(lijst)):
        for j in range(0,4):
            lijst[i]+=[int(binair[i*4+j])]
    #we zetten elke 4 bits in een lijst, die lijsten zetten we weer in een overkoepelende lijst
    return lijst

def parity_lijst(input):
    '''
    Geeft een lijst van lijsten terug, waarin de pariteitsvectoren zijn verwerkt
        Invoer: input: een lijst van lijsten van lengte 4
        Uitvoer: lijst: een lijst van lijsten van lengte 7, waarin de pariteitsbits
                 van de nibbles van input zijn verwerkt    
    '''
    lijst=[]
    for i in range(len(input)):
        #we bepalen de pariteitsbits met de bits waardoor deze gerepresenteerd wordt
        p1=input[i][0]^input[i][1]^input[i][3]
        p2=input[i][0]^input[i][2]^input[i][3]
        p3=input[i][1]^input[i][2]^input[i][3]
        lijst+=[[p1,p2,input[i][0],p3,input[i][1],input[i][2],input[i][3]]]
        #we vullen een lege lijst met lijsten waarin 7 bits staan:
            #drie pariteitsbits en 4 boodschaps-bits op de goede volgorde
    return lijst

def check_correct(input):
    '''
    Geeft een lijst van lijsten terug waarin de lijsten zijn gecontroleerd en
    verbeterd met behulp van de pariteitsbits.
        Invoer: input: een lijst van lijsten van lengte 7
        Uitvoer: lijst: een lijst van lijsten van lengte 7
    '''
    lijst=[]
    for i in range(len(input)):
        #we controleren of de pariteiten nog steeds klopt voor de drie pariteitsbits
        p1=input[i][0]^input[i][2]^input[i][4]^input[i][6]
        p2=input[i][1]^input[i][2]^input[i][5]^input[i][6]
        p3=input[i][3]^input[i][4]^input[i][5]^input[i][6]
        if p1==0 and p2==0 and p3==0:
            #als de pariteit klopt, is er waarschijnlijk geen fout opgetreden
            lijst+=[input[i]]
        else:
            #als er wel een fout is, moeten we de foute bit aanpassen
            plek=binairDecimaal(str(p3)+str(p2)+str(p1))-1
            input[i][plek]=input[i][plek]^1
            lijst+=[input[i]]
    return lijst

def decodeer(input):
    '''
    Geeft een string van karakters terug die gerepresenteerd werd door alle bits 
    in de lijst van de input.
        Invoer: input: een lijst van lijsten van lengte 7
        Uitvoer: uitvoer: een string waarvan de karakters bepaald worden door alle
                 boodschapsbits uit input
    '''
    string=''
    uitvoer=''
    for i in range(len(input)):
        #we gebruiken de boodschaps-bits om de ontvangen boodschap te bepalen
        string+=str(input[i][2])+str(input[i][4])+str(input[i][5])+str(input[i][6])
    for i in range(0,len(string),8):
        #elke 8 bits representeren één karakter uit de string
        uitvoer+=chr(binairDecimaal(string[i:i+8]))
    return uitvoer

def random_verandering(input,aantal):
    '''
    Geeft een lijst van lijsten terug, waarvan een aantal elementen van die lijsten 
    willekeurig veranderd zijn.
        Invoer: input: lijst van lijsten met lengte 7
                aantal: een positieve integer die het aantal fouten weergeeft
        Uitvoer: ontvangst: lijst van lijsten met lengte 7 waarin aantal keer een 
                 bit geflipt is van input
    '''
    verstuur=input
    lijst=[]
    for i in range(len(verstuur)):
        #we zetten alle bits achter elkaar in een lijst
        lijst+=verstuur[i]
    lengte=len(lijst)
    #er wordt 'aantal' keer een willekeurig getal gekozen uit de totale lengte van de lijst
    k = random.sample(range(0,lengte),aantal)
    for j in k:
        #voor de gekozen willekeurige getallen, veranderen we de bits op die plek in de lijst
        lijst[j]=lijst[j]^1
    ontvangst=[]
    for i in range(0,lengte,7):
        #we zetten de lijst weer om in een lijst van lijsten van lengte 7
        ontvangst+=[list(lijst[i:i+7])]
    return ontvangst
        
def hamming(input,aantal):
    '''
    Geeft een boodschap terug die na het versturen door een communicatiekanaal
    met ruis is gecontroleerd op fouten en verbeterd is.
        Invoer: input: een string
                aantal: een positieve integer
        Uitvoer: er wordt een string met de boodschap na de fouten geprint
                 d: een string
    '''
    if type(aantal)!=int or aantal<0:
        raise TypeError('Er is geen geldig aantal fouten opgegeven.')
    n=nibbles(str(input))
    v=parity_lijst(n)
    r=random_verandering(v,aantal)
    print('Uw boodschap na de fouten is:',decodeer(r))
    c=check_correct(r)
    d=decodeer(c)
    return d

def hamming_code():
    '''
    Geeft de hamming(input,aantal) code terug, na eerst om input gevraagd te hebben
        Invoer: code: een string
                aantal: een positieve integer
        Uitvoer: hamming(code,aantal): de functie hamming wordt uitgevoerd met 
                 code en aantal.
    '''
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
    return hamming(code,aantal)