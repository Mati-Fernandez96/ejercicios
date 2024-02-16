personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-02-1994",
    "Adeline LaPadula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-03-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,03-07-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]

#Quiero obtener:
#La cantidad de personas de Argentina
#La cantidad de personas de un país ingresado por el usuario 
#Las fechas de nacimiento de las personas cuyo apellido comience con una letra solicitada al usuario

print("1)")

def cant_personas_pais(pais="Argentina"):
    cantPais=0
    
    for nombres in personas:
        recorteElemento=nombres.split(",")
        recorteAño=recorteElemento[2]
        recorteNombres=recorteElemento[0]
        recortePais=recorteElemento[1]
        if recortePais == pais:
            cantPais = cantPais + 1
    return print(f"la cantidad de personas de {pais} son {cantPais}")

cant_personas_pais(pais="Argentina")
#Anda
print("2)")

def cant_personas_pais():
    cantPais=0
    listaOpciones=['Germany', 'United States', 'Norway', 'France']
    msj=print(f"opciones {listaOpciones}")
    userPais=input("Ingrese otro país además de Argentina: ")
    while userPais not in listaOpciones:
        print("Opcion invalida")
        userPais=input("Ingrese otro país además de Argentina: ")
    for elemento in personas:
        recorteElemento = elemento.split(",")
        recortePais = recorteElemento[1]
        if recortePais == userPais:
            cantPais = cantPais + 1
    print(f"La cantidad de personas de {userPais} es {cantPais}")

cant_personas_pais()   
#Anda

print("3)")

def nacimiento_letra_inicial():
    listaFechas=[]
    inicial=input("Ingrese una inicial de apellido: ")
    for elemento in personas: 
        recorteElemento=elemento.split(",") #separo los elementos
        fecha=recorteElemento[2] #obtengo solo fecha 
        apellido=recorteElemento[0].split(" ")[1] #tomo el elemento en la posicion de nombre y lo separo por el espacio, me quedo con la posicion 1 q es el apellido. 
        if inicial == apellido[0]: 
            listaFechas.append(fecha)
    print(f"las fechas de nacimiento de las personas que su apellido empieza con {inicial} son {listaFechas}")

nacimiento_letra_inicial()

#Anda