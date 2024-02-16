#SimulacroParcial

#Realizar un programa que permita crear una empresa de Informática. 
#Las clases requeridas son: Empleado, Programador y Empresa.
#La clase Empleado debe tener los atributos nombre y sueldo.
#La clase Programador debe tener un constructor que reciba el lenguaje de programación que usa. 
#Además, tendrá un método para asignar un proyecto y otro método que devuelva el proyecto y el lenguaje.
#La clase Empresa es la principal, se deben usar estas listas con los siguientes datos:

"""listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
listaProgramadores = []"""

"""Se debe usar un constructor que reciba nombre y rubro y otro método que devuelva esos mismos datos.
El método central de la clase Empresa es agEmp, que sirve para agregar empleados. En este método se preguntará qué lenguaje maneja el empleado, se debe verificar que dicho lenguaje esté entre los necesarios (son los que están en listaLenguajes) y en caso de ser así se procede a instanciar el nuevo programador. 
Se solicitará su nombre y se le asignará un salario de 1.475.000 pesos si su lenguaje es Python o bien de 615.000 pesos si maneja alguno de los otros tres. 
Luego se elegirá un proyecto (de los dos que están en listaProyectos) y finalmente se incorporará al nuevo programador a listaProgramadores.
En el caso de que el lenguaje conocido NO sea uno de los requeridos, debe mostrarse un mensaje que diga que no se necesita y mostrar la lista de lenguajes.
El último método de la clase Empresa es mostrarTodo, que devuelve por pantalla el nombre de la firma, el rubro y cada empleado con su nombre, salario, proyecto y lenguaje utilizado.

Datos de prueba:
C# - Pedro - "Sistema Gallina SRL"
Python - Pablo - "Web Pollitos"
Ruby - Salvador  - "Web Pollitos"
JavaScript - Ana - "Web Pollitos"

Salida esperada:
Empresa: Google. Rubro: Informática
Programadores:
Pedro. Salario: 615000. Sistema: Gallina SRL. Lenguaje: C#
Pablo. Salario: 1475000. Sistema: Web Pollitos. Lenguaje: Python
Ana.  Salario: 615000. Sistema: Web Pollitos. Lenguaje: JavaScript
"""

class Empleado:
    def __init__(self,nombre,sueldo) -> None:
       self.nombre=nombre
       self.sueldo=sueldo

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje) -> None:
        super().__init__(nombre, sueldo)
        self.lenguaje=lenguaje

    def asignarProyecto(self, proyecto):
        self.proyecto=proyecto

    def __str__(self) -> str:
        return f"{self.nombre}. Salario: {self.sueldo}. Proyecto: {self.proyecto}. Lenguaje: {self.lenguaje}."


class Empresa:
    def __init__(self, firma, rubro) -> None:
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []
        self.firma=firma
        self.rubro=rubro

    def getFirmaRubro(self) -> str:
        return f"Firma de la empresa: {self.firma}. Rubro: {self.rubro}."
    
    def agEmp(self):
        lenguaje=input("Que lenguaje maneja?: ")
        if lenguaje in self.listaLenguajes:
            nombre=input("Ingrese su nombre: ")
            sueldo = 1475000 if lenguaje == "Python" else 615000
            programador1=Programador(nombre, sueldo, lenguaje)
            proyecto=input(f"Elija un proyecto entre {self.listaProyectos}: ") 
            programador1.asignarProyecto(proyecto)
            self.listaProgramadores.append(programador1)
        else:
            print(f"Error--Los lenguajes que se necesitan son: {self.listaLenguajes}")

    def mostrarTodo(self):
        print(f" Empresa: {self.firma}. Rubro: {self.rubro}.")
        for programador in self.listaProgramadores:
            print (f"Empleado: {programador}.")
    
                     
empresa = Empresa("Google", "Informática")

for x in range (4):
    empresa.agEmp()


empresa.mostrarTodo()
                     




