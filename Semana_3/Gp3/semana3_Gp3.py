#!/usr/bin/env python
# coding: utf-8

# In[3]:


rock=["cancion1","cancion2","cancion3"]
bachata=["cancion4","cancion5","cancion6"]
pop=["cancion7","cancion8"]

playlist=rock+bachata
print(playlist)
print("_________________________")
playlist.append("ejem_append") #append agrega un nuevo item al final de la lista, agrega el elemento completo
#playlist.append(pop)
print(playlist)
print("_________________________")

playlist.extend(pop)
print(playlist)
print("_________________________")

playlist.extend("cancion8")# cuando agrego una sola cosa con extend, la agrega separando sus elementos
print(playlist)

#Resumen:
#si quiero agregar un solo elemento a la lista lo agrego con append
#si quiero agregar otra lista a mi lista lo hago con extend (porque asi me une varios elementos)


# In[4]:


rock=["cancion1","cancion2","cancion3"]
del rock[1]#delete-> borrar desde la coordenada 
print(rock)


# In[6]:


rock=["cancion1","cancion2","cancion3"]
#.pop() -> toma el ultimo valor, lo elimina y lo retorna
ultima_cancion=rock.pop() #deshacer -> ctrl+z -> para listas
print(ultima_cancion)
print(rock)


# In[11]:


rock=["cancion1","cancion2","cancion3", "cancion2"]
#.remove() -> remover un elemento especifico,OJO! solo elimina el primero de varios items repetidos
rock.remove("cancion2") #
print(rock)


# In[18]:


#slicing -> es recortar una lista en rangos definidos
print(list(range(0,10,1)))

a_list=[1,2,3,4,5,6,7,8,9]
lst_recortada=a_list[1:5]
print(lst_recortada)

lst_recortada2=a_list[::5]# nomenclatura diferente por ejemplo a_list[0:9:5]
print(lst_recortada2)


# In[30]:


#saber si la lista contiene un elemento
a_list=[1,2,3,4,5,6,7,8,9]
pregunta1 = 8 in a_list
pregunta2 = 12  in a_list
print(pregunta1,pregunta2)

for n in a_list:
    print(n, end=" ")

if (pregunta2 == False ):
    a_list.append(12)

if (pregunta1 == True ):
    a_list.remove(1)
    
print()
print(a_list) 


# In[40]:


person1=["jose",28,0,170.00,234]
person2=["luis",25,0,175.00,435]
person3=["yudivith",18,1,165.00,123]
person4=["sara",21,1,165.00,789]

asistentes=person1+person2+person3+person4

n_person=(len(asistentes)//5)
age_average=0
age_sum=0
for age in asistentes[1::5]:
    age_sum+=age
age_average= age_sum // n_person  
print(n_person)    
print("la edad promedio es : {}".format(age_average))


# In[ ]:


a_list=[1,2,3,4,5,6,7,8,9]
print(len(a_list)) #me retorna la longitud -> la cantidad de elementos
print(max(a_list))
print(min(a_list))
print(sum(a_list))


hay_cosas_en_a=any(a_list) # pregunta si hay elementos en la lista
print(hay_cosas_en_a)
b_list=[0,''] # creo una lista vacia, porque se necesitara mas adelante
print(b_list)
any(b_list)


#for n in b_list:
#    b_list.append("sgXXX") # se que est lo necesitaria mas adelante
    #print(n, end=" ")
    
c.append(7) # cuando la lsita no existe, append la crea


# In[56]:


a_list=[1,2,3,4,6,7,8,9]
a_list.insert(4,5) # inserta en insert(coordena,valor)
print(a_list)


# In[58]:


#sort organiza
a_list=[5,6,2,8,1,3,4,9,7] 
a_list.sort() # ascendente
print(a_list)
a_list.sort(reverse = True) #descendente
print(a_list)


# In[59]:


tup=(5,3,2,6,1,4)
#si yo tengo una tupla, y la queiro editar OBLIGATORIAMENTE debo convertirla a lista
aux_list=list(tup)
aux_list.sort()
print(aux_list)


# In[67]:


l=[1,2,3,1,1,1,2,3,1,3]
print(l.count(1)) # count cuenta cuantas veces esta el elemento
print(l.count(2))
l.clear() # borra todo
print(l)


# In[75]:


profe1={"nombre":"jose","edad":"28","codigo":"3"}
print(profe1["nombre"])
np1=profe1.get("nombre") #obtiene el valor correspondiente a la clave
profe1.items() #obtiene todo el diccionario


# In[ ]:




