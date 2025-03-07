import os
os.system("cls")

#Descripcion:
#Este archivo tiene como objetivo exponer los conceptos de la programación orientada a objetos en Python de una forma
# sencilla y entendible.

#Como usar:
#El archivo se divide en secciones, cada sección explica un tema específico y tiene ejemplos.
#Para correr el código de cada ejemplo simplemente hay que eliminar o comentar las tres comillas (""") 
#Que están por encima y por debajo del código de la sección correspondiente.

#Indice
#-Seccion 1: introducción
#-Seccion 2: Objetos propios de python
#-Seccion 3: creación de clase
#-Seccion 4: explicación self
#-Seccion 5: métodos get y set
#-Seccion 6: métodos getter properties y setter properties
#-Seccion 7: métodos y atributos estáticos
#-Seccion 8: métodos privados
#-Seccion 9: Encapsulamiento
#-Seccion 10: Abstracción
#-Seccion 11: Herencia
#-Seccion 12: Polimorfismo










#Seccion 1: introducción-----------------------------------------------------------------------------------------
#La programación orientada a objetos se fundamenta en que todo lo que se pueda crear con código es un objeto
#y como tal tiene propiedades (en Python se suelen llamar atributos) y pueden realizar acciones (en Python se 
#suelen llamar métodos)
#Por ejemplo auto es un objeto, y tiene propiedades (color, modelo, patente) y 
#puede realizar acciones (encender, apagar, frenar)











#Seccion2 : Objetos propios de python----------------------------------------------------------------------------
"""
nombre="arturo" #Esto es una cadena de texto (es un objeto)
print(type(nombre))  #Con el comando type, Python nos dice a que clase pertenece (en este caso str).
print(nombre.upper()) #Los objetos de la clase str tienen un método por el cual se puede pasar todos sus caracteres a mayúscula.
print(nombre[0]) #Los objetos de la clase str tienen un primer elemento, un segundo etc (que corresponden sus caracteres)
"""
#Existen objetos propios de Python (se las llaman built-in) listas, funciones, cadenas de texto, etc y 
#objetos que podemos crear manualmente (en los cuales se enfoca esta guía).











#Seccion 3: creación de clase ------------------------------------------------------------------------------------
#Se puede entender una clase como un molde, y un objeto es una entidad perteneciente a una clase, 
#Las clases tienen definidas ciertos atributos y métodos, que luego los objetos pertenecientes a esas clases tendrán
#Por ejemplo, podríamos crear una clase que se llame "vehículo", y a partir de esa clase crear objetos, como "auto1" o
#"auto2" y ambos tienen los mismos métodos y propiedades, ya que esos quedan definidos por la clase ("vehículo"), 
#pero estos métodos pueden tener valores distintos, por ejemplo:
#Si la clase vehículo tiene una propiedad "peso", entonces el "peso" del "objeto" "auto1" puede ser 1.000 kg
#y el "peso" del "objeto" "auto2" puede ser 1.200 kg, además ambos "objetos" tendrán una propiedad "Arrancar".
#Recapitulando:
#clase >> vehículo.
#objeto >> auto1, auto2.
#atributo >> peso. 
#metodo >> arrancar.
"""
class perro(): #Creación clase perro
    
    #El método init es una convención que se usa para declarar/inicializar las propiedades del objeto.
    def __init__(self,nombre,raza,dueño):
        self.nombre=nombre #atributo
        self.raza=raza     #atributo
        self.dueño=dueño   #atributo


    def ladrar(self):       #método
        print("woof woof")
    
#Esto se entendería como:
#"Un perro tiene un nombre, una raza y un dueño, ademas el perro puede ladrar"


class dueño(): #Creación clase dueño
    def __init__(self,nombre,direccion,contacto):
        self.nombre=nombre
        self.direccion=direccion
        self.contacto=contacto

#Esto se entendería como:
#"Un dueño tiene un nombre, direccion y un contacto"

dueño1=dueño("Alberto","Antartida 225",2364588996) #Creación objeto dueño.
perro1=perro("Tornillo","Salchicha",dueño1) #Creación objeto perro.
 
#Podemos ver ciertas propiedades de los objetos dueño y perro
print(dueño1.direccion) #Se imprime la direccion del dueño Alberto
print(perro1.raza)  #Se imprime la raza del perro Tornillo

#Ademas algun metodo

perro1.ladrar() #En esta linea de código, hacemos que tornillo ladre.
"""








