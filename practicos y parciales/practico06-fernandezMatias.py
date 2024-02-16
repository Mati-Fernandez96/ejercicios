class Animal():
    def __init__(self, id, peso) -> None:
        self.id = id
        self.peso = peso
    
    def salud(self, pesoSano):
        return 'sano' if self.peso >= pesoSano else 'enfermo' 

class Puma(Animal):
    def __init__(self, id, peso,edad) -> None:
        super().__init__(id, peso)
        self.edad = edad
        self.pesoSano = 200
    
    def esAdulto(self):
        if self.edad >= 5:
            return True

    def __str__(self):
        return f"# {self.id} - {self.salud(self.pesoSano)}"    
   
class Venado(Animal):
    def __init__(self, identificador, peso) -> None:
        super().__init__(identificador, peso)            
        self.pesoSano = 120

    def __str__(self):
        return f"# {self.id} - {self.salud(self.pesoSano)}"    

class Jaula():
    def __init__(self, animal, cantidad) -> None:
        self.listaAnimales = []
        self.animal = animal
        if animal == "Pumas":
            datosPumas = [(230, 6), (180, 4), (210, 7), (190, 10)]
            for i,elemento in enumerate(datosPumas,start = 1):
                puma = Puma(i,elemento[0],elemento[1])
                self.listaAnimales.append(puma)
        else:
            datosVenados = [100,130]
            for i,elemento in enumerate(datosVenados,start = 1):
                venado = Venado(i,elemento)
                self.listaAnimales.append(venado)

    def cantidadAdultos(self):
        c = 0
        for puma in self.listaAnimales:
            if puma.esAdulto():
                c += 1
        return c

    def datos(self):
        print()
        print(f'Jaula de {self.animal}')
        for elemento in self.listaAnimales:
            print(elemento)
        if self.animal == 'Pumas':
            print(f'Cantidad de adultos: {self.cantidadAdultos()}')        

jaulaPumas = Jaula("Pumas",4)
jaulaPumas.datos()
jaulaVenados = Jaula("Venados",2)
jaulaVenados.datos()