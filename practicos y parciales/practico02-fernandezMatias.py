personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell, StaUnitedtes(America),04-01-2000"
]

#Los apellidos de las personas nacidas antes de un año solicitado al usuario.

print("1)")

listaApellidos=[]

inicio=(input("desea realizar una busqueda de apellidos por año?:(si/no)"))

while inicio=="si":
    añoDeCorte=int(input("ingrese el año: "))
    for nombres in personas:
            recorteElemento=nombres.split(",")
            recorteAño=recorteElemento[2]
            separadorAño=recorteAño.split("-")
            añoNac=int(separadorAño[2])
            if añoDeCorte > añoNac:
                  recorteNombres= recorteElemento[0].split(" ")
                  apellido=recorteNombres[1]
                  listaApellidos.append(apellido)
                  
    print("los apellidos de las personas nacidas antes del año ingresado son: ", listaApellidos)
    inicio=int(input("desea realizar una busqueda de apellidos por año?:(si/no)"))        
        
print(añoNac)        

#La cantidad de personas nacidas en un país ingresado por el usuario.

print("2)")
cantPer=0
paisIngreso=input("ingrese un país con la primer letra en mayúscula: ") 

for persona in personas:
      recorteElemento=persona.split(",")
      continente=recorteElemento[1]
      pais=continente.split("(")[0]
      if paisIngreso==pais:
            cantPer+=1

print("La cantidad de personas nacidas en",paisIngreso, "es: ", cantPer)    

#El nombre de pila de la persona más joven de Europe.
edadMenor = 1000 # pongo un número alto para reemplazarlo seguro 

aH = 2023
mH = 5
dH = 22
personaMasJoven=[]


for persona in personas:
      recorteElemento=persona.split(",") #separo el elemento en Nombres, Ubicacion y Fecha de Nacimiento

      fecha=recorteElemento[2]  #De acá hasta la línea 72 obtengo la fecha de nacimiento separada en dia, mes y año
      separacionFecha=fecha.split("-")
      dN=int(separacionFecha[0])             
      mN=int(separacionFecha[1])
      aN=int(separacionFecha[2])  

      continente_y_pais=recorteElemento[1] #de acá hasta la linea 76 obtengo solo continente 
      busquedaContinente=continente_y_pais.split("(") 
      continente=busquedaContinente[0:-1] 

      nombreCompleto=recorteElemento[0] #obtencion nombre de pila
      separoNombre=nombreCompleto.split(" ")
      nombrePila=separoNombre[0]

      if continente=="Europe":
            edad = aH - aN
            if    (mN > mH) or (mN == mH and dN > dH):
                edad -= 1
            if edad < edadMenor:
                edadMenor = edad
                personaMasJoven = nombrePila

print('Persona más joven:', personaMasJoven)
        #No logre encontrar la logica para ubicar el algoritmo de edad
            


            

    
            



              
     
    
           
    