#Seccion 4: explicación self ------------------------------------------------------------------------------------
#Como los objetos son una "Copia" de la clase, al heredar (se verá el concepto herencia más adelante) sus propiedades
# el objeto tiene que poder reconocer cuando se habla de una propiedad que le pertenece.
"""
class usuario():
    def __init__(self,nombre_usuario,email,contraseña):
        self.nombre_usuario=nombre_usuario
        self.email=email
        self.contraseña=contraseña
    
    def saludar(self,usuario):
        print(f"Hola {usuario.nombre_usuario}, te envio un saludo. \n-{self.nombre_usuario}") #
        #Aqui se puede ver que el método utiliza el nombre_usuario de ambos objetos usuario, el
        #que saluda y el que recibe el saludo.
        #para poder diferenciar el nombre del usuario que recibe el saludo (que se pasa como parámetro)
        #del que saluda que es el que aplica el método se usa el prefijo self (que es el que hace referencia al 
        # atributo del objeto que esta usando el método, en este caso "saludar").
        #persona que recibe saludo (usuario.nombre_usuario)
        #persona que manda saludo (self.nombre_usuario)

        #Una ventaja que trae esto, es que el parámetro que tiene como sufijo self, queda siempre guardado dentro del
        #objeto y lo podemos usar en otros métodos que tenga el mismo objeto.



usuario1=usuario("Loki","loki@gmail.com","abc")
usuario2=usuario("Thor","thor@gmail.com","123")
usuario1.saludar(usuario2)
"""









#Seccion 5: métodos get y set------------------------------------------------------------------------------------
#Cuando se quiere obtener o modificar las propiedades de un objeto, se podría hacer de la siguiente forma:
#objeto.propiedad  
#objeto.propiedad=valor_nuevo
#Sin embargo esto puede hacer se cambie algún valor fuera de la misma clase por accidente, porque se suelen crear métodos 
#dentro de la clase para evitarlo.
#Otra ventaja es que los atributos se emplean como si fuera métodos en el código.
"""
class usuario():
    #cuando definimos la variable dentro del método __init__, la declaramos con dos
    #guiones bajos al principio, esto hará que sea imposible utilizarla desde fuera
    #de la clase misma

    def __init__(self,nombre_usuario,email,contraseña):
        self.__nombre_usuario=nombre_usuario  
        self.email=email
        self.contraseña=contraseña
    
    #Para poder acceder al atributo nombre_usuario del objeto se define el método get,
    #La convención del método es get_ y el nombre de la variable a devolver.
    def get_nombre_usuario(self): 
        return self.__nombre_usuario

    #Para poder modificar el atributo nombre_usuario del objeto se define el método set,
    #La convención del método es set_ y el nombre de la variable a devolver.
    def set_nombre_usuario(self,nombre_usuario):
        self.__nombre_usuario=nombre_usuario

usuario1=usuario("Loki","loki@gmail.com","abc")

print(usuario1.get_nombre_usuario()) #Imprimimos el nombre del usuario.
usuario1.set_nombre_usuario("Loki2") #Cambiamos el nombre del usuario.
print(usuario1.get_nombre_usuario()) #Imprimimos el nuevo nombre del usuario.
"""











#Seccion 6: métodos getter properties y setter properties ------------------------------------------------------------------------------------
#Estos métodos prácticamente hacen lo mismo que set y get, pero usan decoradores.
#Esta metodología mejora la legibilidad del Código, debido que se generan atributos
#que funcionan como métodos, y al funcionar como métodos, permiten agregar una lógica.
"""
class usuario():
    
    def __init__(self,nombre_usuario,email,contraseña):
        self.__nombre_usuario=nombre_usuario  
        self.email=email
        self.contraseña=contraseña
    
    @property #Para el metodo get usamos la palabra reservada property.
    def nombre_usuario(self):
            return self.__nombre_usuario

    @nombre_usuario.setter #Para el metodo set usamos la palabra setter.
    def nombre_usuario(self,nombre_usuario_nuevo):
        self.__nombre_usuario=nombre_usuario_nuevo


usuario1=usuario("Loki","loki@gmail.com","abc")
print(usuario1.nombre_usuario) #Imprimimos el nombre del usuario.
usuario1.nombre_usuario="Loki2" #Cambiamos el nombre del usuario.
print(usuario1.nombre_usuario)  #Imprimimos el nombre del usuario.
"""










