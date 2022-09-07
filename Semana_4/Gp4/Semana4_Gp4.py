#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#como programador defino funciones (metodos) que se van a usar repetidamente
#por ejemplo tenemos la funcion print que se definio para usarla repetidamen
#a las funciones tambien se les conoce como METODOS()

#cuando empleo funciones recuerdo 4 cosas
#1 Defino la funcion
#2 Defino si tiene entradas (ARGUMENTOS)
#3 Defino si tiene salidas (RETORNO)
#4 Invoco o uso la funcion (usarla)

#def nombre(argumentos):
#    proceso
#    return


# In[ ]:


#Programacion orientada a objetos POO

# CLASES : es un algo que encierra un conjunto de objetos -sirve para catalogar
# OBJETOS : un objeto es un elemento (UNA INSTANCIA) que pertenece a una clase ->
#           el elemento dentro del conjunto
# ATRIBUTOS :los elementos que pueden diferenciar un objeto de otro
# METODOS: funciones -> una cosa que hace algo que necesito para mi objeto

#diferencia entre  objeto e instancia:
#son "lo mismo" un objeto es una instancia de una clase


#constructores: inicializa/crea/hace que exista  el objeto de la clase y le asigna los atributos
#               correspondientes a su clase
#SELF: autoparametros  -> puntero -> el codigo entiende sobre quien estan hablando 
#                        toma los valores del objeto especifico que estoy trabajando

#JERARQUIA O HERENCIA -> hay un orden, y hay cosas que se pueden heredar 
#                        ->hay abuelos, papas, hijos,etc


# In[1]:


# ejemplo de clases
# Profe Jose
# Gp4
# SIC2022
# 6/09/22

################################## CLASES ################################################

#________________________CLASE PRINCIPAL______________________________

class seres_vivos: #Clase ppal(main) , clase abuelo
    
    
    
    # SIEMPRE PRIMERO DEFINO UN CONSTRUCTOR
    # EN EL CONSTRUCTOR ASIGNO LOS ATRIBUTOS DEL OBJETO QUE PERTENECE A ESA CLASE
    
    def __init__(self,tipo,alimento,habitat,desplazamiento,color): #CONSTRUCTOR
        self.tipo=tipo
        self.alimento=alimento
        self.habitat=habitat
        self.desplazamiento=desplazamiento
        self.color=color
        
    #-------------------GETTERS--------------------- PARA OBTENER INFO
    
    def get_tipo(self):
        return self.tipo
    def get_alimento(self):
        return self.alimento
    def get_habitat(self):
        return self.habitat
    def get_desplazamiento(self):
        return self.desplazamiento
    def get_color(self):
        return self.color
    


    #-------------------SETTERS--------------------- PARA MODIFICAR INFO
    
    def set_tipo(self,tipo):
        self.tipo=tipo
    def set_alimento(self,alimento):
        self.alimento=alimento
    def set_habitat(self,habitat):
        self.habitat=habitat
    def set_desplazamiento(self,desplazamiento):
        self.desplazamiento=desplazamiento
    def set_color(self,color):
        self.color=color
    

#________________________SUBCLASES____________________________________ 

class humanos(seres_vivos): #subclase de la clase seres_vivos
    
    #ejemplo 1 -> en este heredo el constructor de la clase principal (y los atributos)
    
    #def __init__(self,tipo,alimento,habitat,desplazamiento,color):
    #    seres_vivos.__init__(self,tipo,alimento,habitat,desplazamiento,color)
        
    #ejemplo 2 -> en este creo nuevos atributos de mi subclase, y 
    #"por ahora no me interesan los atributos que se heredaron"
    
    def __init__(self,nombre,edad,estatura,peso,codigo):
        self.nombre=nombre
        self.edad=edad
        self.estatura=estatura
        self.peso=peso
        self.codigo=codigo


    #ejemplo 3 -> constructor completo en el que agrego nuevos atributos ademas de los heredados
    
    #def __init__(self,nombre,edad,estatura,peso,codigo,tipo,alimento,habitat,desplazamiento,color):
    #    self.nombre=nombre
    #    self.edad=edad
    #    self.estatura=estatura
    #    self.peso=peso
    #    self.codigo=codigo
    #    seres_vivos.__init__(self,tipo,alimento,habitat,desplazamiento,color)
        
        
    #-------------------GETTERS  SUBCLASE --------------------- PARA OBTENER INFO
    
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_estatura(self):
        return self.estatura
    def get_peso(self):
        return self.peso
    def get_codigo(self):
        return self.codigo
    
    #-------------------SETTERS    SUBCLASE--------------------- PARA MODIFICAR INFO
    
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_edad(self,edad):
        self.edad=edad
    def set_estatura(self,estatura):
        self.estatura=estatura
    def set_peso(self,peso):
        self.peso=peso
    def set_codigo(self,codigo):
        self.codigo=codigo    
        
        
        
################################## VARIABLES GLOBALES, FUNCIONES , ETC  ################################################


################################## MAIN ################################################

#________________ ejemlplo de como definir objetos para la clase padre ________


# crear los objetos de la clase seres_vivos
ser_vivo1=seres_vivos("humanos","variado","panama","bipedo","amarillo")
ser_vivo2=seres_vivos("animales","variado","panama","depende","variado")
ser_vivo3=seres_vivos("plantas","luz","panama","estatico","verde")

#accedemos a los atributos mediante los metodos set y get 
print(ser_vivo1.get_habitat())
ser_vivo1.set_habitat("colombia")
print(ser_vivo1.get_habitat())
print("________________________")

#________________ ejemplo de como definir objetos para la clase hijo usando HERENCIA ________

#ejemplo 1 -> solo heredo los atributos de la clase padre y sus metodos
#                  tipo    ,alimento ,habitat,desplazamiento,color
#persona1=humanos("humano","variado","panama","bipedo","amarillo")
#print(persona1.get_tipo())


#ejemplo 2 -> creo mis nuevos atributos sin usar los del padre, PERO!!!!! SI HEREDO TODO 

#               nombre,edad,estatura,peso,codigo
persona1=humanos("jose","28","170","63","1234")
print(persona1.nombre)
persona1.set_habitat("colombia") # Aunque en este ejemplo no habia atributo habitat, lo herede del padre, tambien el metodo
print("el habitat es : ",  persona1.get_habitat())

#ejemplo 3 -> creo lo nuevo + lo que herede
#                 nombre,edad,estatura,peso,codigo,tipo,alimento ,habitat,desplazamiento,color
#persona1=humanos("jose","28","170","63","1234","humano","variado","colombia","bipedo","amarillo")

