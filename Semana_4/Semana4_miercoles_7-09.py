#!/usr/bin/env python
# coding: utf-8

# In[43]:


#codigo de un constructor de pantalla de inicio de un juego

# creo un diccionario con todos los posibles personajes que puede tener mi juego

#diccionario={"key1":"valor1","key2":"valor2"}

personajes = {
    "raza":{
        "humanos":{
            "clase":{
                "gerreros":{
                    "stats":{
                        "vida":"1200",
                        "mana":"850"
                    }
                },
                "cazador":{
                    "stats":{
                        "vida":"800",
                        "mana":"900"
                    }             
                },
                "druida":{
                    "stats":{
                        "vida":"1000",
                        "mana":"1200"
                    }             
                }
                           
            }
            
        },
        
        "orcos":{
            "clase":{
                "gerreros":{
                    "stats":{
                        "vida":"1200",
                        "mana":"850"
                    }
                },
                "cazador":{
                    "stats":{
                        "vida":"800",
                        "mana":"900"
                    }             
                },
                "chaman":{
                    "stats":{
                        "vida":"1000",
                        "mana":"1200"
                    }             
                }
                           
            }
            
        }
        
    }
}

#print(personajes["raza"]["humanos"]["clase"]["cazador"]["stats"]["mana"])

import uuid
import json
import time


class personaje():
    
    def __init__(self,nombre,raza,clase,vida,mana):
        self.nombre=nombre
        self.raza=raza
        self.clase=clase
        self.vida=vida
        self.mana=mana
    
    def configurar_personaje(self):
        
        print("Que raza quieres ser?: \n 1. humanos \n 2. orcos \n")
        raza=input("\n")
        
        if raza=="1" or raza=="humanos":
            raza="humanos"
            
            print("Que clase quieres ser?: \n 1. guerrero \n 2. cazador \n 3. druida \n")
            clase=input("\n")
            
            if clase=="1" or clase=="guerrero":
                clase="guerrero"
                
                #aqui llamamos un metodo que cree al personaje
                self.crear_personaje(raza,clase)
                
            elif clase=="2" or clase=="cazador":
                clase="cazador"
                
                #aqui llamamos un metodo que cree al personaje
                self.crear_personaje(raza,clase)
                
            elif clase=="3" or clase=="druida":
                clase="druida"
                
                #aqui llamamos un metodo que cree al personaje
                self.crear_personaje(raza,clase)
            
            else:
                print("clase no valida")
                #control de errores
        
        elif raza=="2" or raza=="orcos":
            raza="orcos"
            
            print("Que clase quieres ser?: \n 1. guerrero \n 2. cazador \n 3. chaman \n")
            clase=input("\n")
            
            if clase=="1" or clase=="guerrero":
                clase="guerrero"
                
                #aqui llamamos un metodo que cree al personaje
                self.crear_personaje(raza,clase)
                
            elif clase=="2" or clase=="cazador":
                clase="cazador"
                
                #aqui llamamos un metodo que cree al personaje
                self.crear_personaje(raza,clase)
                
            elif clase=="3" or clase=="chaman":
                clase="chaman"
                
                #aqui llamamos un metodo que cree al personaje
                self.crear_personaje(raza,clase)
            
            else:
                print("clase no valida")
                #control de errores
                
        else:
            print("raza no valida")
                #control de errores
                
    def crear_personaje(self,raza,clase):
        #accedo al diccionario
        vida=personajes["raza"][raza]["clase"][clase]["stats"]["vida"] 
        mana=personajes["raza"][raza]["clase"][clase]["stats"]["mana"]
        
        nombre = input("Adalid! , como deseas ser llamado : \n")
        #llamo al constructor
        nuevo_pj=personaje(nombre=nombre,raza=raza,clase=clase,vida=vida,mana=mana)
        
        #creo un diccionario para guardar la info de mi personaje creado
        datos={
            "id":str(uuid.uuid1()),
            "nombre":nuevo_pj.nombre,
            "raza":nuevo_pj.raza,
            "clase":nuevo_pj.clase,
            "vida":nuevo_pj.vida,
            "mana":nuevo_pj.mana
        }
        
        #aqui tenemos que llamar un metodo para guardar al personaje
        print("El personaje {} ha sido creado y guardado satisfactoriamente".format(nuevo_pj.nombre))
        
pj=personaje("Shigueru","humano","druida","1000","1200") 
pj.configurar_personaje()
        
        
    


# In[18]:


import uuid

u1 = uuid.uuid1() #me otorga un codigo unico de identificacion
u2 = uuid.uuid1()
u3 = uuid.uuid1()
print(u1)
print(u2)
print(u3)


# In[21]:


import json # es un formato para guardar datos, como archivo
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}


# In[24]:


import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  time.sleep(1) # es un delay,un retraso temporal en la ejecucion del loop


# In[36]:


raza="elfo";

