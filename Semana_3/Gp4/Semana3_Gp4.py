#!/usr/bin/env python
# coding: utf-8

# In[7]:


#añadir datos
rock=["cancion1","cancion2","cancion3"]
bachata=["cancion4","cancion5","cancion6"]
jazz=["cancion7","cancion8"]

playlist=rock+bachata

print(playlist)
print("________________________________")

playlist.append("ejm_append") #append agrega un nuevo item al final de la lista / si la lista no exite, appen la crea
print(playlist)
print("________________________________")

#playlist.append(jazz) #pasa de ser lista a ser matriz porque append agrega la lista jazz como un lista dentro de otra lista
#print(playlist)
#print("________________________________")

playlist.extend(jazz) # extend me agrega los elementos uno por uno
print(playlist)
print("_________________________")

playlist.extend("cancion8")# cuando agrego una sola cosa con extend, la agrega item por item 
print(playlist)




# In[20]:


#Eliminar datos de la lista
rock=["cancion1","cancion2","cancion3","cancion4","cancion5"]
print(rock[1])
del rock[1] # del -> delete -> eliminar
print(rock[1])
print(rock)
# .pop()  -> pop, revisa cual es el ultimo valor, lo retorna y lo elimina
ultimo_item=rock.pop() # ctrl-z toma el ultimo elemento
print(ultimo_item)
print(rock)
print("_________________________")
ultimo_item=rock.pop(0) # el argumento nos dice a que posicion hacer el pop
print(ultimo_item)
print(rock)
print("_________________________")
rock.remove("cancion4") # Elimina haciendo una busqueda por nombre o elemento
print(rock)
print("_________________________")
aux_list=[8,5,6,8,7,4,8,6]
rock.extend(aux_list*3) # podemos utilizar mutipplicadores para repetir un proceso varias veces
print(rock)
print("_________________________")
rock.remove(8) # si existen elementos repetidos solo borra el primero
print(rock)
print("_________________________")


# In[22]:


# slicing -> particionar,es recortar una lista en rangos definidos
print(list(range(0,10,1))) # range(inicio,final,paso)


aux_list=[8,5,6,8,7,4,8,6]
lst_recortada=aux_list[1:5]# [inicio:final:paso]
print(lst_recortada)
print("_________________________")

lst_recortada=aux_list[::3]# [inicio:final:paso] # nomenclatura diferente
print(lst_recortada)
print("_________________________")


# In[31]:


# saber si la lista tiene un elemento

# for i in lstMercado:
aux_list=[8,5,6,8,7,4,8,6]

pregunta1= 8 in aux_list #tengo en stock / bodega / existencias del producto
pregunta2= 1 in aux_list

print(pregunta1,pregunta2)

print(aux_list)

while (pregunta1 == True):
    pregunta1= 8 in aux_list
    if (pregunta1 == True):
        aux_list.remove(8)
        print(aux_list)


# In[32]:


person1=["jose",28,0,170.00,234]
person2=["luis",25,0,175.00,435]
person3=["jorge",21,1,181.00,123]
person4=["laurent",17,1,160.00,789]
asistentes=person1+person2+person3+person4
print(asistentes)
n_person=(len(asistentes)//5) #// division exacta -> int
age_average=0
age_sum=0
for age in asistentes[1::5]:
    age_sum+=age
age_average= age_sum // n_person 
print(n_person) 
print("la edad promedio es : {}".format(age_average))


# In[48]:


#Otras funciones utiles

a_list=[1,2,3,4,5,6,7,8,9]
print(len(a_list)) #me retorna la longitud -> la cantidad de elementos
print(max(a_list)) # retorna el maximo
print(min(a_list)) # retorna el min
print(sum(a_list)) # retorna la suma

b_list=["dr","ds","dc","da"] #toma los valores del codigo ASCII
# compara los valores de izq a derecha
print(len(b_list)) #me retorna la longitud -> la cantidad de elementos
print(max(b_list)) # retorna el maximo
print(min(b_list)) # retorna el min

b_list.sort()
print(b_list)
#100-d
#97-a
#114-r


# In[56]:


#mas funciones utiles
l=[1,2,3,1,1,1,2,3,1,3]
print(l.count(1)) # count cuenta cuantas veces esta el elemento
print(l.count(2))
l.insert(4,"test") # inserta en insert(coordena,valor)
print(l)
l.clear() # borra todo
print(l)


# In[40]:


# sort -> ordenar
a_list=[5,6,2,8,1,3,4,9,7] 
b_list=["c","j","a","d","e"]
a_list.sort() # ascendente
print(a_list)
a_list.sort(reverse = True) #descendente
print(a_list)
print("_______________________")
b_list.sort() # ascendente
print(b_list)
b_list.sort(reverse = True) #descendente
print(b_list)


# In[ ]:


# recordatorio
tup=(5,3,2,6,1,4)
#si yo tengo una tupla, y la queiro editar OBLIGATORIAMENTE debo convertirla 
aux_list=list(tup)
aux_list.sort()
print(aux_list)



# In[53]:


#Diccionarios
profe1={"nombre":"jose","edad":"28","codigo":"3"}
print(profe1["nombre"])
np1=profe1.get("nombre") #obtiene el valor correspondiente a la clave
profe1.items() #obtiene todo el diccionario

