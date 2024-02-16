#Datos cargados en forma de listas paralelas.
nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 
sexos = ["f","f","m","f","m","f","m"]
fechas = [
"02/05/1943",
"07/09/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]
#Mostrar las iniciales de los nombres con un punto, luego un espacio 
#y finalmente el apellido completo de todas las personas.
print("1)")

for x in nombres:
    nombreSeparado = x.split(", ")
    apellido = nombreSeparado[0]
    nombrePila=nombreSeparado[1]

    print(nombrePila[0]+". "+apellido) 


#Decir cuál es el nombre de pila más largo
print("2)")

nombreMasLargo=""
for x in nombres:
    separador = x.split(", ")
    apellido = separador[0]
    nombrePila= separador[1]
    if len(nombrePila) > len(nombreMasLargo):
        nombreMasLargo=nombrePila

print("El nombre más largo es:", nombreMasLargo)
   
#Mostrar el promedio de edad de las mujeres. (Pueden usar el módulo edad.py que está subido en el Classroom)
print("3)")
aH = 2023
mH = 5
dH = 17
aN = 0
mN = 0
dN = 0

cantMujeres=0
edadAcumulada=0
for x in range(len(sexos)):
    cantMujeres += 1
    if sexos[x]=="f":
        dN = int(fechas[x][:2])
        mN = int(fechas[x][3:5])
        aN = int(fechas[x][6:])
        edad = aH - aN
        if (mN > mH) or ((mN == mH) and (dN > dH)):
            edad -= 1
        edadAcumulada += edad

print("el promedio de edad de las mujeres es de: ", edadAcumulada//cantMujeres)




