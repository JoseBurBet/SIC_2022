#!/usr/bin/env python
# coding: utf-8

# In[40]:


lstMercado=["leche","pan",8,"huevos",5,6,7] 
print(list(range(len(lstMercado))))

for i in range(len(lstMercado)):
    print(i)    
print("________________________________________")    
for i in lstMercado:
    print(i)    


# In[12]:


rock=["cancion1","cancion2","cancion3"]
bachata=["cancion4","cancion5","cancion6"]
pop=["cancion7","cancion8"]

playlist=rock+bachata
playlist.append("cancion7") #append agrega un nuevo item al final de la lista
#playlist.append(pop)
playlist.extend(pop)
playlist.extend("cancion8")
print(playlist)


# In[37]:


#diccionario={"key":"valor"}
#profe1=[jose,28,234234]
#profe1[0]==jose
        
profe1={"nombre":"jose","edad":"28","codigo":"3"}
profe2={"nombre":"rafa","edad":"30","codigo":"7"}
#print(profe1["nombre"])
datos_profes={"jose":profe1,"rafa":profe2}

#PROGRAMACION ORIENTADA A OBJETOS -> POO
#print(datos_profes["rafa"])
print(datos_profes)

print("________________________________________________")

for key,value in profe1.items():
        print(key,value)
    

print("________________________________________________")

for key,value in datos_profes.items():
    for i,j in datos_profes[key].items():
        print(key,value)
    print()
    