#Seccion 7: métodos y atributos estáticos------------------------------------------------------------------------------------
#Los atributos estáticos son pertenecientes a la clase e independientes del objeto u objetos que se cree a partir de la misma.
#Los métodos estáticos tienen la misma finalidad, pertenecer a la clase, utilizan el método @staticmethod.
"""
class Invitado():
    personas_en_la_fiesta=[] #atributo estatico, esta dentro de la clase, pero no pertenece a ningun objeto en si.


    def __init__(self,invitado,locacion): #El método __init__ se ejecuta cada vez que se crea un objeto
        self.invitado=invitado             #a partir de una clase.
        self.locacion=locacion
        Invitado.personas_en_la_fiesta.append(self.invitado)
        print(f"Llego {self.invitado}! viene desde {self.locacion}!!! \n ")
    


    @staticmethod #metodo estatico, esta dentro de la clase, pero no pertenece a ningun objeto en si.
    def controlador_multitud():
        if len(Invitado.personas_en_la_fiesta)==5:
            print("No entra nadie mas a la fiesta...")
            return
        print("Todavia hay lugar en la fiesta!!! \n")

Usuario1=Invitado("Loki","Jotunheim") #Se crea un objeto contador_usuarios + 1
Usuario1=Invitado("Thor","Asgard") #Se crea un objeto contador_usuarios + 1
Usuario1=Invitado("Odin","Asgard") #Se crea un objeto contador_usuarios + 1

Invitado.controlador_multitud() #Controlamos cuantas personas hay en la fiesta.

Usuario1=Invitado("Frey","Vanaheim") #Se crea un objeto contador_usuarios + 1
Usuario1=Invitado("Sif","Asgard") #Se crea un objeto contador_usuarios + 1

Invitado.controlador_multitud() #Controlamos cuantas personas hay en la fiesta.
#Notar que los métodos estaticos se utilizan en relacion a la clase y no a los objetos.
"""





#Seccion 8: métodos privados------------------------------------------------------------------------------------
#Al igual que con los atributos podemos crear métodos privados utilizando el prefijo __ (doble guion bajo)
"""
class perro():
    
    def __init__(self,nombre): 
        self.nombre=nombre

    def ladrar(self): #Este método se puede ver desde afuera de la clase.
        print("woof woof")

    def __aullar(self):  #Este método no se puede ver desde afuera de la clase.
        print("awoooooo ooo ooo")

    def aullar_y_ladrar(self): #Este método no se puede ver desde afuera de la clase.
        self.__aullar() #Este método es privado y se puede solo desde adentro de la clase.
        self.ladrar()

perro1=perro("Tornillo")
perro1.ladrar()
#perro1.__aullar() #Esto lanza un error,debido a que desde fuera de la clase no se ve el metodo.
print("----------------------------------------------------------------")
perro1.aullar_y_ladrar()
"""










#Seccion 9: Encapsulamiento------------------------------------------------------------------------------------
#El encapsulamiento consiste en hacer completamente invisible el atributo de una clase, de tal forma que ni siquiera sea necesario 
#Iniciarlizarlo cuando se crea el objeto, pero poder modificarlo con métodos del objeto.
"""
class persona():

    def __init__(self,nombre):
        self.nombre=nombre
        self.__edad=22

    def presentacion(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.__edad} años de edad.") #Este método puede usar el atributo edad
                                                                                 #por que esta adentro de la clase.

    def aumentar_edad(self,años_a_aumentar): #Este método puede modificar el atributo edad
                                             #por que esta adentro de la clase.
        self.__edad=self.__edad+años_a_aumentar


persona1=persona("Loki") #Creamos objeto persona, como se puede ver, no se pasa el valor de edad, ya que se ese tributo esta encapsulado.
persona1.presentacion() #Usamos un método para presentar a la persona.
#print(persona1.__edad) #Este método no va funcionar por que el atributo es privado.
persona1.aumentar_edad(10) #Este método modifica indirectamente el atributo edad del objeto persona.
persona1.presentacion()  #Usamos un método para presentar a la persona.

#Como se puede ver, desde afuera de la clase, en ningún momento se modificar el atributo edad de manera directa
"""










