#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Calculadora
# Profe Jose
# clase 1 17/08/2022

try: # try ejecuta el codigo hasta que salga un error, en este ejemplo un error seria no ingresar un numero sino letras
    dato1,dato2=input("ingrese dos numeros separados por un espacio \n").split() #la función split separa cada entrada para asignarla a cada variable
    suma=int(dato1)+int(dato2)
    resta=int(dato1)-int(dato2)
    division=int(dato1)/int(dato2)
    multiplicacion=int(dato1)*int(dato2)
    potencia=int(dato1)**int(dato2)
    modulo=int(dato1)%int(dato2)
    cocienteExacto=int(dato1)//int(dato2)
    raiz=int(dato1)**(1/int(dato2))
    print("la suma es: " + str(suma))
    print("la resta es: " + str(resta))
    print("la division es: " + str(division))
    print("la multiplicacion es: " + str(multiplicacion))
    print("la potencia es: " + str(potencia))
    print("la modulo es: " + str(modulo))
    print("la cocienteExacto es: " + str(cocienteExacto))
    print("la raiz es: " + str(raiz))
    
except: # cuando el try detecta el error se activa este código y saca este mensaje 
    print("verifica si lo ingresado si es un numero")
  


# In[17]:


#int(palabra) -> convertir un tipo string en tipo numero = int
#str(numero) -> convertir un tipo numero a string 

dato=input(" \t ingrese un numero \n ") # \t añade una tabulación , \n añade un salto de linea
datoInt=int(dato)
print("dato")
print(dato)
print("el dato es: " + str(datoInt))

v1= 3
v2= 3.14
suma= v1+v2
print(suma)


# In[26]:


#ejemplo de condicional con if -> si
#dato1=input("ingrese un numero")
#dato2=input("ingrese otro numero")
#En el if, si se cumple una condicion ejecuta ese codigo e ignora todo lo demas

dato1,dato2=input("ingrese 2 numeros separados por espacio : \n").split() # recordemos que el split hace lo mismo que las lineas 2 y 3
if int(dato1)>int(dato2): # si?
    print("el numero mayor es: " + dato1)
elif int(dato1)<int(dato2): # si no otra opcion
    print("el numero mayor es: " + dato2)
#elif int(dato1)==int(dato2): #sino
#    print("los numeros son iguales")
else: #cualqueir otra opcion de descarte
    print("los numeros son iguales")
    
#< ,> ,<= , >= ,==,!= 
    


# In[ ]:


dato1,dato2=input("ingrese 2 numeros separados por espacio : \n").split()
if int(dato1)>int(dato2) or int(dato1)<int(dato2): #sino    #or permite que si se cumple alguna de las 2 condiciones ejecute el codigo 
    print("no me interesa")
else:
    print("los numeros son iguales")
    


# In[29]:


user="jose" 
password="python"
us=input("ingrese su usuario: ")
pas=input("ingrese su contraseña: ")
if user==us and password==pas:
    print("logueado")
elif user==us and password!=pas: 
    print("contraseña incorrecta")
else:
    print("datos incorrectos")


# In[35]:


password="python"
pas=""
contador = 0 #i, j,k

# while es un bucle que se repite infinitamente hasta que se cumpla la condición, si le añado un contador se convierte en un for
while pas!= password and contador<3 :# mientras ->repite mientras la condicion se cumpla
    pas=input("ingrese su contraseña: ")
    contador=contador+1 # los contadores se usan como variables auxiliares, es una variable que se actualiza y aumenta en cada repetición
    print(contador)
    #contador+=1 #otra opcion que hace lo mismo
    if pas!= password:
        print("loging failed")
    else:
        print("loging success")
        contador=4
    

