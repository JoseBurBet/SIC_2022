#!/usr/bin/env python
# coding: utf-8

# In[5]:


#bucle que se repite un numero limitado de veces
i=0
contador=80
for contador in range(0,10,2): #range (inicio,final,paso)
    i+=1 # i=i+1
    print("el contador es" + str(contador))
    print("el valor de i es" + str(i))
    #print("hello world \n")


# In[48]:


password="python"
pas=""
contador = 0 #i, j,k
#while pas!= password and contador<3 :# mientras ->repite mientras la condicion se cumpla
print(list(range(0,3,1)))
for contador in range(0,3,1): 
    pas=input("ingrese su contraseña: ")
    #contador=contador+1
    print(contador)
    #contador+=1 #otra opcion que hace lo mismo
    if pas!= password:
        print("loging failed")
    else:
        print("loging success")
        break
        #contador=4

        


# In[47]:


import random  as rd # importo una libreria que se llama random

print(rd.randrange(1,7,2))



# In[53]:


pi=3.141592654
lamda=1.123
texto="el valor de pi es : "
print(texto + str(pi))
print("el valor de pi es : " + str(pi)) 
print("el valor de pi es : {} y el valor de lamda es :{} ".format(pi,lamda))
print("el valor de pi es : {0:.3f} ".format(pi))

print(list(range(2,11,2)))
for i  in range (2,11,2):
    print("{0:3d} {1:4d} {2:5d} ".format(i,i*i,i*i*i))


# In[56]:


print(list(range(2,11,2)))
for i  in range (2,11,2):
    print("{0:3d} {1:4d} {2:5d} ".format(i,i*i,i*i*i))


# In[87]:


#MANERAS DE ALMACENAR DATOS
#LISTAS!!!!!!!! # CONJUNTO DE DATOS SEPARADOS POR UNA , SE PUEDEN EDITAR, SE DEFINEN CON []

lst_super=["leche","pan","carne",8]
print(lst_super[2])
lst_super[2]="pescado"
print(lst_super[2])
print(lst_super)

#TUPLAS!!!!!!!# CONJUNTO DE DATOS SEPARADOS POR UNA , NO SE PUEDEN EDITAR, SE DEFINEN CON ()
print("________________________________________")
tupla_banco=("jose",1234)
print(tupla_banco[1])
#tupla_banco[1]=9876 # no se puede !!!  porque no puedo permitir que el usuario modifique ese valor
print(tupla_banco[1])
print(tupla_banco)

lst_banco=list(tupla_banco) # puedo convertir de un tipo al otro
print(lst_banco)


#MATRICES!!!!!!!!!! # es una lista de listas
M_teclado_telefono=[[1,2,3],[4,5,6],[7,8,9]] #matriz simetrica
print(M_teclado_telefono)
print(M_teclado_telefono[1][1])

print("________________________________________")

print(len(M_teclado_telefono)) #len = lenght

for fila in range(len(M_teclado_telefono)): #len te dice la longitud de las filas
    for columna in range(len(M_teclado_telefono[fila])):# len te dice la longitud de las columnas [i]
        print(M_teclado_telefono[fila][columna], end=" ") # el end evita el salto de linea
        #print("fila {} \n ".format(fila))
        #print("columna {} \n ".format(columna))
    print()# =  print("\n"), lo ponemos para generar el salto de linea
    


# In[84]:


print("bla bla", end=" ") # el end evita el salto de linea
print("sadfasdf")