#Seccion 10: Abstracción------------------------------------------------------------------------------------
#La abstracción no es una herramienta de la programación orientada a objetos, sino una forma de diseñar programas
#que consiste en hacer que el usuario no acceda a cuestiones que no deba, dicho de otra forma, se busca ocultar toda 
# la información que es irrelevante para que el usuario use el programa

#Por ejemplo, en un hipotético caso de un inicio de sesión de una aplicación, no es necesario que el usuario se entere del proceso de
#verificacion, solo debe enterarse de que el inicio de sesión fue aprobado o no:

#Suponemos un ejemplo donde hay que introducir usuario y contraseña
#Al usarlo, se ve que el usuario no interactúa directamente con el método validación, no tiene idea de su lógica, 
# ni es de su interés solo le interesa saber si accedió o no a su cuenta.
#(Nota: en este ejemplo y solo por simplificar, suponemos que una contraseña correcta es una que sea de tipo int)
"""
class cuenta():

    def __init__(self,usuario,contraseña):
        self.usuario=usuario
        self.contraseña=contraseña

    def __validacion(self):
        if type(self.contraseña)==int:
            return "es valido"
        else:
            return "no es valido"

    def acceso(self):
        print(f"El acceso para {self.usuario} {self.__validacion()}")


usuario1=cuenta("Loki",123)
usuario1.acceso()

usuario2=cuenta("Thor","123")
usuario2.acceso()
"""





#Seccion 11: Herencia------------------------------------------------------------------------------------
#Python permite que al tener una clase definida, otra pueda "heredar" sus atributos y metodos y ademas permite agregar 
# propios de esta nueva clase, esto sirve para ahorrar codigo.
#La idea es que la clase padre, sea la mas general, es decir, que contenga atributos y metodos que tendrian las clases hijas.
"""
class Persona():  #Clase padre 
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def caminar(self):
        print(f"{self. nombre} esta caminando...")
    def dormir(self):
        print(f"{self. nombre} esta durmiendo...")
    


class Estudiante(Persona): #Clase hija 1, se agrega la clase padre entre los parentesis de la definicion de la clase.
    def __init__(self,nombre,edad,carrera,universidad):
        super().__init__(nombre,edad) #Esta instruccion inicializa los atributos heredados,
        self.carrera=carrera          #la palabra super hacer referencia a la clase padre.
        self.universidad=universidad
    def estudiar(self):
        print(f"{self. nombre} esta estudiando")
    def ir_universidad(self):
        print(f"{self. nombre} esta yendo a la universidad...")


class Trabajador(Persona): #Clase hija 2, se agrega la clase padre entre los parentesis de la definicion de la clase.
    def __init__(self,nombre,edad,puesto,empresa):
        super().__init__(nombre,edad)
        self.puesto=puesto
        self.empresa=empresa

    def trabajar(self):
        print(f"{self. nombre} esta trabajando...")
    def ir_trabajo(self):
        print(f"{self. nombre} esta yendo al trabajo...")


persona=Persona("Norberto",75)
estudiante=Estudiante("Julian",18,"Administracion","MIT")
trabajador=Trabajador("Juan",28,"Programador","python.org")



#Se vera que puede hacer cada uno

persona.caminar()
persona.dormir()    
print(persona.nombre)
print(persona.edad)
print("---------------------")
estudiante.dormir()
estudiante.caminar()
estudiante.estudiar()
estudiante.ir_universidad()
print(estudiante.nombre)
print(estudiante.edad)
print(estudiante.carrera)
print(estudiante.universidad)
print("---------------------")
trabajador.caminar()
trabajador.dormir()
trabajador.trabajar()
trabajador.ir_trabajo()
print("---------------------")
print(trabajador.nombre)
print(trabajador.edad)
print(trabajador.puesto)
print(trabajador.empresa)

#Algunas cosas que no funcionarían... (Se puede descomentar para corroborar que no funciona)

#Para la clase padre.
#print(persona.puesto) # la clase persona no tiene el atributo puesto.
#print(persona.empresa) # la clase persona no tiene el atributo empresa.
#persona.estudiar() # la clase persona no tiene el método estudiar.
#persona.trabajar() # la clase persona no tiene el  método trabajar.

#Para las clases hijas.
#print(estudiante.puesto) # la clase estudiante no tiene el atributo puesto.
#print(trabajador.ir_universidad()) # la clase trabajador no tiene el método ir a universidad.
"""










