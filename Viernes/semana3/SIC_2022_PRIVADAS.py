#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#como programador defino funciones (metodos) que se van a usar repetidamente
#por ejemplo tenemos la funcion print que se definio para usarla repetidamente!
#a las funciones tambien se les conoce como METODOS()


#cuando empleo funciones recuerdo 4 cosas

#1 Defino la funcion
#2 Defino si tiene entradas (ARGUMENTOS)
#3 Defino si tiene salidas (RETORNO)
#4 Invoco o uso la funcion


# In[ ]:


#Programacion orientada a objetos POO

# CLASES : es un algo que encierra un conjunto de objetos -sirve para catalogar
# OBJETOS : un objeto es un elemento (UNA INSTANCIA) que pertenece a una clase -> el elemento dentro del conjunto
# ATRIBUTOS :los elementos que pueden diferenciar un objeto de otro
# METODOS: funciones -> una cosa que hace algo que necesito para mi objeto

#diferencia entre  objeto e instancia:
#son "lo mismo" un objeto es una instancia de una clase


#constructores: inicializa/crea/hace que exista  el objeto de la clase y le asigna los atributos
#               correspondientes a su clase
#SELF: autoparametros  -> puntero -> el codigo entiende sobre quien estan hablando 
#                        toma los valores del objeto especifico que estoy trabajando

#JERARQUIA O HERENCIA -> hay un orden, y hay cosas que se pueden heredar ->hay abuelos, papas, hijos,etc


# In[17]:


#####################################################################
#Primer ejemplo de Calses

########################################### CLASE PADRE
########## Defino mis Calses #############
class profesoresSIC:
    
    def __init__(self,nombre,apellido,edad,codigo): #constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.codigo = codigo

        
###########Setters y getters        
        
########## con el get, accedo a toda la informacion sobre los atributos del objeto    
    
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_edad(self):
        return self.edad
    def get_codigo(self):
        return self.codigo

########## con el set, modifico toda la informacion sobre los atributos del objeto    
    
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_apellido(self,apellido):
        self.apellido = apellido
    def set_edad(self,edad):
        self.edad = edad
    def set_codigo(self,codigo):
        self.codigo = codigo   
        
    
############################################# clase hijo

class tutor(profesoresSIC):
    
    def __init__(self,nombre,apellido,edad,codigo):
        profesoresSIC.__init__(self,nombre,apellido,edad,codigo)
        
        
        
        
        

############ MAIN #################### aqui hago el llamado mis funciones,clases, etc


####################### cree los profesores principales de la clase profesores
profe1 = profesoresSIC("jose","burgos",28,1234)
profe2 = profesoresSIC("rafa","puche",30,5678)
profe3 = profesoresSIC("argenis","bouzas",32,9012)
profe4 = profesoresSIC("cristiam","loaiza",33,3456)

print(profe1.get_nombre())
profe1.set_nombre("erick")
print(profe1.get_nombre())

############ voy a crear a los tutores

tutor1 = tutor("luis","gutierrez",23,1234)
tutor2 = tutor("ana","bermudez",23,1234)
tutor3 = tutor("fredy","gonzales",23,1234)
tutor4 = tutor("arturo","morales",23,1234)

print(tutor1.get_nombre())



# In[20]:


class profesoresSIC: 
    def __init__(self,nombre,apellido,edad,codigo) : 
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad = edad 
        self.codigo = codigo 

  

        
profe1 = profesoresSIC("jose","burgos",28,1234) 
profe2 = profesoresSIC("rafa","puche",30,5678) 
profe3 = profesoresSIC("argenis","bouzas",32,9212) 
profe4 = profesoresSIC("cristian","loaiza",33,3456)

