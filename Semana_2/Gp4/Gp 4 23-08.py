#!/usr/bin/env python
# coding: utf-8

# In[6]:


#while -> mientras : es un bucle que se repite infinitamente

#for -> para : es un bucle que se repite un numero especifico de veces

password="python"
pas=""
#while pas!= password and contador<3 :# mientras ->repite mientras la condicion se cumpla
print(list(range(3,0,-1)))
for contador in range(0,3,1): # range(incio,final,paso)
    pas=input("ingrese su contraseña: ")
    #contador=contador+1 # los contadores se usan como variables auxiliares, es una variable que se actualiza y aumenta en cada repetición
    print(contador)
    
    #contador+=1 #otra opcion que hace lo mismo
    if pas!= password:
        print("loging failed")
    else:
        print("loging success")
        #contador=4
        break #interrupcion del codigo
print("close program")


        


# In[8]:


print(list(range(7,15,2)))
print(list(range(7,15,3)))


# In[81]:


import random as rd
print(rd.random())
print(rd.randrange(0,10,2))
print(list(range(0,10,2)))


# In[99]:


pi=3.141592654
e=0.213123
print("La constante pi es: " + str(pi))
print("La constante pi es: ",pi,"y e es: ",e)
print("La constante pi es: {0:.4f} ".format(pi))
print("La constante pi es: {0:.4f} y e es : {1:.4f} ".format(e,pi)) 
#el numero antes de : hace referencia al orden de las vqariables dentro de format
print("La constante pi es: {1:.4f} y e es : {0:.4f} ".format(e,pi))


# In[101]:


for i in range (1,10,1):
    print("{0:3d} {1:4d} {2:5d}".format(i,i*i,i**3))


# In[128]:


#maneras de almacenar data

# LISTAS -> conjunto de datos separados por una coma, con [], SI se puede modificar
print(list(range(3,0,-1)))

lstMercado=["leche","pan",8,"huevos",5,6,7] 
print(lstMercado[3])
lstMercado[3]="queso"
print(lstMercado[3])
print(lstMercado)

#for i in range(lstMercado):
#    print((lstMercado[i]))


#TUPLAS -> conjunto de datos separados por una coma, con (), NO se puede modificar
tMercado=("leche","pan",8,"huevos",5,6,7)
print(tMercado[3])
#tMercado[3]="queso"
print(tMercado[3])
print(tMercado)
t_datos_de_usuario_bancario=("jose","132412564","300")

#MATRICES -> lista de listas, [], SI se puede modificar
m_teclado=[[1,2,3],[4,5,6],[7,8,9]]
print(m_teclado)
print(m_teclado[1][1])
#m_teclado[1][2]=27
print(m_teclado)




# In[127]:


m_teclado=[[1,2,3],[4,5,6],[7,8,9]]

#len() -> lenght -> longitud
#print(len(m_teclado))
#print(len(m_teclado[0]))
#print(len(m_teclado[1]))

for filas in range(len(m_teclado)):
    for columnas in range(len(m_teclado[filas])):
        print(m_teclado[filas][columnas],end=" ")
    print() # -> print("\n")