#Seccion 12: Polimorfismo------------------------------------------------------------------------------------
#El polimorfismo, es la capacidad que un método de comportarse distinto dependiendo de que objeto lo use.

class Auto():
    def __init__(self,marca,patente,numero_puertas):
        self.marca=marca
        self.patente=patente
        self.numero_puertas=numero_puertas

    def andar(self):
        print (f"el vehiculo de identificacion {self.patente} esta andando")

class Lancha():
    def __init__(self,marca,patente,numero_velas):
        self.marca=marca
        self.patente=patente
        self.numero_velas=numero_velas

    def navegar(self):
        print (f"el vehiculo de identificacion {self.patente} esta navegando")


auto=Auto("Ford","ABC123",5)
lancha=Lancha("Sherman","U128T",28)

#Algunos metodos e informacion.
#auto.informacion()
#auto.andar()

#lancha.informacion()
#lancha.navegar()

#Si quisiéramos utilizar un método que representa lo mismo para ambos objetos, pero que son distintos 
# (para este caso andar y navegar) haríamos:

lista=[auto,lancha] #Creamos una lista para poder iterarla.

for v in lista:
    if isinstance(v,Auto)==True:
        v.andar()
    elif  isinstance(v,Lancha)==True:
        v.navegar()

#Es decir tendríamos que diferenciar entre un objeto u otro.

#El polimorfismo consiste en que un método heredado de la clase padre se comporte distinto en la clase hija
#Esto mediante la sobreescritura de métodos.


class Vehiculo():
    def __init__(self,marca,patente):
        self.marca=marca
        self.patente=patente

    def andar(self):
        print("el Vehiculo esta andando")
    
    def informacion(self):
        print(f"Este vehiculo es un {self.marca}, su numero de identificacion es {self.patente}")

class Auto(Vehiculo):
    def _init__(self,marca,patente,numero_puertas):
        super().__init__(marca,patente)
        self.numero_puertas=numero_puertas
    def andar(self): #Al llamar al método como el que hereda de la clase padre, se sobre escribe el Código interior.
        print (f"el vehiculo de identificacion {self.patente} esta andando")

class Lancha(Vehiculo):
    def _init__(self,marca,patente,numero_velas):
        super().__init__(marca,patente)
        self.numero_velas=numero_velas
    
    def andar(self): #Al llamar al método como el que hereda de la clase padre, se sobre escribe el Código interior.
        print (f"el vehiculo de identificacion {self.patente} esta navegando")




auto=Auto("Ford","ABC123")
lancha=Lancha("Sherman","U128T")

lista=[auto,lancha] #Creamos una lista para poder iterarla.


for v in lista:
        v.andar()


#Como se puede ver, ahora, ambos objetos llaman al mismo método, pero hacen cosas distintas. esto de definir un método
#En la clase padre y volver a definirlo con el mismo nombre en la clase hija se llama sobreescritura.
#El polimorfismo consiste en que un método se comporte distinto, dependiendo de que objeto lo use.

#Un ejemplo de polimorfismo propio de python es el de la funcion len
#len([1,2,3]) devuelve 3 , debido a que len() al tomar una lista devuelve la cantidad de elementos que contiene.
#len("Hola") devuelve 4 , debido a que len() al tomar una cadena de texto devuelve la cantidad de caracteres de la misma.










#seccion x: algunos datos extra:
#print(clase.__dict__) #Devuelve informacion sobre los parametros de la clase
















